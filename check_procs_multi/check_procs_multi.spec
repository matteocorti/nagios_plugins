%define version 1.0.1
%define release 0
%define name    check_procs_multi
%define _prefix /usr/lib/nagios/plugins/contrib

Summary:   Nagios plugin similar to check_procs able to check several processes at once.
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

%description
check_procs_multi is a Nagios plugin similar to check_procs able to
check several processes at once.

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
* Mon Jun 15 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0.1-0
- removed dep on Net::DNS

* Mon Jun  9 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0.0-0
- grepping in perl

* Mon May 26 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.5-0
- fixed a bug when command name != proc name

* Fri Mar 21 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.4-0
- fixed the missing usage message

* Thu Mar 20 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.3-0
- ePN compatibility

* Tue Feb 12 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.2-0
- fixed a bug in the sanity checks

* Tue Feb 12 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.1-0
- version 0.9.1 (default min 1)

* Mon Feb 11 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.0-0
- Initial release
