Name:		texlive-translation-moreverb-de
Version:	23957
Release:	1
Summary:	German version of moreverb
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/moreverb/de
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-moreverb-de.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-moreverb-de.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is a "translation" of the moreverb documentation.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/translation-moreverb-de/filecontens-de.ins.txt
%doc %{_texmfdistdir}/doc/latex/translation-moreverb-de/moreverb-de.dtx.pdf
%doc %{_texmfdistdir}/doc/latex/translation-moreverb-de/moreverb-de.dtx.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
