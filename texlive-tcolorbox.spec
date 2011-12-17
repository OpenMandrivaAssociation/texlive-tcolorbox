# revision 24811
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-tcolorbox
Version:	20111217
Release:	1
Summary:	TeXLive tcolorbox package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tcolorbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tcolorbox.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive tcolorbox package.

%pre
    %{_sbindir}/texlive.post

%post
    %{_sbindir}/texlive.post

%preun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tcolorbox/tcolorbox.sty
%doc %{_texmfdistdir}/doc/latex/tcolorbox/CHANGES
%doc %{_texmfdistdir}/doc/latex/tcolorbox/README
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcblistings.code.tex
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcbtheorems.code.tex
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox-example.pdf
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox-example.tex
%doc %{_texmfdistdir}/doc/latex/tcolorbox/tcolorbox.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
