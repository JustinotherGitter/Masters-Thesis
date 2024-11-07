%
% ociamthesis v2.2
% By Keith A. Gillow <gillow@maths.ox.ac.uk>
% Version 1.0 released 26/11/1997
% Modified by Justin Cooper <Justin.jb78@gmail.com>
% Version 1.1 released 06/11/2024
%-------------------------- identification ---------------------
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{thesis}[2010/11/22 v2.2 OCIAM thesis class]
%-------------------------- initial code -----------------------
%\def\logoversion{squarelogo}
%\DeclareOption{beltcrest}{\def\logoversion{beltcrest}}
%\DeclareOption{shieldcrest}{\def\logoversion{shieldcrest}}
%\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}
\ProcessOptions\relax

\LoadClass[a4paper,12pt]{book}
% As an alternative to the above could use next line for twosided output
%\LoadClass[a4paper,twoside,openright]{report}

%\RequirePackage{graphicx} % needed for latest frontpage logo
%\RequirePackage{ifthen}   % needed for option parsing for logo

\raggedbottom

% Define the default submitted text
\newcommand{\submittedtext}{%
    {Submitted in partial fulfillment of the requirements for the degree}
}

%
% MARK: DECLARATIONS
%
% These macros are used to declare arguments needed for the
% construction of the title page and other preamble.

% The year and term the thesis is submitted 
\def\degreedate#1{\gdef\@degreedate{#1}}
% The current highest degree
\def\Cdegree#1{\gdef\@Cdegree{#1}}
% The full (unabbreviated) name of the degree
\def\Sdegree#1{\gdef\@Sdegree{#1}}
% The name of the University
\def\university#1{\gdef\@university{#1}}
\def\faculty#1{\gdef\@faculty{#1}}
\def\department#1{\gdef\@department{#1}}
\def\country#1{\gdef\@country{#1}}
\def\supervisor#1{\gdef\@supervisor{#1}}
\def\cosupervisor#1{\gdef\@cosupervisor{#1}}
%
% Define text area of page and margin offsets
%
%\setlength{\topmargin}{0.0in}
%\setlength{\oddsidemargin}{0.33in}
%\setlength{\evensidemargin}{-0.08in}
%\setlength{\textheight}{9.0in}
%\setlength{\textwidth}{6.0in}

%
% MARK: Environments
%

% This macro define an environment for front matter that is always 
% single column even in a double-column document.

\newenvironment{alwayssingle}{%
    \@restonecolfalse
    \if@twocolumn\@restonecoltrue\onecolumn
    %\else\if@openright\cleardoublepage\else\clearpage\fi
    \else\if@openright\newpage\else\clearpage\fi
    \fi
}{%
    \if@restonecol\twocolumn
    \else\newpage\thispagestyle{empty}\fi
}

% MARK: Title page layout
\renewcommand{\maketitle}{%
    \begin{alwayssingle}
        %\renewcommand{\footnotesize}{\small}
        \renewcommand{\footnoterule}{\relax}
        \thispagestyle{empty}
        \begin{center}
            {\LARGE {\@title} \par}
            {\vspace*{20mm}}
            {{\Large \@author} \par}
            {{\normalsize \@Cdegree} \par}
            \vspace*{20mm}
                {\normalsize {{\submittedtext} \par}
            \vspace*{1ex}
                {{\@Sdegree} \par}
            \vspace*{1ex}
                {{in the \@faculty} \par}
            \vspace*{1ex}
                {{\@department} \par}
            \vspace*{1ex}
                {{\@university} \par}
            \vspace*{1ex}
                {{\@country} \par}}
            {\vspace*{10mm}}
                {\footnotesize {\@degreedate \par}}
            {\vspace*{10mm}}
                {\normalsize {{Supervised by: \@supervisor, \@department} \par}}
        \end{center}
    
    %\let\thefootnote\relax\footnote{The financial assistance of the National Research Foundation (NRF) towards this research is hereby acknowledged. Opinions expressed and conclusions arrived at, are those of the author and are not necessarily to be attributed to the NRF.}
    
    \end{alwayssingle}
}

% MARK: DEDICATION
%
% The dedication environment makes sure the dedication gets its
% own page and is set out in verse format.

\newenvironment{dedication}{%
    \begin{alwayssingle} \thispagestyle{empty}
        %\begin{center}
        %    \vspace*{1.5cm}
        %    {\LARGE \bfseries Dedication}
        %\end{center}
        %\vspace{0.5cm}
        \begin{verse}
            \begin{center}
}{%
            \end{center}
        \end{verse}
    \end{alwayssingle}
}


% MARK: ACKNOWLEDGEMENTS
%
% The acknowledgements environment puts a large, bold, centered 
% "Acknowledgements" label at the top of the page. The acknowledgements
% themselves appear in a quote environment, i.e. tabbed in at both sides, and
% on its own page.

\newenvironment{acknowledgements}{%
    \begin{alwayssingle} \thispagestyle{empty}
        \begin{center}
            \vspace*{1.5cm}
            {\Large \bfseries Acknowledgements}
        \end{center}
        \vspace{0.5cm}
        \begin{quote} \scriptsize
}{%
        \end{quote}
    \end{alwayssingle}
}

% The acknowledgementslong environment puts a large, bold, centered 
% "Acknowledgements" label at the top of the page. The acknowledgement itself 
% does not appears in a quote environment so you can get more in.

\newenvironment{acknowledgementslong}{%
    \begin{alwayssingle} \thispagestyle{empty}
        \begin{center}
            \vspace*{1.5cm}
            {\Large \bfseries Acknowledgements}
        \end{center}
        \vspace{0.5cm}
}{%
    \end{alwayssingle}
}

% MARK: STATEMENT OF ORIGINALITY (AS SUGGESTED BY GSW)
%
% The originality environment puts a large, bold, centered 
% "Statement of originality" label at the top of the page. The statement 
% of originality itself appears in a quote environment, i.e. tabbed in at 
% both sides, and on its own page.

\newenvironment{originality}{%
    \begin{alwayssingle} \thispagestyle{empty}
        \begin{center}
            \vspace*{1.5cm}
            {\Large \bfseries Statement of Originality}
        \end{center}
        \vspace{0.5cm}
        \begin{quote}
}{%
        \end{quote}
    \end{alwayssingle}
}

% The originalitylong environment puts a large, bold, centered 
% "Statement of originality" label at the top of the page. The statement 
% of originality itself does not appears in a quote environment so you can 
% get more in.

\newenvironment{originalitylong}{%
    \begin{alwayssingle} \thispagestyle{empty}
    \begin{center}
        \vspace*{1.5cm}
        {\Large \bfseries Statement of Originality}
    \end{center}
    \vspace{0.5cm}
}{%
    \end{alwayssingle}
}


% MARK: ABSTRACT
%
% The abstract environment puts a large, bold, centered "Abstract" label at
% the top of the page. The abstract itself appears in a quote environment,
% i.e., tabbed in at both sides, and on its own page.

\newenvironment{abstract}{%
    \begin{alwayssingle} \thispagestyle{empty}
        \begin{center}
            \vspace*{1.5cm}
            {\Large \bfseries  Abstract}
        \end{center}
        \vspace{0.5cm}
        \begin{quote} \scriptsize
}{%
        \end{quote}
    \end{alwayssingle}
}

\newenvironment{opsomming}{%
    \begin{alwayssingle} \thispagestyle{empty}
        \begin{center}
            \vspace*{1.5cm}
            {\Large \bfseries  Opsomming}
        \end{center}
        \vspace{0.5cm}
        \begin{quote} \scriptsize
}{%
        \end{quote}
    \end{alwayssingle}
}

% The abstractlong environment puts a large, bold, centered "Abstract" label at
% the top of the page. The abstract itself does not appears in a quote
% environment so you can get more in.

\newenvironment{abstractlong}{%
    \begin{alwayssingle} \thispagestyle{empty}
        \begin{center}
            \vspace*{1.5cm}
            {\Large \bfseries  Abstract}
        \end{center}
        \vspace{0.5cm}
}{%
    \end{alwayssingle}
}

% The abstractseparate environment is for running of a page with the abstract
% on including title and author, etc., as required to be handed in separately

\newenvironment{abstractseparate}{%
    \begin{alwayssingle} \thispagestyle{empty}
        \vspace*{-1in}
        \begin{center}
            {\Large {\bfseries {\@title}} \par}
            {{\large \vspace*{1ex} \@author} \par}
            {\large \vspace*{1ex}
            {{\@college} \par}
            {University of Oxford \par}
            \vspace*{1ex}
            {{\it \submittedtext} \par}
            {\it {\@Cdegree} \par}
            \vspace*{2ex}
            {\@degreedate}}
        \end{center}
}{%
    \end{alwayssingle}
}

\newenvironment{abbreviations}{%
    \begin{alwayssingle} \thispagestyle{empty}
        \vspace*{1.5cm}
        {\Huge \bfseries  List of Acronyms}
        \vspace{0.5cm}
        \begin{quote}
}{%
        \end{quote}
    \end{alwayssingle}
}
