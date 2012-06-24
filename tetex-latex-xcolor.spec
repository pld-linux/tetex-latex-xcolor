
%define short_name xcolor
%define	texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

Summary:	Allows for access to color tints, shades, tones etc
Summary(pl):	Pozwala na dost�p do odcieni, gradient�w itp.
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
`xcolor' dostarcza �atwego, niezale�nego od urz�dzenia dost�pu do wielu
rodzai cieniowania, ton�w i po��cze� dowolnych kolor�w. Pozwala na wyb�r
modelu koloru dla ca�ego dokumentu i oferuje narz�dzia dla schemat�w
kolor�w, konwersji mi�dzy o�mioma modelami kolor�w oraz naprzemiennych
kolor�w w tabelach.

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
