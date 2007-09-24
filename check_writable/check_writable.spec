%define version 1.0.0
%define release 0
%define name    check_writable
%define _prefix /usr/lib/nagios/plugins/contrib

Summary:    Nagios plugin that checks if one or more directories are writable
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

%install
make DESTDIR=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0644)
%doc AUTHORS ChangeLog NEWS README INSTALL TODO COPYING VERSION
%attr(0755, root, root) %{_prefix}/check_writable

%changelog
* Mon Sep 24 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0.0-0
- first rpm package


