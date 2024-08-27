# Thesis Overview and Design Organizer (TODO 😝)

<!-- markdownlint-disable MD033-->
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

* Update tables `\input{}` to use relative pathing (`import` package?)
* Use the `minted` package instead of the `listings` `STOPS_docs` style workaround
* Unify (x-pixel/y-pixel/x/y/wavelength/) or vertical/horizontal axis or rows/columns
  * → (?) ($x_p$, $y_p$)/(\AA, $y_p$) | ($u$, $v$) for pixel position and $s_{u|v}$ for pixel ($x$|$y$) size
* STOPS: skylines legend use [double markers](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-handlers "matplotlib.org")
* Edit created plots to use $\LaTeX$ font (both Python and Inkscape figures)
  * Edit plots to use `subfigures` where possible (?)
  * (?) <https://jwalton.info/Matplotlib-latex-PGF/>
* Align `continued` equations by `=`, align `related` equations by centering (see Equations style guide)
* Limit paragraph breaks to only `left-to-right` pages, not across a page turn.
* O[arc/beam/etc.] → [arc/beam/etc.]O
* Check common errors:
  * \$O\$- and \$E\$-beam(s)
  * `extension`
  * `the user` instead of `a user`
  * `$#$~unit` instead of `# $unit$`

<!-- MARK: Final TODO's -->
## Final `TODOs`

* Organize Glossary entries:
  * Glossary (Alphabetical)
  * Abbreviations, Acronyms, and Symbols (By group(?)/category, then Alphabetical)
  * Unify usage of exposure / frame / extension and add to glossary (see references)
* Cite STOPS as repo? (See `.cff` references)
* Change \today to MONTH, YEAR at final submission in [Thesis text](/Thesis.tex#L194)
* Ask for read through from friends to ensure no spelling/grammar errors

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
  | `1 \| 1.1` → `$1$ \| $1.1$` | `\s([0-9][\.]*[0-9]*)\s*` | `$$$1$` |

</div>

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
  * $6.28$ x ? inches
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
  * name = cmr10
  * weight = normal
  * size = $16$ px

* Stroke properties
  * width = $1$ px

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

<!-- MARK: 5. Glossaries -->
### Glossary and Acronyms

Glossary and acronym entries are implemented throughout the thesis. Glossaries allow keywords to be defined while acronyms allow acronyms to be used and stated in full on first use. Note that acronyms used for software use a display text in the small caps font.

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
\Glspl{maths} -> mathematics

% Acronym entries
\newacronym{gcd}{GCD}{Greatest Common Divisor}

\acrlong{} -> Greatest Common Divisor
\acrshort{} -> GCD
\acrfull{} -> Greatest Common Divisor (GCD)
```

New commands for the most common glossary/acronym keys may improve 'writability' (`\acr{POLSALT}` vs `\polsalt`). This was implemented for all software acronyms.

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
