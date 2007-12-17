%define version 1.2
%define release 2
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
BuildArch: i386

Requires:  perl(Net::DHCP::Watch)

%description
A collection of various nagios plugins

check_afsspace
check_bos
check_cpu.pl
check_dhcp.pl
check_mailq
check_mem
check_rxdebug
check_udebu
check_procs (patched to generate performance data)

%prep
%setup -q

%build

%install
if grep -q 'Red Hat Enterprise Linux AS release 4' /etc/issue ; then
        cp check_procs.rh4 check_procs
elif grep -q 'Fedora release 8' /etc/issue ; then
        cp check_procs.f8 check_procs
fi
        
make DESTDIR=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0644)
%attr(0755, root, root) %{_prefix}/check_afsspace
%attr(0755, root, root) %{_prefix}/check_bos
%attr(0755, root, root) %{_prefix}/check_cpu.pl
%attr(0755, root, root) %{_prefix}/check_mailq
%attr(0755, root, root) %{_prefix}/check_mem
%attr(0755, root, root) %{_prefix}/check_rxdebug
%attr(0755, root, root) %{_prefix}/check_udebug
%attr(0755, root, root) %{_prefix}/check_procs

%changelog
* Mon Dec 17 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.2-1
- check_dhcp requires Net::DHCP::Watch

* Mon Dec 17 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.2-0
- added check_dhcp.pl

* Mon Dec 10 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.1-0
- added a patched version of check_procs (adds performance data)

* Wed Apr 27 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0-1
- Initial release
