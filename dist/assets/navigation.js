const more = document.querySelector('.more-nav');
if (more) {
  document.addEventListener('click', (event) => {
    if (!more.contains(event.target)) more.open = false;
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && more.open) {
      more.open = false;
      more.querySelector('summary').focus();
    }
  });
}

const networkDialog = document.querySelector('.network-profile');
if (networkDialog) {
  const networkCanvas = document.querySelector('.network-canvas');
  const collaborationPanel = document.querySelector('.collaboration-panel');
  const networkNodes = [...document.querySelectorAll('.network-node:not(.node-center)')];
  const networkLines = [...document.querySelectorAll('.network-lines line')];
  const networkHint = document.querySelector('.network-heading span');
  const profileAvatar = networkDialog.querySelector('.profile-avatar');
  const profileName = networkDialog.querySelector('#network-profile-name');
  const profileRole = networkDialog.querySelector('.profile-role');
  const profileScholar = networkDialog.querySelector('.profile-scholar');
  const closeButton = networkDialog.querySelector('.network-close');
  const motionPreference = window.matchMedia('(prefers-reduced-motion: reduce)');
  let selectedNode = null;
  let suppressNodeClick = false;
  let dragging = false;
  let dragDistance = 0;
  let lastPointerX = 0;
  let lastPointerY = 0;
  let rotationX = -0.16;
  let rotationY = 0.35;
  let lastFrame = performance.now();
  let networkExpanded = false;

  const networkHomeMarker = document.createComment('collaboration-network-home');
  collaborationPanel.before(networkHomeMarker);
  const explorerDialog = document.createElement('dialog');
  explorerDialog.className = 'network-explorer';
  explorerDialog.setAttribute('aria-label', 'Expanded collaboration network');
  const explorerClose = document.createElement('button');
  explorerClose.className = 'network-explorer-close';
  explorerClose.type = 'button';
  explorerClose.setAttribute('aria-label', 'Close expanded network');
  explorerClose.textContent = '×';
  explorerDialog.append(explorerClose);
  document.body.append(explorerDialog);

  const restoreNetwork = () => {
    if (!networkExpanded) return;
    networkHomeMarker.after(collaborationPanel);
    collaborationPanel.classList.remove('is-expanded');
    networkExpanded = false;
    networkHint.textContent = 'Drag to rotate · click to enlarge';
    requestAnimationFrame(renderSphere);
  };

  const expandNetwork = () => {
    if (networkExpanded) return;
    explorerDialog.append(collaborationPanel);
    collaborationPanel.classList.add('is-expanded');
    networkExpanded = true;
    networkHint.textContent = 'Drag to rotate · select a node';
    explorerDialog.showModal();
    requestAnimationFrame(renderSphere);
  };

  const expandButton = document.createElement('button');
  expandButton.className = 'network-expand';
  expandButton.type = 'button';
  expandButton.setAttribute('aria-label', 'Enlarge collaboration network');
  expandButton.textContent = '⛶';
  document.querySelector('.network-heading').append(expandButton);
  expandButton.addEventListener('click', (event) => {
    event.stopPropagation();
    expandNetwork();
  });
  explorerClose.addEventListener('click', () => explorerDialog.close());
  explorerDialog.addEventListener('click', (event) => {
    if (event.target === explorerDialog) explorerDialog.close();
  });
  explorerDialog.addEventListener('close', () => {
    restoreNetwork();
    expandButton.focus();
  });

  const goldenAngle = Math.PI * (3 - Math.sqrt(5));
  const spherePoints = networkNodes.map((node, index) => {
    const y = 1 - (index / (networkNodes.length - 1)) * 2;
    const radius = Math.sqrt(1 - y * y);
    const theta = index * goldenAngle;
    return {
      node,
      line: networkLines[index],
      x: Math.cos(theta) * radius,
      y,
      z: Math.sin(theta) * radius,
    };
  });

  const photoExtensions = ['jpg', 'png', 'webp'];
  document.querySelectorAll('.network-node').forEach((node) => {
    const slug = node.dataset.name.toLowerCase().replace(/\./g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
    const avatar = node.querySelector('.node-avatar');
    const tryPhoto = (index = 0) => {
      if (index >= photoExtensions.length) return;
      const photo = new Image();
      photo.className = 'node-photo';
      photo.alt = '';
      photo.addEventListener('load', () => {
        node.dataset.photo = photo.src;
        avatar.append(photo);
      }, { once: true });
      photo.addEventListener('error', () => tryPhoto(index + 1), { once: true });
      photo.src = `assets/collaborators/${slug}.${photoExtensions[index]}`;
    };
    tryPhoto();
  });

  const renderSphere = () => {
    const cosY = Math.cos(rotationY);
    const sinY = Math.sin(rotationY);
    const cosX = Math.cos(rotationX);
    const sinX = Math.sin(rotationX);

    spherePoints.forEach((point) => {
      const xAfterY = point.x * cosY - point.z * sinY;
      const zAfterY = point.x * sinY + point.z * cosY;
      const yAfterX = point.y * cosX - zAfterY * sinX;
      const zAfterX = point.y * sinX + zAfterY * cosX;
      const depth = (zAfterX + 1) / 2;
      const xPercent = 50 + xAfterY * (35 + depth * 4);
      const yPercent = 50 + yAfterX * (38 + depth * 3);
      const scale = 0.7 + depth * 0.38;

      point.node.style.left = `${xPercent}%`;
      point.node.style.top = `${yPercent}%`;
      point.node.style.transform = `translate(-50%,-50%) scale(${scale})`;
      point.node.style.opacity = 0.5 + depth * 0.5;
      point.node.style.zIndex = Math.round(depth * 20 + 3);
      point.line?.setAttribute('x2', (xPercent * 4).toFixed(2));
      point.line?.setAttribute('y2', (yPercent * 3.4).toFixed(2));
      if (point.line) point.line.style.opacity = 0.28 + depth * 0.6;
    });
  };

  const animateSphere = (now) => {
    const elapsed = Math.min(now - lastFrame, 40);
    if (!dragging && !motionPreference.matches && !networkDialog.open) {
      rotationY += elapsed * 0.00014;
    }
    renderSphere();
    lastFrame = now;
    requestAnimationFrame(animateSphere);
  };

  networkCanvas.tabIndex = 0;
  networkCanvas.setAttribute('aria-label', 'Interactive collaboration network. Drag or use arrow keys to rotate, then select a person.');
  networkHint.textContent = 'Drag to rotate · click to enlarge';

  collaborationPanel.addEventListener('click', (event) => {
    if (networkExpanded || suppressNodeClick || event.target.closest('.network-node') || event.target.closest('.network-expand')) return;
    expandNetwork();
  });

  networkCanvas.addEventListener('pointerdown', (event) => {
    if (event.button !== 0) return;
    if (event.target.closest('.network-node')) return;
    dragging = true;
    dragDistance = 0;
    lastPointerX = event.clientX;
    lastPointerY = event.clientY;
    networkCanvas.classList.add('is-dragging');
    networkCanvas.setPointerCapture(event.pointerId);
  });

  networkCanvas.addEventListener('pointermove', (event) => {
    if (!dragging) return;
    const deltaX = event.clientX - lastPointerX;
    const deltaY = event.clientY - lastPointerY;
    dragDistance += Math.hypot(deltaX, deltaY);
    rotationY += deltaX * 0.011;
    rotationX = Math.max(-1.25, Math.min(1.25, rotationX - deltaY * 0.009));
    lastPointerX = event.clientX;
    lastPointerY = event.clientY;
    renderSphere();
    event.preventDefault();
  });

  const endDrag = (event) => {
    if (!dragging) return;
    dragging = false;
    networkCanvas.classList.remove('is-dragging');
    if (networkCanvas.hasPointerCapture(event.pointerId)) networkCanvas.releasePointerCapture(event.pointerId);
    if (dragDistance > 6) {
      suppressNodeClick = true;
      window.setTimeout(() => { suppressNodeClick = false; }, 120);
    }
  };

  networkCanvas.addEventListener('pointerup', endDrag);
  networkCanvas.addEventListener('pointercancel', endDrag);
  networkCanvas.addEventListener('keydown', (event) => {
    const step = 0.13;
    if (event.key === 'ArrowLeft') rotationY -= step;
    else if (event.key === 'ArrowRight') rotationY += step;
    else if (event.key === 'ArrowUp') rotationX = Math.min(1.25, rotationX + step);
    else if (event.key === 'ArrowDown') rotationX = Math.max(-1.25, rotationX - step);
    else return;
    renderSphere();
    event.preventDefault();
  });

  document.querySelectorAll('.network-node').forEach((node) => {
    node.addEventListener('click', () => {
      if (suppressNodeClick) return;
      selectedNode = node;
      profileAvatar.textContent = node.dataset.initials;
      profileAvatar.classList.toggle('has-photo', Boolean(node.dataset.photo));
      profileAvatar.style.backgroundImage = node.dataset.photo ? `url("${node.dataset.photo}")` : '';
      profileName.textContent = node.dataset.name;
      profileRole.textContent = node.dataset.role;
      profileScholar.href = node.dataset.scholar;
      networkDialog.showModal();
    });
  });

  profileScholar.addEventListener('click', (event) => {
    const scholarUrl = profileScholar.href;
    if (!scholarUrl) return;
    event.preventDefault();
    const scholarWindow = window.open(scholarUrl, '_blank', 'noopener,noreferrer');
    if (!scholarWindow) window.location.href = scholarUrl;
  });

  closeButton.addEventListener('click', () => networkDialog.close());
  networkDialog.addEventListener('click', (event) => {
    if (event.target === networkDialog) networkDialog.close();
  });
  networkDialog.addEventListener('close', () => selectedNode?.focus());
  renderSphere();
  requestAnimationFrame(animateSphere);
}
