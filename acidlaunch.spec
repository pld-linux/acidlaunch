Summary:	Small, light-weight app launcher with a simple XML-based configuration
Name:		acidlaunch
Version:	0.5
Release:	1
License:	GPL v2.1
Group:		X11/Applications
Source0:	http://linuxgamers.net/download/%{name}-%{version}.tar.gz
URL:		http://linuxgamers.net/infoPage.php?page=acidlaunchh
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gtk+-devel
BuildRequires:	gdk-pixbuf-devel > 0.9.0
BuildRequires:	libxml2-devel > 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
acidlaunch is a small, light-weight app launcher with a simple
XML-based configuration syntax. It's written in C++ using gtk,
gdk-pixbuf and libxml2. It's great as a small, simple app launcher,
and it can optionally run in a withdrawn mode for embedding in the
blackbox slit.

%prep
%setup  -q

%build
rm -f missing
%{__aclocal}
autoconf
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
