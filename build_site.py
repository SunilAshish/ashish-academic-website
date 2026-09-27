from pathlib import Path
from html import escape
import shutil

ROOT = Path(__file__).parent
OUT = ROOT / 'dist'
OUT.mkdir(exist_ok=True)

def item(title, text='', meta='', link=''):
    heading = f'<a href="{escape(link)}">{title} <span aria-hidden="true">↗</span></a>' if link else title
    return f'<article class="entry"><p class="meta">{meta}</p><h2>{heading}</h2><p>{text}</p></article>'

def publication_item(title, citation, meta, doi, logo, logo_alt, preview, preview_alt):
    return f'''<article class="publication-entry">
    <a class="paper-preview" href="{escape(doi)}" target="_blank" rel="noopener">
      <img src="assets/publications/{escape(preview)}" alt="{escape(preview_alt)}" loading="lazy">
      <span>First page <b aria-hidden="true">&nearr;</b></span>
    </a>
    <div class="publication-copy">
      <img class="journal-logo" src="assets/publications/{escape(logo)}" alt="{escape(logo_alt)}" loading="lazy">
      <p class="meta">{meta}</p>
      <h2><a href="{escape(doi)}" target="_blank" rel="noopener">{title} <span aria-hidden="true">&nearr;</span></a></h2>
      <p>{citation}</p>
      <a class="publication-doi" href="{escape(doi)}" target="_blank" rel="noopener">View paper <span aria-hidden="true">&rarr;</span></a>
    </div>
  </article>'''

pages = {}
pages['research'] = ('Research', 'Understanding how flood adaptation changes risk across people, places, and time.',
    item('Connected and equitable flood adaptation', 'My doctoral research examines how flood adaptation redistributes risk across spatial scales, moving beyond isolated protection toward connected and equitable risk management.', '01 / FLOOD RISK & EQUITY') +
    item('Flood–structure interactions', 'Three-dimensional numerical modelling of flood–building interactions and assessment of flood adaptation strategies.', '02 / HYDRAULICS & MODELLING') +
    item('Nature-based and hybrid adaptation', 'Research interests include wetlands, urban greening, nature-based and hybrid adaptation, and the connections between flood hazards and heat risk.', '03 / CLIMATE RESILIENCE') +
    item('Data and decision support', 'Hydrologic and hydrodynamic modelling, physics-guided and data-driven flood modelling, Earth observation, remote sensing, and geospatial decision support for adaptation planning.', '04 / METHODS'))
pages['education'] = ('Education', 'Civil engineering, hydrology, and climate-risk research.',
    item('Ph.D. in Civil Engineering', '<strong>Indian Institute of Technology Gandhinagar, India</strong><br>CPI: 9.50/10<br>Thesis: <em>Moving Flood Adaptation beyond Isolated Protection towards Connected and Equitable Risk Management across Spatial Scales.</em><br>Supervisor: Dr. Udit Bhatia.<br>Thesis submitted on 14 August 2026; defence expected in October 2026.', 'JULY 2021–PRESENT · THESIS SUBMITTED') +
    item('B.Tech. in Civil Engineering', 'National Institute of Technology Jamshedpur, India<br>CGPA: 7.97/10.', '2016–2020'))
pages['publications'] = ('Publications', 'Peer-reviewed research on flood adaptation, urban climate, and equitable resilience.',
    publication_item(
        'Dense canopies reverse the cooling effect of urban greening in humid cities.',
        'Borah, A., Datta, A., <strong>Kumar, A. S.</strong>, Dave, R., and Bhatia, U.<br><em>Nature Communications</em>, 17, 5997.',
        '2026 &middot; JOURNAL ARTICLE',
        'https://doi.org/10.1038/s41467-026-72636-w',
        'nature-communications-logo.png', 'Nature Communications',
        'dense-canopies-first-page.png', 'First page of the Nature Communications article') +
    publication_item(
        'Partial flood defenses shift risks and amplify inequality in a core&ndash;periphery city.',
        '<strong>Kumar, A. S.</strong>, Majumder, R., Kapadia, V. P., and Bhatia, U.<br><em>Nature Cities</em>, 2, 835&ndash;846.',
        '2025 &middot; JOURNAL ARTICLE',
        'https://doi.org/10.1038/s44284-025-00299-7',
        'nature-cities-logo.png', 'Nature Cities',
        'partial-flood-defenses-first-page.png', 'First page of the Nature Cities article') +
    publication_item(
        'Three-dimensional numerical study of flood&ndash;building interactions to assess the efficiency of flood adaptation strategies.',
        '<strong>Kumar, A. S.</strong>, Pandey, A. K., Mohapatra, P. K., and Bhatia, U.<br><em>Journal of Hydraulic Engineering</em>, 151(5), 04025028.',
        '2025 &middot; JOURNAL ARTICLE',
        'https://doi.org/10.1061/JHEND8.HYENG-14299',
        'journal-hydraulic-engineering-logo.png', 'ASCE Journal of Hydraulic Engineering',
        'flood-building-interactions-first-page.png', 'First page of the Journal of Hydraulic Engineering article'))

pages['patents'] = ('Patent applications', 'Methods for understanding spatial and temporal redistribution of flood risk.',
    item('Dual Barcode Method for Quantifying Spatial Redistribution of Dry Land under Flood Protection.', 'Kumar, A. and Bhatia, U.<br>Indian Patent Application No. 202621008727. Filed on 28 January 2026.', '2026 · APPLICATION') +
    item('Protection-Induced Time-Shift Method for Quantifying Temporal Redistribution of Urban Flood Risk.', 'Kumar, A. and Bhatia, U.<br>Indian Patent Application No. 202521103502. Filed on 27 October 2025.', '2025 · APPLICATION'))
talks = [
('2026 · EGU · POSTER', 'Risk redistribution and inequality under partial flood protection in a core–periphery city.', 'Kumar, A., Majumder, R., Kapadia, V. P., and Bhatia, U. EGU26-18151.', 'https://doi.org/10.5194/egusphere-egu26-18151'),
('2025 · EGU · ORAL', 'Flood risk redistribution due to gaps and constraints in adaptation strategies.', 'Kumar, A. and Bhatia, U. EGU25-15089.', 'https://doi.org/10.5194/egusphere-egu25-15089'),
('2025 · AGU · POSTER', 'How Creek Widening and Wetland Buffers Flip Urban Flood Hazards to Protection.', 'Kumar, A., Datta, A., and Bhatia, U. AGU Fall Meeting, New Orleans, LA, NH43D-048.', 'https://ui.adsabs.harvard.edu/abs/2025AGUFMNH43D.048K'),
('2025 · EGU', 'Dynamic Management Strategies for Plant Pollinator Networks under Anthropogenic Warming Scenarios.', 'Datta, A., Kumar, A., Dubey, S., and Bhatia, U. EGU25-779.', 'https://doi.org/10.5194/egusphere-egu25-779'),
('2025 · EGU', 'Quantifying Subsurface Contributions to Compound Flooding in Coastal Urban Areas for Enhanced Resilience.', 'Sutrave, M., Kumar, A., Dave, R., and Bhatia, U. EGU25-867.', 'https://doi.org/10.5194/egusphere-egu25-867'),
('2024 · AGU · ORAL', 'Integrating shared risk into the economic assessment of flood adaptation.', 'Kumar, A. and Bhatia, U. AGU Annual Meeting.', 'https://doi.org/10.22541/essoar.174426927.77603029/v1'),
('2024 · EGU · POSTER', 'Evaluating flood adaptation effectiveness through economic analysis: A case study of Surat, India.', 'Kumar, A. and Bhatia, U. EGU24-7335.', 'https://doi.org/10.5194/egusphere-egu24-7335')]
pages['presentations'] = ('Presentations', 'Research shared at EGU and AGU.', ''.join(item(t, b, m, l) for m,t,b,l in talks))
pages['fieldwork'] = ('Field experience', 'Connecting numerical models with observations on the ground.',
    item('Chaliyar and Kallayi River bathymetry survey', 'Conducted ADCP- and RTK-based bathymetric surveys, generated river cross-sections, collected information on the depth and extent of the 2018 flood, and developed a preliminary riverine flood model.', 'KOZHIKODE, KERALA') +
    item('Railway underpass water-seepage assessment', 'Investigated chronic water seepage and underpass flooding associated with adjacent reservoirs and surface runoff. Delineated the interacting groundwater–surface-water system and developed a modelling strategy for mitigation planning.', 'GONDAL, GUJARAT') +
    item('Flood data collection and site reconnaissance', 'Collected hydrological, hydraulic, reservoir-operation, and historical flood data. Conducted city-wide reconnaissance to understand flood pathways and reconstruct the behaviour of the 2006 flood event.', 'SURAT, GUJARAT') +
    item('Narmada River intake-well survey', 'Conducted an ADCP-based bathymetric survey and mapped riverbed topography near a river intake structure to support water-resource assessment.', 'JHAGADIA, GUJARAT'))
pages['teaching'] = ('Teaching', 'Hydrology, hydraulic modelling, infrastructure, and remote sensing.',
    item('Graduate Teaching Fellow · Hydrology and Hydraulics', 'IIT Gandhinagar<br>Designed and taught laboratory modules in hydrology, hydraulic measurements, hydrological and hydrodynamic modelling, and experimental flume analysis.', 'JUL–NOV 2025') +
    item('PMRF Teaching Fellow · Remote Sensing using Google Earth Engine', 'L.D. College of Engineering<br>Delivered lectures and hands-on laboratory sessions in remote sensing and Google Earth Engine.', 'MAR–MAY 2024') +
    item('Teaching Assistant · Networks and Complex Systems', 'IIT Gandhinagar<br>Guided interdisciplinary course projects and supported student evaluation.', '2022–2024') +
    item('Teaching Assistant · Infrastructure Systems, Planning and Management', 'IIT Gandhinagar<br>Guided projects on infrastructure planning, flood modelling, risk assessment, and resilience.', '2023'))
pages['mentoring'] = ('Mentoring', 'Supporting student research in flood modelling and resilience.',
    item('Master’s thesis mentoring', 'Mentored three Master’s thesis projects on subsurface contributions to compound urban flooding, flood fragility of low-rise buildings, and groundwater-flood mitigation using pumping and underground drainage wells.') +
    item('Undergraduate project mentoring', 'Mentored projects on AI/ML-assisted flood prediction using physics-based modelling and sensor-based real-time urban flood-depth monitoring.'))
pages['skills'] = ('Technical skills', 'Tools and methods spanning field observations, simulation, and spatial analysis.',
    item('GIS, Earth observation, and remote sensing', 'ArcGIS · QGIS · Google Earth Engine<br>DEM processing, raster/vector analysis, flood-hazard and exposure mapping, and spatial-data analysis.') +
    item('Hydrologic and hydraulic modelling', 'MIKE+ 1D–2D · HEC-RAS · ANUGA · HEC-HMS · SWMM · SWAT<br>Riverine, pluvial, urban, and dam-break flood modelling.') +
    item('Computation and analysis', 'ANSYS Fluent · Python · MATLAB · C++ · STATA<br>3-D CFD, flood–structure interaction, large model-output processing, time-series analysis, uncertainty analysis, economic-impact assessment, and machine learning.') +
    item('Field methods', 'ADCP- and RTK-based bathymetric surveys, river cross-section development, flood-depth and inundation surveys, field reconnaissance, and data collection.') +
    item('Scientific communication and collaboration', 'Peer-reviewed publications, technical reports, and oral and poster presentations at EGU and AGU. Interdisciplinary collaboration across hydrology, hydraulics, urban climate, remote sensing, and engineering.') +
    item('Engineering software', 'AutoCAD · STAAD.Pro'))
pages['awards'] = ('Honours & awards', 'Research fellowships and support.',
    item('Prime Minister’s Research Fellowship', 'PMRF · Government of India', '1 AUGUST 2023–16 JULY 2026') +
    item('International Travel Grant', 'Anusandhan National Research Foundation (ANRF), Government of India', '2025'))
pages['service'] = ('Service & interests', 'Contributing to the research community, and life beyond research.',
    item('Session Co-Convener · EGU General Assembly', 'Session BG10.12: “From Urban Heat to Flood Risk: Integrating Geospatial Data, Models, and Observations for Green–Blue Adaptation Strategies.”', '2026') +
    item('Peer review', 'Reviewer for international journals, including <em>Journal of Hydrology</em> and <em>Nature Water</em>.') +
    item('Beyond research', 'I enjoy playing badminton, advancing my swimming skills, and exploring different Indian regional cuisines through cooking.'))
pages['contact'] = ('Contact', 'Get in touch about research and academic collaboration.',
    item('Email', '<a href="mailto:ashishkumar@iitgn.ac.in">ashishkumar@iitgn.ac.in</a>') +
    item('Academic affiliation', 'Department of Civil Engineering<br>Indian Institute of Technology Gandhinagar<br>Gandhinagar, India') +
    item('Research profiles', '<a href="https://scholar.google.com/citations?user=hPkHV7cAAAAJ">Google Scholar ↗</a><br><a href="https://orcid.org/0000-0002-8632-0915">ORCID · 0000-0002-8632-0915 ↗</a>'))
pages['cv'] = ('Curriculum vitae', 'Academic background, research, publications, and experience.', '<div class="cv-panel"><p class="meta">SEPTEMBER 2026</p><h2>Ashish Kumar</h2><p>Publishing as Ashish S. Kumar<br>Ph.D. Scholar · Thesis Submitted<br>IIT Gandhinagar</p><a class="button" href="assets/ashish-kumar-cv.pdf" download>Download CV (PDF) ↓</a><a class="text-link" href="assets/ashish-kumar-cv.pdf">View PDF ↗</a></div>')

nav = [('index','About'),('research','Research'),('publications','Publications'),('education','Education'),('patents','Patents'),('presentations','Presentations'),('fieldwork','Fieldwork'),('teaching','Teaching'),('mentoring','Mentoring'),('skills','Skills'),('awards','Awards'),('service','Service & interests'),('cv','CV'),('contact','Contact')]

collaborators = [
    ('UB', 'Udit Bhatia', 50, 8),
    ('AD', 'Adrija Datta', 68, 12),
    ('RD', 'R. Dave', 82.5, 21),
    ('AB', 'A. Borah', 91, 36.5),
    ('RM', 'R. Majumder', 92, 56),
    ('VK', 'V. P. Kapadia', 85, 73.5),
    ('AP', 'A. K. Pandey', 71, 87),
    ('PM', 'P. K. Mohapatra', 50, 92),
    ('HP', 'H. Poonia', 29, 87),
    ('DU', 'D. Upadhyay', 15, 73.5),
    ('AN', 'A. C. Nikumbh', 8, 56),
    ('RMu', 'R. Murtugudde', 9, 36.5),
    ('SD', 'S. Dubey', 17.5, 21),
    ('MS', 'M. Sutrave', 32, 12),
]

def scholar_search(name):
    return 'https://scholar.google.com/scholar?q=author:%22' + name.replace(' ', '+') + '%22'

collaboration_nodes = ''.join(
    f'<button class="network-node" type="button" style="--x:{x}%;--y:{y}%;--delay:{i * .16:.2f}s" data-initials="{initials}" data-name="{name}" data-role="Research collaborator" data-scholar="{scholar_search(name)}" aria-label="View {name} profile"><span class="node-avatar">{initials}</span><span class="node-name">{name}</span></button>'
    for i, (initials, name, x, y) in enumerate(collaborators, 1)
)
network_lines = ''.join(
    f'<line x1="200" y1="170" x2="{x * 4:g}" y2="{y * 3.4:g}"/>'
    for _, _, x, y in collaborators
)
collaboration_panel = f'''<aside class="collaboration-panel" aria-labelledby="collaboration-title"><div class="network-heading"><p id="collaboration-title">COLLABORATION NETWORK</p><span>14 collaborators · select a node</span></div><div class="network-canvas"><svg class="network-lines" viewBox="0 0 400 340" aria-hidden="true"><g>{network_lines}</g></svg><button class="network-node node-center" type="button" style="--x:50%;--y:50%;--delay:0s" data-initials="AK" data-name="Ashish Kumar" data-role="Flood risk & climate adaptation" data-scholar="https://scholar.google.com/citations?user=hPkHV7cAAAAJ" aria-label="View Ashish Kumar profile"><span class="node-avatar">AK</span><span class="node-name">Ashish Kumar</span></button>{collaboration_nodes}</div></aside>'''

home = f"""<section class="hero"><div class="wrap hero-layout"><div class="hero-copy"><p class="eyebrow">FLOOD RISK · CLIMATE ADAPTATION · EQUITY</p><h1>Understanding flood risk.<br>Rethinking adaptation.</h1><p class="hero-intro">I am Ashish Kumar. My research explores how flood protection reshapes risk across cities, and how that knowledge can guide more connected and equitable adaptation.</p><div class="actions"><a class="button" href="research.html">Explore my research</a><a class="hero-link" href="publications.html">View publications →</a></div></div>{collaboration_panel}</div><dialog class="network-profile" aria-labelledby="network-profile-name"><button class="network-close" type="button" aria-label="Close profile">×</button><div class="profile-avatar" aria-hidden="true">AK</div><p class="profile-label">COLLABORATION NETWORK</p><h2 id="network-profile-name">Ashish Kumar</h2><p class="profile-role">Flood risk & climate adaptation</p><a class="profile-scholar" href="https://scholar.google.com/citations?user=hPkHV7cAAAAJ" target="_blank" rel="noopener">Open Google Scholar ↗</a></dialog></section>
<section class="section"><div class="wrap about-grid"><div><p class="kicker">ABOUT ME</p><h2>Connecting flood science<br>with equitable resilience.</h2><p class="intro">I am a Ph.D. scholar in the Department of Civil Engineering at the Indian Institute of Technology Gandhinagar, supervised by Dr. Udit Bhatia.</p><p>My work brings together hydrologic and hydrodynamic modelling, flood–structure interactions, and geospatial analysis to understand the wider consequences of flood adaptation. I am interested in how protection in one place can change risk elsewhere, and how adaptation planning can account for those connections.</p><p>I publish as <strong>Ashish S. Kumar</strong>.</p><div class="identity-links"><a href="mailto:ashishkumar@iitgn.ac.in">Email ↗</a><a href="https://scholar.google.com/citations?user=hPkHV7cAAAAJ">Google Scholar ↗</a><a href="https://orcid.org/0000-0002-8632-0915">ORCID ↗</a><a href="cv.html">Curriculum vitae ↓</a></div></div><aside class="academic-note"><p class="kicker">IIT GANDHINAGAR</p><h3>Ph.D. in<br>Civil Engineering</h3><p>Thesis submitted<br><strong>14 August 2026</strong></p><p>Moving Flood Adaptation beyond Isolated Protection towards Connected and Equitable Risk Management across Spatial Scales.</p><a href="education.html">My academic journey →</a></aside></div></section>
<section class="section research-preview"><div class="wrap"><p class="kicker">RESEARCH</p><h2>Floods, adaptation,<br>and the risks we share.</h2><div class="research-grid"><article><p class="meta">01 / FLOOD RISK</p><h3>Connected protection</h3><p>Understanding how flood defenses redistribute risk across people, places, and time.</p><a href="research.html">Research interests →</a></article><article><p class="meta">02 / MODELLING</p><h3>From flow to impact</h3><p>Hydrodynamic and three-dimensional numerical modelling of flood–building interactions.</p><a href="publications.html">Related publications →</a></article><article><p class="meta">03 / ADAPTATION</p><h3>Equitable resilience</h3><p>Exploring nature-based and hybrid adaptation, urban climate risk, and decision support.</p><a href="fieldwork.html">Field experience →</a></article></div></div></section>
<section class="section"><div class="wrap"><p class="kicker">SELECTED PUBLICATION · 2025</p><h2 class="selected-title">Partial flood defenses shift risks and amplify inequality in a core–periphery city.</h2><p class="muted">Ashish S. Kumar, R. Majumder, V. P. Kapadia, and U. Bhatia<br><em>Nature Cities</em>, 2, 835–846.</p><a class="text-link" href="publications.html">Browse publications →</a></div></section>
<section class="contact-band"><div class="wrap"><p class="eyebrow">GET IN TOUCH</p><h2>Let’s connect.</h2><p>For research discussions and academic collaboration.</p><a href="mailto:ashishkumar@iitgn.ac.in">ashishkumar@iitgn.ac.in ↗</a></div></section>"""

def render(slug, title, subtitle, body):
    def nav_link(s, t):
        return f'<a href="{s}.html"'+ (' aria-current="page"' if s==slug else '')+f'>{t}</a>'
    primary = [('index','About'),('research','Research'),('publications','Publications'),('education','Education'),('teaching','Teaching'),('fieldwork','Fieldwork')]
    more = [(s,t) for s,t in nav if s not in {n[0] for n in primary} | {'cv','contact'}]
    links = ''.join(nav_link(s,t) for s,t in primary)
    links += '<details class="more-nav"><summary'+ (' class="active"' if slug in dict(more) else '')+'>More <span aria-hidden="true">⌄</span></summary><div class="dropdown">'+''.join(nav_link(s,t) for s,t in more)+'</div></details>'
    links += nav_link('cv','CV') + nav_link('contact','Contact')
    content = home if slug=='index' else f'<section class="page-banner"><div class="wrap"><p class="eyebrow">ASHISH KUMAR</p><h1>{title}</h1><p class="lead">{subtitle}</p></div></section><section class="section"><div class="wrap entries">{body}</div></section>'
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{'Ashish Kumar | Flood Risk & Climate Adaptation' if slug=='index' else title+' | Ashish Kumar'}</title><meta name="description" content="{escape(subtitle, quote=True)}"><meta name="theme-color" content="#012169"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="assets/style.css"></head>
<body id="top"><a class="skip" href="#main">Skip to content</a><header class="site-header"><div class="wrap header-inner"><a class="brand" href="index.html">Ashish Kumar<span>Flood risk & climate adaptation</span></a><nav aria-label="Main navigation">{links}</nav></div></header><main id="main">{content}</main><footer><div class="wrap footer-inner"><span>© Ashish Kumar</span><span>Content updated September 2026</span><a href="#top">Back to top ↑</a></div></footer><script src="assets/navigation.js"></script></body></html>'''

(OUT/'index.html').write_text(render('index','About','Ashish Kumar — flood risk, climate adaptation, and equitable urban resilience at IIT Gandhinagar.',''),encoding='utf-8')
for slug,(title,subtitle,body) in pages.items():
    (OUT/f'{slug}.html').write_text(render(slug,title,subtitle,body),encoding='utf-8')
(OUT/'assets').mkdir(exist_ok=True)
shutil.copyfile(r'd:\post_doc_applications\jpl_postdoc\ashish_cv_jpl.pdf',OUT/'assets/ashish-kumar-cv.pdf')
print(f'Created {len(pages)+1} pages.')
