Name:           elinks
Version:        0.12pre6
Release:        1
Summary:        ELinks is a program for browsing the web in text mode
Url:            http://elinks.or.cz/
Source0:        %{name}-%{version}.tar.bz2
License:        GPLv2
BuildRequires:  autoconf
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(mozjs185)

%description
ELinks is a program for browsing the web in text mode.

%package docs
Summary: Elinks documentation package

%description docs
Documentation for Elinks - a program for browsing the web in text mode.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
./autogen.sh
%configure --enable-256-colors
%make_build

%install
%make_install

%files
%defattr(-,root,root)
#%license COPYING
%{_bindir}/elinks

%files docs
%defattr(-,root,root)
%{_datadir}/man/man1/*
%{_datadir}/man/man5/*
%{_datadir}/locale/af/LC_MESSAGES/elinks.mo
%{_datadir}/locale/be/LC_MESSAGES/elinks.mo
%{_datadir}/locale/bg/LC_MESSAGES/elinks.mo
%{_datadir}/locale/ca/LC_MESSAGES/elinks.mo
%{_datadir}/locale/cs/LC_MESSAGES/elinks.mo
%{_datadir}/locale/da/LC_MESSAGES/elinks.mo
%{_datadir}/locale/de/LC_MESSAGES/elinks.mo
%{_datadir}/locale/el/LC_MESSAGES/elinks.mo
%{_datadir}/locale/es/LC_MESSAGES/elinks.mo
%{_datadir}/locale/et/LC_MESSAGES/elinks.mo
%{_datadir}/locale/fi/LC_MESSAGES/elinks.mo
%{_datadir}/locale/fr/LC_MESSAGES/elinks.mo
%{_datadir}/locale/gl/LC_MESSAGES/elinks.mo
%{_datadir}/locale/hr/LC_MESSAGES/elinks.mo
%{_datadir}/locale/hu/LC_MESSAGES/elinks.mo
%{_datadir}/locale/id/LC_MESSAGES/elinks.mo
%{_datadir}/locale/is/LC_MESSAGES/elinks.mo
%{_datadir}/locale/it/LC_MESSAGES/elinks.mo
%{_datadir}/locale/locale.alias
%{_datadir}/locale/lt/LC_MESSAGES/elinks.mo
%{_datadir}/locale/nb/LC_MESSAGES/elinks.mo
%{_datadir}/locale/nl/LC_MESSAGES/elinks.mo
%{_datadir}/locale/pl/LC_MESSAGES/elinks.mo
%{_datadir}/locale/pt/LC_MESSAGES/elinks.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/elinks.mo
%{_datadir}/locale/ro/LC_MESSAGES/elinks.mo
%{_datadir}/locale/ru/LC_MESSAGES/elinks.mo
%{_datadir}/locale/sk/LC_MESSAGES/elinks.mo
%{_datadir}/locale/sr/LC_MESSAGES/elinks.mo
%{_datadir}/locale/sv/LC_MESSAGES/elinks.mo
%{_datadir}/locale/tr/LC_MESSAGES/elinks.mo
%{_datadir}/locale/uk/LC_MESSAGES/elinks.mo

