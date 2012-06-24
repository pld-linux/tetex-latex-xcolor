
%define short_name xcolor
%define	texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

Summary:	Allows for access to color tints, shades, tones etc
Summary(pl):	Pozwala na dost�p do odcieni, gradient�w itp.
Name:		tetex-latex-xcolor
Version:	2.00
Release:	1
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
BuildRequires:	tetex-latex-carlisle
BuildRequires:	tetex-tex-misc
BuildRequires:	tetex-tex-pstricks
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
`xcolor' provides easy driver-independent access to several kinds of
color tints, shades, tones, and mixes of arbitrary colors. It allows to
select a document-wide target color model and offers tools for automatic
color schemes, conversion between eight color models, and alternating
table row colors.

%description -l pl
`xcolor' dostarcza �atwego, niezale�nego od urz�dzenia dost�pu do wielu
rodzai cieniowania, ton�w i po��cze� dowolnych kolor�w. Pozwala na wyb�r
modelu koloru dla ca�ego dokumentu i oferuje narz�dzia dla schemat�w
kolor�w, konwersji mi�dzy o�mioma modelami kolor�w oraz naprzemiennych
kolor�w w tabelach.

%package examples
Summary:	Example files for the LaTeX xcolor package
Summary(pl):	Pliki przyk�adowe pakietu xcolor dla LaTeX-a
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}-%{release}

%description examples
Example files for the LaTeX xcolor package.

%description -l pl examples
Pliki przyk�adowe pakietu xcolor dla LaTeXa.

%prep
%setup -q -n %{short_name}
cp %{SOURCE1} .

%build
latex xcolor.ins

pdflatex xcolor1.tex
latex xcolor2.tex
dvipdf xcolor2.dvi
pdflatex xcolor3.tex
pdflatex xcolor.dtx
pdflatex xcolor.dtx

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
