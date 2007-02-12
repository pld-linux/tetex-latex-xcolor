
%define short_name xcolor
%define	texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

Summary:	Allows for access to color tints, shades, tones etc
Summary(pl.UTF-8):   Pozwala na dostęp do odcieni, gradientów itp.
Name:		tetex-latex-xcolor
Version:	2.00
Release:	2
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
Source0:	http://dl.sourceforge.net/latex-beamer/%{short_name}-%{version}.tar.gz
# Source0-md5:	f8960a11271fa9d7bfa352966916553f
Source1:	http://www.ctan.org/tex-archive/macros/latex/contrib/misc/chngpage.sty
Requires:	tetex-latex
Requires:	tetex-latex-carlisle
Requires(post,postun):	/usr/bin/texhash
BuildRequires:	tetex-dvips
BuildRequires:	tetex-format-pdflatex
BuildRequires:	tetex-format-latex
BuildRequires:	tetex-latex-ams
BuildRequires:	tetex-latex-carlisle
BuildRequires:	tetex-metafont
BuildRequires:	tetex-tex-misc
BuildRequires:	tetex-tex-pstricks
BuildRequires:	tetex-makeindex
# for dvipdf
BuildRequires:	ghostscript
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
`xcolor' provides easy driver-independent access to several kinds of
color tints, shades, tones, and mixes of arbitrary colors. It allows to
select a document-wide target color model and offers tools for automatic
color schemes, conversion between eight color models, and alternating
table row colors.

%description -l pl.UTF-8
`xcolor' dostarcza łatwego, niezależnego od urządzenia dostępu do wielu
rodzai cieniowania, tonów i połączeń dowolnych kolorów. Pozwala na wybór
modelu koloru dla całego dokumentu i oferuje narzędzia dla schematów
kolorów, konwersji między ośmioma modelami kolorów oraz naprzemiennych
kolorów w tabelach.

%package examples
Summary:	Example files for the LaTeX xcolor package
Summary(pl.UTF-8):   Pliki przykładowe pakietu xcolor dla LaTeX-a
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}-%{release}

%description examples
Example files for the LaTeX xcolor package.

%description examples -l pl.UTF-8
Pliki przykładowe pakietu xcolor dla LaTeXa.

%prep
%setup -q -n %{short_name}
cp %{SOURCE1} .

%build
latex xcolor.ins

latex xcolor.dtx
latex xcolor.dtx
makeindex -s gind.ist xcolor.idx
latex xcolor.dtx
latex xcolor.dtx
dvipdf xcolor.dvi

# Missing BR (?):
# Font TS1/cmss/m/n/8=tcss0800 at 8.0pt not loadable: Metric (TFM) file not found.
# latex xcolor1.tex
# dvipdf xcolor1.dvi

latex xcolor2.tex
dvipdf xcolor2.dvi

latex xcolor3.tex
dvipdf xcolor3.dvi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/texmf/tex/latex/%{short_name},%{_examplesdir}/%{name}-%{version}}

install xcolor.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
install xcolor[123].{pdf,tex} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc xcolor.pdf
%{_datadir}/texmf/tex/latex/%{short_name}

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
