%define version 1.5
%define release 0
%define name    nagios-plugins-various
%define _prefix /usr/lib/nagios/plugins/contrib
%define _unpackaged_files_terminate_build 0 

Summary:   A collection of various nagios plugins
Name:      %{name}
Version:   %{version}
Release:   %{release}
License:   GPL
Packager:  Matteo Corti <matteo.corti@id.ethz.ch>
Group:     Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Source:    http://www.id.ethz.ch/people/allid_list/corti/%{name}-%{version}.tar.gz

Requires:  perl(Net::DHCP::Watch)

%description
A collection of various nagios plugins

check_cpu.pl
check_dhcp.pl
check_mailq
check_mem
check_open_files

%prep
%setup -q

%build

%install        
make DESTDIR=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0644)
%attr(0755, root, root) %{_prefix}/check_cpu.pl
%attr(4755, root, root) %{_prefix}/check_dhcp.pl
%attr(0755, root, root) %{_prefix}/check_mailq
%attr(0755, root, root) %{_prefix}/check_mem
%attr(0755, root, root) %{_prefix}/check_open_files.pl

%changelog
* Wed Nov 25 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 1.5-0
- removed AFS plugins

* Fri Dec  5 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 1.3-1
- removed check_procs

* Wed Jan 23 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 1.3-0
- added check_open_files

* Wed Jan 23 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 1.2-6
- added check_procs.rh5

* Mon Dec 17 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.2-1
- check_dhcp requires Net::DHCP::Watch

* Mon Dec 17 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.2-0
- added check_dhcp.pl

* Mon Dec 10 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.1-0
- added a patched version of check_procs (adds performance data)

* Wed Apr 27 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0-1
- Initial release
