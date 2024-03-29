Summary:	Small, light-weight app launcher with a simple XML-based configuration
Summary(pl.UTF-8):	Mały, lekki program do uruchamiania aplikacji z prostą konfiguracją w XML-u
Name:		acidlaunch
Version:	0.5
Release:	1
License:	LGPL v2.1
Group:		X11/Applications
Source0:	http://linuxgamers.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	7c90e429d5883b9f109a52e024597fab
Patch0:		%{name}-ac.patch
Patch1:		%{name}-gcc4.patch
Patch2:		%{name}-c++.patch
URL:		http://linuxgamers.net/infoPage.php?page=acidlaunch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel >= 0.9.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.0
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
acidlaunch is a small, light-weight app launcher with a simple
XML-based configuration syntax. It's written in C++ using gtk,
gdk-pixbuf and libxml2. It's great as a small, simple app launcher,
and it can optionally run in a withdrawn mode for embedding in the
blackbox slit.

%description -l pl.UTF-8
acidlaunch jest małym, lekkim programem do uruchamiania aplikacji z
konfiguracją o prostej składni, bazującą na XML-u. Jest napisany w C++
z użyciem gtk, gdk-pixbuf i libxml2. Jest wspaniały jako małe
narzędzie do uruchamiania aplikacji i może opcjonalnie uruchamiać w
trybie osadzenia w szczelinie blackboksa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/acidlaunch
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/default.png
%{_datadir}/%{name}/config.xml
%{_mandir}/man1/acidlaunch.1*
