%define version 1.0.0
%define release 1
%define name    check_free_mem
%define _prefix /usr/lib/nagios/plugins/contrib

Summary:   Nagios plugin that checks the amount of free physical memory
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
check_free_mem is a Nagios plugin that checks the amount of free physical memory

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
* Thu Mar 20 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.11.3-0
- ePN compatibility

* Sun Jan 13 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.11.0-0
- updated to 0.11.0, --free can be used to specify the path of 'free'

* Sun Jan 13 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.10.0-0
- updated to 0.10.0 with --swap to monitor swap space

* Wed Jan  9 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.0-0
- Initial revision

