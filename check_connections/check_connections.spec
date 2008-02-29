%define version 2.0.0
%define release 0
%define name    check_connections
%define _prefix /usr/lib/nagios/plugins/contrib

Summary:   Nagios plugin to monitor the number of network connections
Name:      %{name}
Version:   %{version}
Release:   %{release}
License:   GPL
Packager:  Matteo Corti <matteo.corti@id.ethz.ch>
Group:     Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Source:    http://www.id.ethz.ch/people/allid_list/corti/%{name}-%{version}.tar.gz
BuildArch: noarch

%description
Nagios plugin to monitor the number of network connections

%prep
%setup -q

%build

%install
make DESTDIR=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0644)
%doc AUTHORS ChangeLog NEWS README INSTALL TODO COPYING VERSION
%attr(0755, root, root) %{_prefix}/check_connections

%changelog
* Mon Sep 24 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.2.0-0
- First RPM package

