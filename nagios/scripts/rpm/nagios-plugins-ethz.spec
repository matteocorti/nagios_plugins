%define version 1.1
%define release 1
%define name    nagios-plugins-ethz

Summary:   An empty package to force the installation of all the ETHZ Nagios plugins
Name:      %{name}
Version:   %{version}
Release:   %{release}
License:   GPL
Packager:  Matteo Corti <matteo.corti@id.ethz.ch>
Group:     Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Source:    http://www.id.ethz.ch/people/allid_list/corti/%{name}-%{version}.tar.gz
BuildArch: noarch

Requires: check_topology
Requires: check_tcptraffic
Requires: check_cpu
Requires: check_dir
Requires: check_diskio
Requires: check_updates
Requires: check_connections
Requires: check_afs_vol
Requires: check_afs_offline_volumes
Requires: nagios-plugins-various
Requires: check_lm_sensors

%description
An empty package to force the installation of all the ETHZ Nagios plugins

%prep
%setup -q

%build

%install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0644)
%doc AUTHORS ChangeLog NEWS README TODO COPYING VERSION

%changelog
* Fri Jun 15 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.1-1
- +check_lm_sensors

* Fri Apr 27 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0-1
- +nagios-plugins-various

* Wed Apr 25 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0-1
- Initial release
