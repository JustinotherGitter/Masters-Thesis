# Thesis overview document

This file stands to track any final edits needed before the submission of the thesis, any minor improvements that may be made at a later date, any styles and style preferences to keep the file/document structure neat and logical, as well as any useful external references.

## Final `TODOs`

* Change \today to MONTH, YEAR at final submission [Thesis.tex:197]
* Ask for read through from friends to ensure no spelling/grammar errors

## Minor `TODOs`

* Update tables `\input{}` to use relative pathing
* Use the `minted` package instead of the `listings` `STOPS_docs` style workaround
* \$O\$- and \$E\$-beam(s)
* Unify usage of exposure / frame / extension and add to glossary (see references)

## Style guides

Included herein are the style guides I have followed during the course of writing my thesis. Custom styles (`my*.sty files`) have been included to both simplify the preamble (located in `Thesis.tex`) and to create a more homogeneous styling throughout when dealing with the relevant packages contained in the style files.

### Equations style guide

Equations are written in-text and are a part of sentences unless otherwise indicated. To this end, there is no new line before `\begin` or after `\end` (unless the sentence ends with the equation and the equation is punctuated) and multiple equations in a single environment are properly punctuated.

```Latex
% Align center
\begin{equation}
    'equation1' \,,\quad 'equation2'
\end{equation}

% Align center, ignore end text
\begin{equation}
    'equation1' \,,\rlap{\quad text\,,}
\end{equation}
```

The equation can either be a single- or multi-line equation:

```Latex
\begin{equation}
    R = \frac{\lambda}{FWHM}\,,\label{eq:resolving_power}
\end{equation}
```

or a collection of equations:

```Latex
\begin{equation}
    \begin{gathered}
        T_{0}(x) = 1\,,\\
        T_{1}(x) = x\,,\rlap{\quad and}\\
        T_{n}(x) = 2 x T_{n - 1}(x) - T_{n - 2}(x)\,,\rlap{\quad for $n > 1$\,,}
    \end{gathered} \label{eq:chebypoly}
\end{equation}
```

See references (Wikibooks) for more configurations of equations.

### Figures style guide

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

### Table style guide

Tables can be generated using a [Table Generator](https://www.tablesgenerator.com/). Tables are located in their relevant chapter (`chapter_*/tables/`) and have the chapter number, $i$, prepended to their name (`<i>_<name>.tex`). The contents of the file are structured similar to:

```Latex
\begin{table}[t]
    \begin{tabular}{c(* the amount of colums)}
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

* Markdown (for this document): <https://www.markdownguide.org/basic-syntax/>
* Glossaries ( minor to-do's): <https://www.overleaf.com/learn/latex/Glossaries>
* Latex docs: <https://en.wikibooks.org/wiki/LaTeX>

See 'preamble' of `references.bib` for further useful links relevant to specific chapters.
