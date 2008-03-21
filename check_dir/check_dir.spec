%define version 2.1.5
%define release 0
%define name    check_dir
%define _prefix /usr/lib/nagios/plugins/contrib

Summary:   Nagios plugin to monitor the number of files in one or more directories.
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
Nagios plugin to monitor the number of files in one or more directories.

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
* Fri Mar 21 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 2.1.5-0
- fixed the missing usage message

* Thu Mar 20 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 2.1.4-0
- added -d (which was automatic w/o the option bundling introduced in 2.1.3)

* Thu Mar 20 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 2.1.3-0
- short command line options can be bundled and are case sensitive

* Thu Mar 20 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 2.1.2-0
- ePN compatibility

* Tue Mar 18 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 2.1.1-0
- added more sanity checks

* Tue Mar 18 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 2.1.0-0
- accepts ranges for -c and -w

* Mon Sep 24 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.2-0
- first RPM package

# /usr/share/man/man1/check_dir.1
