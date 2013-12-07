# revision 31674
# category Package
# catalog-ctan /macros/latex/contrib/tcolorbox
# catalog-date 2013-09-16 15:30:54 +0200
# catalog-license lppl1.3
# catalog-version 2.51
Name:		texlive-tcolorbox
Epoch:		1
Version:	2.51
Release:	4
Summary:	Coloured boxes, for LaTeX examples and theorems, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tcolorbox
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tcolorbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tcolorbox.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides an environment for coloured and framed
text boxes with a heading line. Optionally, such a box can be
split in an upper and a lower part; thus the package may be
used for the setting of LaTeX examples where one part of the
box displays the source code and the other part shows the
output. Another common use case is the setting of theorems. The
package supports saving and reuse of source code and text
parts.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tcolorbox/tcbbreakable.code.tex
%{_texmfdistdir}/tex/latex/tcolorbox/tcbdocumentation.code.tex
%{_texmfdistdir}/tex/latex/tcolorbox/tcbfitting.code.tex
%{_texmfdistdir}/tex/latex/tcolorbox/tcbhooks.code.tex
%{_texmfdistdir}/tex/latex/tcolorbox/tcblistings.code.tex
%{_texmfdistdir}/tex/latex/tcolorbox/tcblistingscore.code.tex
%{_texmfdistdir}/tex/latex/tcolorbox/tcblistingsutf8.code.tex
%{_texmfdistdir}/tex/latex/tcolorbox/tcbminted.code.tex
%{_texmfdistdir}/tex/latex/tcolorbox/tcbskins.code.tex
%{_texmfdistdir}/tex/latex/tcolorbox/tcbtheorems.code.tex
%{_texmfdistdir}/tex/latex/tcolorbox/tcolorbox.sty
%doc %{_texmfdistdir}/doc/latex/tcolorbox/Basilica_5.png
%doc %{_texmfdistdir}/doc/latex/tcolorbox/CHANGES
%doc %{_texmfdistdir}/doc/latex/tcolorbox/README
%doc %{_texmfdistdir}/doc/latex/tcolorbox/lichtspiel.jpg
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox-example.pdf
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox-example.tex
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox.doc.abstract.tex
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox.doc.bib
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox.doc.breakable.tex
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox.doc.coremacros.tex
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox.doc.coreoptions.tex
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox.doc.documentation.tex
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox.doc.fitting.tex
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox.doc.hooks.tex
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox.doc.index.tex
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox.doc.initoptions.tex
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox.doc.intro.tex
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox.doc.listings.tex
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox.doc.references.tex
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox.doc.skins.tex
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox.doc.theorems.tex
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox.doc.verbatim.tex
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox.pdf
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
