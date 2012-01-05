# revision 23957
# category Package
# catalog-ctan /info/translations/moreverb/de
# catalog-date 2011-09-14 17:59:09 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-translation-moreverb-de
Version:	20110914
Release:	2
Summary:	German version of moreverb
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/moreverb/de
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-moreverb-de.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-moreverb-de.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
