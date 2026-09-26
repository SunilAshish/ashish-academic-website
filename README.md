# Ashish Kumar — personal academic website

Every section has its own HTML page in `dist/`. Open `dist/index.html` in a browser to use the website locally. No installation is needed.

## Editing a page

For a quick change, open the corresponding HTML file in a text editor and edit the text inside `<main>`. For example, publications are in `dist/publications.html` and teaching is in `dist/teaching.html`. Navigation appears on every page, so update it in all pages if adding or renaming a section.

Shared colours, fonts, and layouts are in `dist/assets/style.css`. Replace `dist/assets/ashish-kumar-cv.pdf` to update the downloadable CV.

## Regenerating all pages

`build_site.py` contains the original page content and shared layout. Edit it and run Python to regenerate all HTML pages. This overwrites direct edits to the HTML files. The final command in the script copies the source CV from its original location; update that path if the CV moves.

Choose either direct HTML editing or the generator as your usual workflow. The website itself does not require Python. A small optional JavaScript file closes the More menu when clicking outside it or pressing Escape; the navigation also works without JavaScript.

All academic details were transcribed or summarized from the September 2026 supplied CV. Publication status and degree status reflect that document. Telephone number and nationality are omitted from the website biography; the original downloadable CV retains its content.
