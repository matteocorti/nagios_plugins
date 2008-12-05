%define version 1.0.3
%define release 1
%define name    check_cpu
%define _prefix /usr/lib/nagios/plugins/contrib

Summary:   Nagios plugin to monitor the CPU usage on Linux systems
Name:      %{name}
Version:   %{version}
Release:   %{release}
License:   GPL
Packager:  Matteo Corti <matteo.corti@id.ethz.ch>
Group:     Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Source:    http://www.id.ethz.ch/people/allid_list/corti/%{name}-%{version}.tar.gz
BuildArch: noarch

Requires: hddtemp
Requires: perl

%description
Nagios plugin to monitor the CPU usage on Linux systems

%prep
%setup -q

%build
%__perl Makefile.PL  INSTALLSCRIPT=%{buildroot}%{_prefix} INSTALLSITEMAN3DIR=%{buildroot}/usr/share/man/man3 INSTALLSITESCRIPT=%{buildroot}%{_prefix}
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
* Fri Mar 21 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0.3-0
- fixed the missing usage messages

* Thu Mar 20 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0.2-0
- ePN compatibility

* Wed Oct 31 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 2.0.0-0
- Initial RPM package
