from pathlib import Path
from html import escape
import shutil

ROOT = Path(__file__).parent
OUT = ROOT / 'dist'
OUT.mkdir(exist_ok=True)

def item(title, text='', meta='', link=''):
    heading = f'<a href="{escape(link)}">{title} <span aria-hidden="true">↗</span></a>' if link else title
    return f'<article class="entry"><p class="meta">{meta}</p><h2>{heading}</h2><p>{text}</p></article>'

pages = {}
pages['research'] = ('Research', 'Understanding how flood adaptation changes risk across people, places, and time.',
    item('Connected and equitable flood adaptation', 'My doctoral research examines how flood adaptation redistributes risk across spatial scales, moving beyond isolated protection toward connected and equitable risk management.', '01 / FLOOD RISK & EQUITY') +
    item('Flood–structure interactions', 'Three-dimensional numerical modelling of flood–building interactions and assessment of flood adaptation strategies.', '02 / HYDRAULICS & MODELLING') +
    item('Nature-based and hybrid adaptation', 'Research interests include wetlands, urban greening, nature-based and hybrid adaptation, and the connections between flood hazards and heat risk.', '03 / CLIMATE RESILIENCE') +
    item('Data and decision support', 'Hydrologic and hydrodynamic modelling, physics-guided and data-driven flood modelling, Earth observation, remote sensing, and geospatial decision support for adaptation planning.', '04 / METHODS'))
pages['education'] = ('Education', 'Civil engineering, hydrology, and climate-risk research.',
    item('Ph.D. in Civil Engineering', '<strong>Indian Institute of Technology Gandhinagar, India</strong><br>CPI: 9.50/10<br>Thesis: <em>Moving Flood Adaptation beyond Isolated Protection towards Connected and Equitable Risk Management across Spatial Scales.</em><br>Supervisor: Dr. Udit Bhatia.<br>Thesis submitted on 14 August 2026; defence expected in October 2026.', 'JULY 2021–PRESENT · THESIS SUBMITTED') +
    item('B.Tech. in Civil Engineering', 'National Institute of Technology Jamshedpur, India<br>CGPA: 7.97/10.', '2016–2020'))
pages['publications'] = ('Publications', 'Publishing as Ashish S. Kumar.',
    item('Dense canopies reverse the cooling effect of urban greening in humid cities.', 'Borah, A., Datta, A., <strong>Kumar, A. S.</strong>, Dave, R., and Bhatia, U.<br><em>Nature Communications</em>, 17, 5997.', '2026 · JOURNAL ARTICLE', 'https://doi.org/10.1038/s41467-026-72636-w') +
    item('Partial flood defenses shift risks and amplify inequality in a core–periphery city.', '<strong>Kumar, A. S.</strong>, Majumder, R., Kapadia, V. P., and Bhatia, U.<br><em>Nature Cities</em>, 2, 835–846.', '2025 · JOURNAL ARTICLE', 'https://doi.org/10.1038/s44284-025-00299-7') +
    item('Three-dimensional numerical study of flood–building interactions to assess the efficiency of flood adaptation strategies.', '<strong>Kumar, A. S.</strong>, Pandey, A. K., Mohapatra, P. K., and Bhatia, U.<br><em>Journal of Hydraulic Engineering</em>, 151(5), 04025028.', '2025 · JOURNAL ARTICLE', 'https://doi.org/10.1061/JHEND8.HYENG-14299') +
    item('Internal climate variability reshapes global extreme-rainfall synchronization networks.', 'Poonia, H., Upadhyay, D., Nikumbh, A. C., <strong>Kumar, A. S.</strong>, Murtugudde, R., and Bhatia, U.<br><em>npj Climate and Atmospheric Science</em>.', 'MANUSCRIPT · UNDER REVIEW'))
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
home = '''<div class="home-intro"><p class="eyebrow">CIVIL ENGINEERING · IIT GANDHINAGAR</p><h1>Ashish<br><span>Kumar.</span></h1><p class="publishing">Publishing as Ashish S. Kumar</p><p class="lead">Understanding flood risk.<br>Working toward equitable adaptation.</p><p>I am a Ph.D. scholar in Civil Engineering at the Indian Institute of Technology Gandhinagar. My research examines how flood adaptation redistributes risk, and how we can move toward connected and equitable resilience.</p><div class="actions"><a class="button" href="research.html">Explore my research ↗</a><a class="text-link" href="cv.html">Curriculum vitae →</a></div></div><aside class="home-note"><span class="note-number">01 / RESEARCH FOCUS</span><h2>Protection in one place.<br>Consequences<br>across a city.</h2><p>I study flood risk across spatial scales, linking hydrodynamic modelling with questions of adaptation and equity.</p><div class="note-foot">Flood modelling<br>Climate adaptation<br>Equitable urban resilience</div></aside><section class="home-bottom"><div><p class="meta">ACADEMIC STATUS</p><h2>Ph.D. thesis submitted</h2><p>14 August 2026 · Supervised by Dr. Udit Bhatia</p><a href="education.html">Education →</a></div><div><p class="meta">SELECTED PUBLICATION · 2025</p><h2>Partial flood defenses shift risks and amplify inequality in a core–periphery city.</h2><p>Nature Cities · 2, 835–846</p><a href="publications.html">View publications →</a></div></section>'''

def render(slug, title, subtitle, body):
    links = ''.join(f'<a href="{s}.html"'+ (' aria-current="page"' if s==slug else '')+f'>{t}</a>' for s,t in nav)
    content = home if slug=='index' else f'<header class="page-heading"><p class="eyebrow">ASHISH KUMAR / {escape(title.upper())}</p><h1>{title}</h1><p class="lead">{subtitle}</p></header><div class="entries">{body}</div>'
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} | Ashish Kumar</title><meta name="description" content="{escape(subtitle, quote=True)}"><meta name="theme-color" content="#102c40"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="assets/style.css"></head>
<body><a class="skip" href="#main">Skip to content</a><div class="layout"><aside class="sidebar"><a class="identity" href="index.html"><span class="monogram">AK<span>.</span></span><strong>Ashish Kumar</strong><small>Flood risk & climate adaptation</small></a><nav aria-label="Main navigation">{links}</nav><div class="sidebar-bottom"><span>IIT Gandhinagar</span><a href="mailto:ashishkumar@iitgn.ac.in">Get in touch ↗</a></div></aside><div class="page"><div class="topline"><span>PERSONAL ACADEMIC WEBSITE</span><a href="https://scholar.google.com/citations?user=hPkHV7cAAAAJ">Google Scholar ↗</a></div><main id="main" class="{'home' if slug=='index' else ''}">{content}</main><footer><span>© Ashish Kumar</span><span>Content updated September 2026</span><a href="https://orcid.org/0000-0002-8632-0915">ORCID ↗</a></footer></div></div></body></html>'''

(OUT/'index.html').write_text(render('index','About','Ashish Kumar — flood risk, climate adaptation, and equitable urban resilience at IIT Gandhinagar.',''),encoding='utf-8')
for slug,(title,subtitle,body) in pages.items():
    (OUT/f'{slug}.html').write_text(render(slug,title,subtitle,body),encoding='utf-8')
(OUT/'assets').mkdir(exist_ok=True)
shutil.copyfile(r'd:\post_doc_applications\jpl_postdoc\ashish_cv_jpl.pdf',OUT/'assets/ashish-kumar-cv.pdf')
print(f'Created {len(pages)+1} pages.')
