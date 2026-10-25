# BCS353 – Web Designing Workshop — Complete Assignment (Experiments 1–10)

**Project by: Kanan Tarun Sangal**
**College: GL Bajaj Institute of Technology & Management**

Online Bookstore website (Experiments 1–9) + an integrated **To-Do List** mini
project (Experiment 10), built with plain **HTML5, CSS3 and JavaScript** — no
frameworks required.

## How to run

1. Download / open this folder in any modern browser (Chrome, Firefox, Edge).
2. Open the root **`index.html`** — it is a launcher with links to all 10
   experiments.
3. For Experiment 1 open `Exp01_Homepage_Frames/index.html` (uses HTML frames,
   as required by the assignment).

> Tip: if a browser blocks anything on `file://`, run a local server from this
> folder: `python -m http.server 8000` and open `http://localhost:8000`.

## Folder structure and experiment mapping

| Exp | Folder | What is implemented |
|-----|--------|---------------------|
| 1 | `Exp01_Homepage_Frames/` | Homepage with **three frames** — top (logo, college name, nav: Home/Login/Registration/Catalogue/Cart), left (CSE/ECE/EEE/CIVIL links), right (content pages load here). Uses `<frameset>`/`<frame>` exactly as the syllabus asks. |
| 2 | `Exp02_Login_Page/` | Standalone **Login page** — User Name, Password, Submit & Reset. |
| 3 | `Exp03_Catalogue_Page/` | **Catalogue table** — book cover snapshot, author, publisher, price, Add-to-cart button (10 books). |
| 4 | `Exp04_Cart_Page/` | **Cart page** — book name, price, quantity, amount and total (`$130.5`), matching the prescribed wireframe. |
| 5 | `Exp05_Registration_Form/` | **Registration form** — Name, Password, E-mail, Phone, Sex (radio), DOB (3 select boxes), Languages (English/Telugu/Hindi/Tamil checkboxes), Address (textarea). Pure HTML. |
| 6 | `Exp06_JS_Validation_Name_Password/` | Same form + **JavaScript validation** for Name (alphabets only, ≥ 6 chars) and Password (≥ 6 chars), with inline red error messages. |
| 7 | `Exp07_JS_Validation_Email_Phone/` | Adds **E-mail** validation (`name@domain.com` regex) and **Phone** validation (exactly 10 digits) — all four fields validated. |
| 8 | `Exp08_CSS_Fonts_Background/` | External/internal/inline CSS, element/class/id selectors, different fonts & styles, background image on the **page** and on a **single element**. |
| 9 | `Exp09_CSS_Repeat_Links/` | `background-repeat`: repeat / repeat-x / repeat-y / no-repeat, and link pseudo-classes `a:link`, `a:visited`, `a:hover`, `a:active`. |
| 10 | `Exp10_ToDo_List/` | **Mini project — To-Do List** integrating HTML + CSS + JS: add/complete/delete/filter tasks, empty-input validation, statistics, responsive media query, `localStorage` persistence. |

## Syllabus topics covered

- **HTML:** elements, attributes, headings, paragraphs, styles, comments,
  links, images, favicon, tables, lists, class, id, forms, media, navigation
  bar, frames.
- **CSS:** all three CSS types, colors, backgrounds, margin/padding,
  height/width, text & font properties, links, lists, tables, display, float,
  overflow, round corners, media queries, navigation bar, forms,
  background-repeat, pseudo-classes.
- **JavaScript:** variables, operators, datatypes, functions, output,
  statements, events, string methods, arrays, objects, if-else, loops,
  form validation, DOM manipulation, `localStorage`.

## Notes for submission

- The college name **“GL Bajaj Institute of Technology & Management”** appears
  in `Exp01_Homepage_Frames/frames/top.html` and in all standalone pages, and
  the project owner name **Kanan Tarun Sangal** is shown in the headers and
  footers.
- All book covers, the logo and background patterns are hand-written SVG
  files inside the `images/` folders (generated via
  `_generate_assets.py`), so the project works fully offline.
- HTML `<frameset>` is deprecated in HTML5 but is used in Experiment 1
  because the assignment explicitly requires a three-frame home page; every
  other page uses the modern CSS flexbox layout.
