Summary:	Small, light-weight app launcher with a simple XML-based configuration
Summary(pl):	Ma³y, lekki program do uruchamiania aplikacji z prost± konfiguracj± w XML
Name:		acidlaunch
Version:	0.5
Release:	1
License:	GPL v2.1
Group:		X11/Applications
Source0:	http://linuxgamers.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	7c90e429d5883b9f109a52e024597fab
URL:		http://linuxgamers.net/infoPage.php?page=acidlaunchh
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gdk-pixbuf-devel > 0.9.0
BuildRequires:	gtk+-devel
BuildRequires:	libxml2-devel > 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
acidlaunch is a small, light-weight app launcher with a simple
XML-based configuration syntax. It's written in C++ using gtk,
gdk-pixbuf and libxml2. It's great as a small, simple app launcher,
and it can optionally run in a withdrawn mode for embedding in the
blackbox slit.

%description -l pl
acidlaunch jest ma³ym, lekkim programem do uruchamiania aplikacji z
konfiguracj± o prostej sk³adni, bazuj±c± na XML. Jest napisany w C++ z
u¿yciem gtk, gdk-pixbuf i libxml2. Jest wspania³y jako ma³e narzêdzie
do uruchamiania aplikacji i mo¿e opcjonalnie uruchamiaæ w trybie
osadzenia w szczelinie blackboksa.

%prep
%setup  -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man3}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/acidlaunch
%attr(644,root,root) %{_datadir}/%{name}/default.png
%attr(644,root,root) %{_datadir}/%{name}/config.xml
%{_mandir}/man1/*.1*
