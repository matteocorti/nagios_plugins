%define version 1.0.0
%define release 0
%define name    check_nethz
%define _prefix /usr/lib/nagios/plugins/contrib

Summary:   A Nagios plugin to check the health of the nethz system
Name:      %{name}
Version:   %{version}
Release:   %{release}
License:   GPL
Packager:  Matteo Corti <matteo.corti@id.ethz.ch>
Group:     Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Source:    http://www.id.ethz.ch/people/allid_list/corti/%{name}-%{version}.tar.gz
Prefix:    %{_prefix}
BuildArch: noarch

Requires: perl

%description
A Nagios plugin to check the health of the nethz system

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
* Fri Aug 21 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0.0-0
- initial release
