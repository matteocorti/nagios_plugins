%define version 2.0.1
%define release 0
%define name    check_writable
%define _prefix /usr/lib/nagios/plugins/contrib

Summary:   Nagios plugin that checks if one or more directories are writable
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
check_writable is a Nagios plugin that checks if one or more
directories are writable by:

- checking that the supplied directory is indeed a directory
- checking if the the filesystem permissions are OK
- creating a temporary file
- writing random data to the temporary file (and reading it back)

It return a critical status if one of the tests fails


%prep
%setup -q

%build
%__perl Makefile.PL  INSTALLSCRIPT=%{buildroot}%{_prefix} INSTALLSITEMAN1DIR=%{buildroot}/usr/share/man/man1
make

%install
make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0644)
%doc AUTHORS Changes NEWS README INSTALL TODO COPYING VERSION
%attr(0755, root, root) %{_prefix}/%{name}
%attr(0755, root, root) /usr/share/man/man1/%{name}.1.gz

%changelog
* Tue Nov 13 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 2.0.1-0
- updated to 2.0.1

* Wed Oct 31 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 2.0.0-0
- updated to 2.0.0

* Mon Sep 24 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0.0-0
- first rpm package
