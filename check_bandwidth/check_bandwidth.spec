%define version 0.9.6
%define release 0
%define name    check_bandwidth
%define _prefix /usr/lib/nagios/plugins/contrib

Summary:   Nagios plugin that checks the available bandwidth
Name:      %{name}
Version:   %{version}
Release:   %{release}
License:   GPL
Packager:  Matteo Corti <matteo.corti@id.ethz.ch>
Group:     Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Source:    http://www.id.ethz.ch/people/allid_list/corti/%{name}-%{version}.tar.gz
BuildArch: noarch

Requires: perl
Requires: iperf

%description
Nagios plugin that checks the available bandwidth

%prep
%setup -q

%build
%__perl Makefile.PL  INSTALLSCRIPT=%{buildroot}%{_prefix} INSTALLSITEMAN3DIR=%{buildroot}/usr/share/man/man3
make

%install
make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0644)
%doc AUTHORS Changes NEWS README INSTALL TODO COPYING VERSION
%attr(0755, root, root) %{_prefix}/%{name}
%attr(0755, root, root) /usr/share/man/man3/%{name}.3pm.gz

%changelog
* Fri Mar 21 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.6-0
- fixed the usage message (wrong one)

* Fri Mar 21 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.5-0
- fixed missing usage

* Thu Mar 20 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.4-0
- ePN compatibility

* Wed Jan 23 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.3-0
- updated to 0.9.3 (option to swap up- and downstream)

* Tue Jan 22 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.2-0
- updated to 0.9.2 (options to specify local and remote ports)

* Fri Jan 18 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.0-0
- Initial revision

