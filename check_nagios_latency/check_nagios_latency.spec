%define version 0.9.3
%define release 0
%define name    check_nagios_latency
%define _prefix /usr/lib/nagios/plugins/contrib

Summary:   Checks Nagios latency
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
Checks Nagios latency

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
%attr(0755, root, root) %{_prefix}/check_nagios_latency

%changelog
* Wed Nov 28 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.3-0
- updated to 0.9.3 (added -n option)

* Thu Sep 20 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.0-0
- Initial beta release
