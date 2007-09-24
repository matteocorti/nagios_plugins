%define version 1.1.0
%define release 0
%define name    check_tcptraffic
%define _prefix /usr/lib/nagios/plugins/contrib

Summary:   A Nagios plugin to monitor the amount of TCP traffic
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
check_tcptraffic is a Nagios plugin to monitor the amount of TCP traffic

Usage check_tcptraffic [-v] [-r] -c crit -w warn -i iface

  -c crit      critical
  -w warn      warning
  -i iface     network interface
  -r           initialize
  -v           verbose

check_tcptraffic uses the /proc/net/dev Linux entry to compute the
amount of transferred bytes from the last plugin execution (temporary
data is stored in the /tmp/check_tcptraffic-iface file)

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
%attr(0755, root, root) %{_prefix}/check_tcptraffic

%changelog
* Wed Apr 25 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0-1
- Initial release
