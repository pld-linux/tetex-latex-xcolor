
%define short_name xcolor
%define	texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

Summary:	Allows for access to color tints, shades, tones etc
Summary(pl):	Pozwala na dostêp do odcieni, gradientów itp.
Name:		tetex-latex-xcolor
Version:	1.10
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
Source0:	http://dl.sourceforge.net/latex-beamer/%{short_name}-%{version}.tar.gz
# Source0-md5:	1ad338e29dcf62a30df3d770833a8b43
Requires:	tetex-latex
Requires:	tetex-latex-carlisle
Requires(post,postun):	/usr/bin/texhash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
`xcolor' provides easy driver-independent access to several kinds of
color tints, shades, tones, and mixes of arbitrary colors. It allows to
select a document-wide target color model and offers tools for automatic
color schemes, conversion between eight color models, and alternating
table row colors.

%description -l pl
`xcolor' dostarcza ³atwego, niezale¿nego od urz±dzenia dostêpu do wielu
rodzai cieniowania, tonów i po³±czeñ dowolnych kolorów. Pozwala na wybór
modelu koloru dla ca³ego dokumentu i oferuje narzêdzia dla schematów
kolorów, konwersji miêdzy o¶mioma modelami kolorów oraz naprzemiennych
kolorów w tabelach.

%prep
%setup -q -n %{short_name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

install *.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc *.pdf
%{_datadir}/texmf/tex/latex/%{short_name}
