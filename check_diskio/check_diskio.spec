%define version 3.0.3
%define release 0
%define name    check_diskio
%define _prefix /usr/lib/nagios/plugins/contrib

Summary:   Nagios plugin to monitor the amount of disk I/O
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
Nagios plugin to monitor the amount of disk I/O

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
* Tue Jun  9 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 3.0.3-0
- fix for HP Smart Array Cards

* Sun May 17 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 3.0.2-0
- update to 3.0.2 (UOM fix)

* Fri May 15 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 3.0.1-0
- embedded perl -> package variables

* Tue Jan 20 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 3.0.0-0
- multiple devices and LVM

* Sun Oct 26 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 2.2.1-0
- added dependency on Class::Accessor::Fast

* Thu Apr 10 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 2.2.0-0
- --device can be specified as a mount point

* Fri Mar 21 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 2.1.2-0
- fixed missing usage message

* Thu Mar 20 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 2.1.1-0
- ePN compatibility

* Thu Nov 22 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 2.1.0-0
- upgraded to 2.1.0

* Wed Oct 31 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 2.0.1-0
- upgraded to 2.0.1 (bug fix)

* Tue Oct 30 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 2.0.0-0
- upgraded to 2.0.0

* Mon Sep 24 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.4.0-0
- First RPM package
