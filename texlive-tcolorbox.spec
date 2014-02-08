# revision 26072
# category Package
# catalog-ctan /macros/latex/contrib/tcolorbox
# catalog-date 2012-04-20 13:22:20 +0200
# catalog-license lppl1.3
# catalog-version 1.30
Name:		texlive-tcolorbox
Epoch:		1
Version:	1.30
Release:	2
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
%{_texmfdistdir}/tex/latex/tcolorbox/tcbdocumentation.code.tex
%{_texmfdistdir}/tex/latex/tcolorbox/tcblistings.code.tex
%{_texmfdistdir}/tex/latex/tcolorbox/tcbskins.code.tex
%{_texmfdistdir}/tex/latex/tcolorbox/tcbtheorems.code.tex
%{_texmfdistdir}/tex/latex/tcolorbox/tcolorbox.sty
%doc %{_texmfdistdir}/doc/latex/tcolorbox/CHANGES
%doc %{_texmfdistdir}/doc/latex/tcolorbox/README
%doc %{_texmfdistdir}/doc/latex/tcolorbox/README.TEXLIVE
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox-example.pdf
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox-example.tex
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox.pdf
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:1.30-1
+ Revision: 805101
- Update to latest release.

* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:1.20-1
+ Revision: 787793
- Update to latest release.

* Fri Mar 09 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1:1.10-2
+ Revision: 783481
- rebuild without scriptlet dependencies

* Wed Mar 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:1.10-1
+ Revision: 783078
- Update to latest release.

* Thu Feb 23 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:1.02-1
+ Revision: 779667
- Update to latest release.

* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:1.01-1
+ Revision: 770284
- Update to latest upstream package

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111217-2
+ Revision: 756546
- Rebuild to reduce used resources

* Sat Dec 17 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111217-1
+ Revision: 743321
- texlive-tcolorbox
- texlive-tcolorbox

