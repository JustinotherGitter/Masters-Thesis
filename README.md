# Thesis Overview and Design Organizer (TODO 😝)

This file stands to track any minor improvements (at least I think they would be) or final edits needed before the submission of my thesis, my local setup (In case, I don't know, my laptop is stolen 🙄), any styles and style preferences to keep the file/document structure neat and logical, as well as any useful external references.

To any reading, I hope this document serves to improve your write-up experience. ❤️

Worm Regards,

Justin Cooper

## Minor `TODOs`

* Update tables `\input{}` to use relative pathing (`import` package?)
* Use the `minted` package instead of the `listings` `STOPS_docs` style workaround
* Unify (x-pixel/y-pixel/x/y/wavelength/) or vertical/horizontal axis or rows/columns
  * → (?) ($x_p$, $y_p$)/(\AA, $y_p$)
* Edit created plots to use Latex font (both Python and Inkscape figures)
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

## Final `TODOs`

* Organize Glossary entries:
  * Glossary (Alphabetical)
  * Abbreviations, Acronyms, and Symbols (By group(?)/category, then Alphabetical)
  * Unify usage of exposure / frame / extension and add to glossary (see references)
* Cite STOPS as repo? (See `.cff` references)
* Change \today to MONTH, YEAR at final submission [Thesis.tex:197~ish]
* Ask for read through from friends to ensure no spelling/grammar errors

## VSCode

This section contains the setup I've found irreplaceable while writing my thesis in VSCode, or anything useful in general.

### General setup

1. My Python setup includes the full `Python` and `Jupyter Notebook` extensions as well as the `Black` formatting extension.
    * Python must still be installed locally
1. I use a private GitHub repo, shared with my supervisor, for backing up and version control of my thesis, as well as for my developed software, in a separate repo (goodbye `backup_thesis_(copy)_v1` folders).
    * Look up `GitHub Education` if you are a registered student (You're welcome)
1. I use the `Latex Workshop` and the `LTex - ...` extensions to use Latex in VSCode.
    * Latex must still be installed locally (I use `Tex Live` as recommended by `Latex Workshop`)
1. I use GitHub Copilot for its predictive text and as a first stop for problem shooting as the currently open file is included in its context.

### [Useful shortcuts](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)
<div align=center>

  | Keyboard Shortcut | Use |
  |------------------:|:----|
  | <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>p</kbd> | Open Command Palette |
  | <kbd>Ctrl</kbd>+<kbd>k</kbd>, <kbd>v</kbd> | VSCode View rendered [md](https://www.markdownguide.org/basic-syntax/) |
  | <kbd>Ctrl</kbd>+<kbd>k</kbd>, <kbd>Ctrl</kbd>+<kbd>s</kbd> | View VSCode shortcuts |
  |<kbd>Ctrl</kbd>+<kbd>`</kbd>| Open Terminal |
  | <kbd>Ctrl</kbd>+<kbd>k</kbd>, <kbd>z</kbd> | Zen mode |
  | (Hold) <kbd>Alt</kbd>, <kbd>Click(s)</kbd> | Multiple cursors |
  | <kbd>Alt</kbd>+(<kbd>↑</kbd>\|<kbd>↓</kbd>) | Move line up/down |
  | <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+(<kbd>↑</kbd>\|<kbd>↓</kbd>) | Insert cursor above/below |

</div>

### Useful regex patterns

Regex allows for complex find and replace functionality.

* `()` represent capture groups which may be referred to later using `$1`, etc.
* `[]` represent character groups
* Quantifiers such as `+`, `*`, etc. allow for more complex behavior, especially combined with greedy and lazy matching

Here are some useful regex patterns I have needed:

<div align=center>

  | Regex use | Find | Replace |
  |:----------|:----:|--------:|
  |`Name {Surname}` → `{Surname}, N.`| ([A-Z])[a-z]*?\s(\{[A-Z].+?\}) | $2, $1. |

</div>

## Style guides

Included herein are the style guides I have followed during the course of writing my thesis. Custom styles (`my*.sty files`) have been included to both simplify the preamble (located in `Thesis.tex`) and to create a more homogeneous styling throughout when dealing with the relevant packages contained in the style files.

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

### Figures

Figures are located in their relevant chapter (`chapter_*/figures/`) and have the chapter number, $i$, prepended to their name (`<i>_<name>.[pdf|svg]`).

The figures included in the document are `pdf`'s, but it is useful to save a copy of self-generated figures as `svg`'s for when edits to the figure will naturally arise. See 'Custom Figures' for further constraints on generated figures.

To use the figures in the Latex document, use:

```Latex
\begin{figure}[t]
    \centering
    \includegraphics[width = 1.0\textwidth]{'<i>_<name>.[pdf|png]'}
    \caption{Include a suitable caption here. Figure (if cited: 'adapted from', if own: 'created using') 'source'.(if link: \protect\footnotemark)}
    \label{fig:'suitable_label'}
\end{figure}
\footnotetext{\protect\url{(link)}}
```

#### Custom Figures

Figures created by myself are (generally) made using Inkscape. To keep line widths / text size / etc. consistent the following document properties are used:

* Document properties
  * ~10 cm x ? cm (depends on figure aspect ratio)
  * Before saving, use `resize to content`
  * scale = 0.1

* Grid properties
  * X_s, Y_s = 1 mm
  * Major Grid every 5

* Fill properties
  * Lightness = 66
  * (I.E. 0, 0, 66, 100)

* Font properties
  * name = cmr10
  * weight = normal
  * size = 16 px

* Stroke properties
  * width = 1 px

Figures are first saved as an `svg` before being exported as either a `png` or `pdf` to 'play well' with the Latex `\includegraphics[]{}` command.

### Headings

Headings use `Title Case`. Generally, labels are only included when necessary and are not compulsory when creating a new section, etc.

```Latex
% Note case is `Title Case`
\chapter{Chapter Title}
\section{Section Title} \label{sec:sec_title}
\dots
```

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

### Tables

Tables can be generated using a [Table Generator](https://www.tablesgenerator.com/). Tables are located in their relevant chapter (`chapter_*/tables/`) and have the chapter number, $i$, prepended to their name (`<i>_<name>.tex`). The contents of the file are structured similar to:

```Latex
\begin{table}[t]
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
\input{chapter_<i>/tables/'table_name'}
```

## Useful external References

* Glossaries (minor to-do's): <https://www.overleaf.com/learn/latex/Glossaries>
  * Useful glossary and acronym simultaneous addition: <https://tex.stackexchange.com/questions/8946/how-to-combine-acronym-and-glossary>
  * Glossary style <https://www.dickimaw-books.com/gallery/glossaries-styles/>
* Latex docs: <https://en.wikibooks.org/wiki/LaTeX>
* GitHub `.cff` file references: <https://citation-file-format.github.io/>

See 'preamble' of `references.bib` for further useful links relevant to specific chapters of thesis.
