%define		realname	MathReader
Summary:	Mathematica Notebook Reader
Summary(pl.UTF-8):   Przeglądarka plików z programu Mathematica
Name:		MathReader4
Version:	4.2.1
Release:	1
License:	almost free, distributable
# from http://www.wolfram.com/products/mathreader/download.cgi
Source0:	%{realname}-%{version}-Linux-PPC.tar.gz
# Source0-md5:	9743cf3c81d3f83661034ae2cf5b6e78
Source1:	%{realname}.desktop
Group:		Applications/Math
URL:		http://www.wolfram.com/products/mathreader/
ExclusiveArch:	ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MathReader is a viewer for notebook documents created with
Mathematica, the world's only fully integrated technical computing
system. MathReader lets you display and print Mathematica notebooks,
animate graphics, play sounds, and copy information from notebooks to
other documents. MathReader can be used by most web browsers as a
helper application for viewing notebook documents.

%description -l pl.UTF-8
MathReader jest przeglądarką dla dokumentów utworzonych w programie
Mathematica, jedynym w świecie w pełni zintegrowanym systemie
technicznych obliczeń. MathReader pozwala wyświetlać i drukować
notatki, odtwarzać animacje, odgrywać dźwięki i kopiować informacje z
notatek programu Mathematica do innych dokumentów. MathReader może być
też używany przez większość przeglądarek WWW jako aplikacja pomocnicza
do przeglądania dokumentów.

%prep
%setup -q -n %{realname}-%{version}-Linux-PPC

%install
rm -rf $RPM_BUILD_ROOT
PAGER=/bin/cat
export PAGER

(
cat <<EOF
a
$RPM_BUILD_ROOT%{_libdir}
y
$RPM_BUILD_ROOT%{_bindir}
EOF
) | \
sh MathReaderInstaller

install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}
ln -sf %{_libdir}/%{realname}/Executables/{MathReader,mathreader} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Files/SystemFiles/Installation/TextResources/English/LicenseAgreement.txt
%attr(755,root,root) %{_bindir}/%{realname}
%dir %{_libdir}/%{realname}
%attr(755,root,root) %{_libdir}/%{realname}/Executables
%{_libdir}/%{realname}/Configuration
%{_libdir}/%{realname}/Documentation
%dir %{_libdir}/%{realname}/SystemFiles
%{_libdir}/%{realname}/SystemFiles/CharacterEncodings
%dir %{_libdir}/%{realname}/SystemFiles/FrontEnd
%dir %{_libdir}/%{realname}/SystemFiles/FrontEnd/Binaries
%ifarch ppc
%attr(755,root,root) %{_libdir}/%{realname}/SystemFiles/FrontEnd/Binaries/Linux-PPC
%endif
%{_libdir}/%{realname}/SystemFiles/FrontEnd/StyleSheets
%{_libdir}/%{realname}/SystemFiles/FrontEnd/SystemResources
%{_libdir}/%{realname}/SystemFiles/FrontEnd/TextResources
%{_libdir}/%{realname}/SystemFiles/Fonts
%{_libdir}/%{realname}/SystemFiles/SpellingDictionaries
%{_desktopdir}/%{realname}.desktop
