# Figures style guide

To use figures in the Latex document, use:

```Latex
\begin{figure}[t]
    \centering
    \includegraphics[width = 1.0\textwidth]{figures/'figure_name'.png}
    \caption{A suitable caption goes here. (if cited figure) Figure adapted from 'source'(if link)\protect\footnotemark}
    \label{fig:'suitable_label'}
\end{figure}
\footnotetext{\protect\url{(link)}}
```

## Custom Figures

Figures created by myself are (generally) made using Inkscape. To keep line widths / text size / etc. consistent the following document properties are used:

- Document properties
  - ~10 cm x ? cm (depending on figure orientation)
  - Before saving, use `resize to content`
  - scale = 0.1

- Grid properties
  - X_s, Y_s = 1 mm
  - Major Grid every 5

- Fill properties
  - Lightness = 66 (I.E. 0, 0, 66, 100)

- Font properties
  - name = cmr10
  - weight = normal
  - size = 16 px

- Stroke properties
  - width = 1 px

Figures are first saved as an svg file before being exported as a png file to 'play well' with the Latex `\includegraphics[]{}` command.


## Cited / Adapted Figures