%define version 1.0
%define release 0
%define name    nagios-plugins-various
%define _prefix /usr/lib/nagios/plugins/contrib

Summary:   A collection of various nagios plugins
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
A collection of various nagios plugins

check_afsspace
check_bos
check_cpu.pl
check_mailq
check_mem
check_rxdebug
check_udebu

%prep
%setup -q

%build

%install
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

%changelog
* Wed Apr 27 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0-1
- Initial release
