# Thesis Overview and Design Organizer (TODO 😝)

![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=flat)
![Jupyter Badge](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=fff&style=flat)
![NumPy Badge](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=fff&style=flat)
![SciPy Badge](https://img.shields.io/badge/SciPy-8CAAE6?logo=scipy&logoColor=fff&style=flat)

![LaTeX Badge](https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=fff&style=flat)
![Overleaf Badge](https://img.shields.io/badge/Overleaf-47A141?logo=overleaf&logoColor=fff&style=flat)
![GitHub Badge](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=fff&style=flat)
![Inkscape Badge](https://img.shields.io/badge/Inkscape-000?logo=inkscape&logoColor=fff&style=flat)

<!-- <https://simpleicons.org/> <https://badges.pages.dev/> <https://github.com/badges/shields> -->

<!-- markdownlint-disable MD033 MD038-->
<details>
<summary>Useful Thesis Links</summary>

* <https://www.ufs.ac.za/docs/default-source/regulations-documents/rubric-masters-dissertation-1004-eng.pdf>

</details>
<br>

This file stands to track any minor improvements (at least I think they would be) or final edits needed before the submission of my thesis, my local setup (In case, I don't know, my laptop is stolen 🙄), any styles and style preferences to keep the file/document structure neat and logical, as well as any useful external references.

To any reading, I hope this document serves to improve your write-up experience. ❤️

Worm Regards, 🪱

Justin Cooper

<!-- MARK: Minor TODO's -->
## Minor `TODOs`

* Much empty,
  * such wow

<!-- MARK: Final TODO's -->
## Final `TODOs`

* General
  * SALT RSS → SALT/RSS, etc.
  * Footnotes
* Pre-3.4.3/3.4.2 end/POLSALT pre-reductions
  * spacing

<!-- MARK: @Submission -->
## At Submission

From [General Academic Rules](https://www.ufs.ac.za/docs/default-source/policy-documents-documents/general-academic-rules-and-regulations.pdf?Status=Master&sfvrsn=acb23120_3):

* **Submitted material must contain**:
  * **Style**:
    * There is no standard format for the submission of a dissertation or thesis and formatting is at the candidate's discretion.
    * Reasonable-width margins ($2 - 2.5$ cm)
    * 1,5 line spacing are desirable to ensure comfortable reading of the text.
    * Consistent referencing should be applied, according to departmental styling
    * PDF format (for electronic submission)
      * embedded fonts
  * Abstract (<600 words)
  * ~10 key terms, no less than 5(keywords)
    * **Title page**:
      * Registered research title
      * Student's Full names
      * Declaration:
        * “Submitted in fulfillment of the requirements in respect of the Master’s Degree Master of Science in Astrophysics in the Department of Physics in the Faculty of Natural and Agricultural Sciences at the University of the Free State”
      * Submission date
      * Names of Supervisor(s) (and co-supervisor(s) / Mentor(s))
* **Submitted alongside material**:
  * A summary report compiled in the Turnitin plagiarism search engine
  * A written declaration of approval by the supervisor
  * “I, Justin Cooper, declare that the Master’s Degree research dissertation that I herewith submit for the Master’s Degree qualification Master of Science in Astrophysics at the University of the Free State is my independent work, and that I have not previously submitted it for a qualification at another institution of higher
education” (See [GAR](https://www.ufs.ac.za/docs/default-source/policy-documents-documents/general-academic-rules-and-regulations.pdf?Status=Master&sfvrsn=acb23120_3 "Page 106 for variations"))
* **Provided by Supervisor(s)**:
  * A letter that they approve the submission for assessment and that the submitted work has not previously, either in part or in its entirety, been submitted to the examiners or moderators
  * Proof of the title registration, and
  * proof of appointment of the examiners, with their acceptance of appointment and their addresses for the dispatching of the examination copy.
* **Provided for graduation ceremony programme**:
  * Date of birth
  * Place of birth
  * School of matriculation
  * Professional career
  * Exceptional achievements
  * Marital and familial details
* **And Finally**:
  * Review [This webpage](https://www.ufs.ac.za/library/library-and-information-services-home/research(unlisted)/online-submission-of-electronic-theses-and-dissertations "Library submission")

<!-- MARK: VSCode -->
## VSCode

This section contains the setup I've found irreplaceable while writing my thesis in VSCode, or anything useful in general.

<!-- MARK: 1. setup -->
### General setup

1. My Python setup includes the full `Python` and `Jupyter Notebook` extensions as well as the `Black` and `autopep8` formatting extensions.
    * Python must still be installed locally.
1. I use a private GitHub repo, shared with my supervisor, for backing up and version control of my thesis, as well as for my developed software, in a separate repo (goodbye `backup_thesis_(copy)_v1` folders).
    * Look up [`GitHub Education`](https://github.com/education "GitHub Education Homepage") if you are a registered student. It provides both a pro version of GitHub (Private repository advanced features, such as sharing) as well as access to GitHub's Copilot (You're welcome).
1. I use the `Latex Workshop` and the `LTex - LanguageTool grammar/spell chacking` extensions to use $\LaTeX$ in VSCode.
    * $\LaTeX$ must still be installed locally (I use `Tex Live` as recommended by `Latex Workshop`).
1. I use GitHub Copilot for its predictive text and as a first stop for problem shooting as the currently open file is included in its context.
1. I use `markdownlint` for linting Markdown documents.

<!-- MARK: 2. shortcuts -->
### [Useful shortcuts](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)

<div align=center>

  | Keyboard Shortcut | Use |
  |------------------:|:----|
  | <kbd>Ctrl</kbd>+<kbd>k</kbd>, <kbd>v</kbd> | VSCode View rendered markdown |
  | <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> | Open Command Palette |
  | <kbd>Ctrl</kbd>+<kbd>k</kbd>, <kbd>Ctrl</kbd>+<kbd>s</kbd> | View VSCode shortcuts |
  | <kbd>Ctrl</kbd>+<kbd>`</kbd>| Open Terminal |
  | <kbd>Ctrl</kbd>+<kbd>k</kbd>, <kbd>z</kbd> | Zen mode |
  | (Hold) <kbd>Alt</kbd>, <kbd>Click(s)</kbd> | Multiple cursors |
  | <kbd>Alt</kbd>+(<kbd>↑</kbd>\|<kbd>↓</kbd>) | Move line up/down |
  | <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+(<kbd>↑</kbd>\|<kbd>↓</kbd>) | Insert cursor above/below |
  | <kbd>Ctrl</kbd>+<kbd>Click</kbd> | SyncTex: Link from PDF to source |
  | <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>j</kbd> | SyncTex: Link from source to PDF |
  | <kbd>Ctrl</kbd>+<kbd>,</kbd>, Search: `invert` | Latex Workshop: Invert PDF color scheme |
  |  |  |

</div>

[VSCode] also includes the ability to insert code snippets. I've set up a few frequently used code snippets, but there is, as always, much to be improved upon. See [this file](./.vscode/Writeup_snippets.code-snippets 'My Writeup code snippets') for where to implement them as well as my code snippets.[^vs_snip]

[^vs_snip]: If the relative link breaks due to the `.gitignore` file, see [this page](https://code.visualstudio.com/docs/editor/userdefinedsnippets 'Snippets in VSCode') for more information on [VSCode] code snippets.

<!-- MARK: 3. RegEx -->
### Useful RegEx patterns

RegEx allows for complex `find` and `replace` functionality. It may also be used in the VSCode `Search` tab in the primary sidebar (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>F</kbd>)

* `()` represent capture groups in `find` which may be referred to later in `replace` using `$1`, etc.
* `[]` represent character groups in `find`.
* Quantifiers such as `+`, `*`, etc. allow for more complex behavior, especially combined with [greedy and lazy quantifiers](https://javascript.info/regexp-greedy-and-lazy).

Here are some useful RegEx patterns I have needed:

<div align=center>

  | Regex use | Find | Replace |
  |:---------:|-----:|:--------|
  | `John {Smith}` → `{Smith}, J.` | `([A-Z])[a-z]*?\s(\{[A-Z].+?\})` | `$2, $1.` |
  | `E. J {Powell}` → `{Powell}, E. J.` | `(?<=and\s)([A-Z]\.\|[A-Z]\.\s[A-Z]\.)\s(\{.+?\})` | `$2, $1` |
  | `1 \| 1.1` → `$1$ \| $1.1$` | `\s([0-9][\.]*[0-9]*)\s*` | `$$$1$` |
  | `.../:version: ...` → `version: ...` | `^[^:]*:\s*` | ` ` |

</div>

I have also made use of `grep` for finding RegEx patterns within files using a CLI:

```console
grep -ri 'version: ' > version.txt
```

where the `r` flag is used for a recursive search in the working directory, and the `i` flag ignores the RegEx case.
Combining this with the [VSCode] \`find and replace', \`delete duplicates', and \`sort lines ascending' results in a sanitized version list of all polsalt/pysalt software.

<!-- MARK: 4. md -->
### Markdown

<details>
<summary>Useful Links</summary>

* <https://www.markdownguide.org/basic-syntax/>
* <https://ashki23.github.io/markdown-latex.html>
* <https://daringfireball.net/projects/markdown/syntax>

</details>
<br>

This section contains any markdown not used in this document but deemed useful nonetheless.

* Use `[//]: # (Comment)` or `<!-- Comment -->` on a separate line for comments not meant for rendering.
* Use `[^end_text]: A comment that renders as an endnote.`
  * Only works in some Markdown viewers (I.E. GitHub)
* Comments that link to a separate file may link to a specific line within the file using the `#L` suffix.
  * [Thesis.tex line 20 (Hover)](/Thesis.tex#L20 "[Link text](/Thesis.tex#L20 'Hover text')")

<!-- MARK: 5. Tips/Tricks -->
### Tips and Tricks

Here are some general tips and tricks related to VSCode that do not fit neatly into any of the other sections.

* `MARK: Heading` within a comment of a document allows for headings in the VSCode code map, allowing for navigation at a glance.

<!-- MARK: LaTeX Styles -->
## $\LaTeX$ Style guides

<details>
<summary>Useful Links</summary>

* <https://www.learnlatex.org/en/>
* <https://en.wikibooks.org/wiki/LaTeX>
* <https://github.com/James-Yu/LaTeX-Workshop/wiki>
* <https://ashki23.github.io/markdown-latex.html>

</details>
<br>

Included herein are the style guides I have followed during the course of writing my thesis. Custom styles (`my*.sty files`) have been included to both simplify the preamble (located in `Thesis.tex`) and to create a more homogeneous styling throughout when dealing with the relevant packages contained in the style files.

General Notes:

* Inline values with units should be formatted as: `$val$~unit`
  * If the value is a quantifier, consider writing it out
    * i.e. `... 7 filters ...` becomes `... seven filters ...`
* labels are defined using `\label{}`
* Commands may be defined with `\def` but may also be defined using `\newcommand\eg{}`, `\renewcommand\eg{}`, or `\providescommand\eg{}`, which all define new commands that may be used, with differing failure states
  * `\newcommand` crashes when overwriting
  * `\renewcommand` crashes when **not** overwriting, and
  * `\providescommand` attempts to create a new command (I believe exclusively in meta files, I.E. `.sty`, etc.)

<!-- MARK: PRE - hyperref -->
### `hyperref`

$\LaTeX$'s `hyperref` package allows for linking within a PDF as well as setting up the document's metadata properties. The [`hyperref.cfg`](./hyperref.cfg) file is where the metadata is stored.

| Link Types | Description |
| --- | --- |
| `\autoref{label}` | internal reference to `label`, prefixed with (I.E. $\S$, etc.) |
| `\ref{label}` | internal reference to `label`, no prefix text |
| `autopageref{label}` | internal reference to page of `label`, prefixed with (I.E. p.) |
| `\pageref{label}` | internal reference to page of `label`, no prefix text |
| `\href{URL}{text}` | any `URL`'s with anchor `text` |
| `\url{URL}` | any raw `URL` |
| `\hyperref{URL}{category}{name}{text}` | `text` link to `URL` |
| `\hyperref[label]{text}` | `text` link to `label` |

See also the documentation using: `texdoc hyperref`

<!-- MARK: PRE - glossary -->
### Glossary and Acronyms

$\LaTeX$'s `glossaries-extra` allow keywords and acronyms to be defined and used and stated in full on first use. Note that acronyms used for software use a display text in the small caps font.

```Latex
% Glossary entries
\newglossaryentry{maths}
{%
    name=mathematics,
    description={Mathematics is what mathematicians do}
}

\gls{maths} -> mathematics
\Gls{maths} -> Mathematics
\glspl{maths} -> mathematics
\Glspl{maths} -> Mathematics

% Acronym entries
\newacronym{gcd}{GCD}{Greatest Common Divisor}

\acrlong{} -> Greatest Common Divisor
\acrshort{} -> GCD
\acrfull{} -> Greatest Common Divisor (GCD)
```

New commands for the most common glossary/acronym keys may improve 'writability' (`\acr{POLSALT}` vs `\polsalt`). This was implemented for all software acronyms. See also the documentation using: `texdoc glossaries-extra`

<!-- MARK: 1. Headings -->
### Headings

My headings use `Title Case`.[^head_case] Generally, labels are only included when necessary and are not compulsory when creating a new section, etc.

```Latex
% Note case is `Title Case`
\chapter{Chapter Title}
\section{Section Title} \label{sec:sec_title}
\dots
```

[^head_case]: `Sentence case` may also be used, just stick to whichever style is chosen.

<!-- MARK: 2. Equations -->
### Equations

Equations are written in-text and are a part of sentences unless otherwise indicated. To this end, there is no new line before `\begin` or after `\end` (unless the sentence ends with the equation and the equation is punctuated) and multiple equations in a single environment are properly punctuated.

**Note**: multi-line, or continued, equations are aligned by the `=` symbol while related equations within one environment are aligned by centering.

```Latex
% Align center
\begin{equation} \label{eq:name}
    eq \,[,|.]
\end{equation}

% Align center, ignore end text
\begin{equation} \label{eq:name}
    \begin{gathered}
        eq1 = ... \,,\\
        eq2 = ... \rlap{\,,\ and}\\
        eq3 = ...
    \end{gathered}
\end{equation}

% Align by `=', ignore end text
\begin{equation} \label{eq:name}
    \begin{aligned}
      eq1 &= ... \,,\\
      eq2 &= ... \rlap{\,,\ and}\\
      eq3 &= ...
    \end{aligned}
\end{equation}
```

See references (Wikibooks) for more configurations of equations.

<!-- MARK: 3. Figures -->
### Figures

Figures are located in their relevant chapter (`chapter_*/figures/`) and have the chapter number, $i$, prepended to their name (`<i>_<name>.[pdf|svg]`).

The figures included in the document are `pdf`'s, but it is useful to save a copy of self-generated figures as `svg`'s for when edits to the figure will naturally arise. See 'Custom Figures' for further constraints on generated figures. [FITS] images are also saved as `pdf`, but may have a lower `dpi` as compared to other figures when not much detail is needed for the figure.

To use the figures in the $\LaTeX$ document, use:

```Latex
\begin{figure}[t]
    \centering
    \includegraphics[width = 1.0\textwidth]{'<i>_<name>.[pdf|png]'}
    \caption{Include a suitable caption here. Figure (if cited: 'adapted from', if own: 'created using') 'source'.(if link: \protect\footnotemark)}
    \label{fig:'suitable_label'}
\end{figure}
\footnotetext{\protect\url{(link)}}
```

or, for sub-figures, use:

```Latex
\begin{figure}[t]
    \centering
    \begin{subfigure}[b]{0.49\textwidth}
        \centering
        \includegraphics[width = 1.0\textwidth]{fig1.extension}
        \caption{fig1 caption}
        \label{subfig:fig1_label}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.49\textwidth}
        \centering
        \includegraphics[width = 1.0\textwidth]{fig2.extension}
        \caption{fig2 caption}
        \label{subfig:fig2_label}
    \end{subfigure}
    \caption{Overall caption}
    \label{fig:fig_caption}
\end{figure}
```

#### Custom Figures

Figures created by myself are (generally) made using Inkscape. To keep line widths / text size / etc. consistent the following document properties are used:

* Document properties
  * $6.28$ ($160mm$) x ? inches
    * $x$-size set to the $\LaTeX$ `\textwidth` (usually in inches)
      * (`\textwidth` found by using `\the\textwidth` anywhere in the $\LaTeX$ document)
      * $6.28$ inches == $A4$ page with uniform $1$ inch border.
    * $y$-size depends on figure aspect ratio, usually left undefined
  * Before saving, use `resize to content` (if no text included in custom figure)
  * scale = $0.1$

* Grid properties
  * $s_x$, $s_y$ = $1$ mm
  * Major Grid every $5$

* Fill properties
  * Lightness = $66$
  * (I.E. $0$, $0$, $66$, $100$)

* Font properties
  * `CMU Serif` for text
  * `CMU Serif Italics` for symbols
  * weight = normal
  * size = $12$ pt

* Stroke properties
  * width = $1$ px

See also: <https://jwalton.info/Matplotlib-latex-PGF/>

Figures are first saved as an `svg` before being exported as either a `png` or `pdf` to 'play well' with the $\LaTeX$ `\includegraphics[]{}` command.

<!-- MARK: TikZ -->
#### $TikZ$ Figures

<details>
<summary>Useful Links</summary>

* <https://www.baeldung.com/cs/latex-flowcharts>
* <https://www.overleaf.com/learn/latex/LaTeX_Graphics_using_TikZ%3A_A_Tutorial_for_Beginners_(Part_3)%E2%80%94Creating_Flowcharts>

</details>
<br>

$TikZ$ refers to the `tikz` package (which may include libraries) which can generate figures and diagrams, etc. The relevant preamble commands are:

```Latex
\usepackage{tikz}
\usetikzlibrary{shapes.geometric, arrows} % specifically for flowcharts
```

The preamble must also include the definitions of any required `tikzstyle` definitions. Styles may include nodes and lines:

```Latex
\tikzstyle{ends} = [rectangle, draw, text centered, rounded corners, minimum height=2em]
\tikzstyle{step} = [rectangle, draw, text centered, minimum height=2em]
\tikzstyle{choice} = [diamond, draw, text centered, minimum height=2em]
\tikzstyle{data}=[trapezium, draw, text centered, trapezium left angle=60, trapezium right angle=120, minimum height=2em]
\tikzstyle{to} = [draw, -latex']
```

and may be included in a document using:

```Latex
\begin{figure}[t]
    \centering
    \begin{tikzpicture}
        \node (name) [type, right of=(name), below of=(name), xshift=2cm, yshift=2cm] {text};
        \draw [to] (name_from) -- (name_to);
        \draw [arrow] (name_from) -- node[anchor=east] {yes} (name_to_yes);
        \draw [arrow] (name_from) -- node {no} (name_to_no);
    \end{tikzpicture}
    \caption{File caption}
    \label{fig:file_label}
\end{figure}
```

<!-- MARK: 4. Tables -->
### Tables

Tables can be generated using a [$\LaTeX$ Table Generator](https://www.tablesgenerator.com/). Tables are located in their relevant chapter (`chapter_*/tables/`) and have the chapter number, $i$, prepended to their name (`<i>_<name>.tex`). The contents of the file are structured similar to:

```Latex
\begin{table}[t]
    \centering
    \begin{tabular}{c(* the amount of columns)}
        ...
    \end{tabular}
    \caption{A suitable caption and relevant reference.\protect\footnotemark}
    \label{table:'suitable_label'}
\end{table}
\footnotetext{Link or further description of reference or discussion of footnotemark in text.}
```

To insert a table within the document, use the command:

```Latex
\input{chapter_<i>/tables/table_name.tex}
```

<!-- MARK: References -->
## Useful external References

* Glossaries (minor to-do's): <https://www.overleaf.com/learn/latex/Glossaries>
  * Useful glossary and acronym simultaneous addition: <https://tex.stackexchange.com/questions/8946/how-to-combine-acronym-and-glossary>
  * Glossary style <https://www.dickimaw-books.com/gallery/glossaries-styles/>
* GitHub `.cff` file references: <https://citation-file-format.github.io/>

See 'preamble' of `references.bib` for further useful links relevant to specific chapters of thesis.

<!-- Hidden References -->
[FITS]: <https://fits.gsfc.nasa.gov/standard40/fits_standard40aa-le.pdf> (The FITS Standard)
[VSCode]: <https://code.visualstudio.com/> (VSCode Homepage)

<!-- `e.g., ` (exempli gratia, Latin for \`for example') -->
<!-- `i.e., ` (id est, Latin for \`that is') -->