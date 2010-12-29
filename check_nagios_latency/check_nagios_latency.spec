%define version 1.0.0
%define release 0
%define sourcename       check_nagios_latency
%define packagename      nagios-plugins-check_nagios_latency
%define nagiospluginsdir %{_libdir}/nagios/plugins

# No binaries in this package
%define debug_package    %{nil}

Summary:   Checks Nagios latency
Name:      %{packagename}
Obsoletes: check_nagios_latency
Version:   %{version}
Release:   %{release}%{?dist}
License:   GPLv3+
Packager:  Matteo Corti <matteo.corti@id.ethz.ch>
Group:     Applications/System
BuildRoot: %{_tmppath}/%{packagename}-%{version}-%{release}-root-%(%{__id_u} -n)
URL:           https://trac.id.ethz.ch/projects/nagios_plugins/wiki/check_nagios_latency
Source:        https://trac.id.ethz.ch/projects/nagios_plugins/downloads/%{sourcename}-%{version}.tar.gz

Requires:      nagios-plugins

%description
Checks Nagios latency

%prep
%setup -q -n %{sourcename}-%{version}

%build

%install
make DESTDIR=${RPM_BUILD_ROOT}%{nagiospluginsdir} MANDIR=${RPM_BUILD_ROOT}%{_mandir} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%doc AUTHORS ChangeLog NEWS README INSTALL TODO COPYING VERSION COPYRIGHT
%attr(0755, root, root) %{nagiospluginsdir}/check_nagios_latency
%{_mandir}/man1/%{sourcename}.1*

%changelog
* Wed Dec 29 2010 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0.0-0
- added the -f option

* Wed Nov 28 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.3-0
- updated to 0.9.3 (added -n option)

* Thu Sep 20 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.0-0
- Initial beta release
