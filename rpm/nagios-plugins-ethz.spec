%define version 1.6
%define release 0
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

Requires: check_afs_offline_volumes
Requires: check_afs_vol
Requires: check_connections
Requires: check_cpu
Requires: check_dir
Requires: check_diskio
Requires: check_free_mem
Requires: check_lm_sensors
Requires: check_nagios_latency
Requires: check_ssl_cert
Requires: check_tcptraffic
Requires: check_topology
Requires: check_updates
Requires: check_vpp_logs
Requires: check_writable
Requires: nagios-plugins-various

%description
An empty package to force the installation of all the ETHZ Nagios plugins

%prep
%setup -q

%build

%install
# rpmbuild requires an installation root even if we don't install anything
mkdir %{_tmppath}/%{name}-%{version}-root

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0644)
%doc AUTHORS ChangeLog NEWS README TODO COPYING VERSION

%changelog
* Wed Jan  9 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 1.6-0
- added a dependency for check_free_mem

* Mon Dec  3 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.5-0
- added check_vpp_logs

* Fri Aug 10 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.3-1
- +check_ssl_cert

* Thu Jul 26 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.2-0
- +check_writable

* Fri Jun 15 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.1-1
- +check_lm_sensors

* Fri Apr 27 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0-1
- +nagios-plugins-various

* Wed Apr 25 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0-1
- Initial release
