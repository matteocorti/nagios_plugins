%define version 1.1.2
%define release 1
%define sourcename       check_cpu
%define packagename      nagios-plugins-check-cpu
%define nagiospluginsdir %{_libdir}/nagios/plugins

# No binaries in this package
%define debug_package    %{nil}

Summary:   Nagios plugin to monitor the CPU usage on Linux systems
Name:          %{packagename}
Version:       %{version}
Obsoletes:     check_cpu
Release:       %{release}%{?dist}
License:       GPLv3+
Packager:      Matteo Corti <matteo@corti.li>
Group:         Applications/System
BuildRoot:     %{_tmppath}/%{packagename}-%{version}-%{release}-root-%(%{__id_u} -n)
URL:           https://trac.id.ethz.ch/projects/nagios_plugins/wiki/check_cpu
Source:        https://trac.id.ethz.ch/projects/nagios_plugins/downloads/%{sourcename}-%{version}.tar.gz

Requires: perl

%description
Nagios plugin to monitor the CPU usage on Linux systems

%prep
%setup -q -n %{sourcename}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor \
    INSTALLSCRIPT=%{nagiospluginsdir} \
    INSTALLVENDORSCRIPT=%{nagiospluginsdir}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name "*.pod" -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS Changes NEWS README TODO COPYING COPYRIGHT
%{nagiospluginsdir}/%{sourcename}
%{_mandir}/man1/%{sourcename}.1*

%changelog
* Thu Aug 27 2015 Matteo Corti <matteo.corti@id.ethz.ch> - 1.1.2-1
- Upgrade to 1.1.2

* Thu Aug 27 2015 Matteo Corti <matteo@corti.li> - 1.1.1-1
- Upgrade to 1.1.1

* Fri Dec 18 2014 Matteo Corti <matteo@corti.li> - 1.1.0-0
- general spec update

* Fri Mar 21 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0.3-0
- fixed the missing usage messages

* Thu Mar 20 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0.2-0
- ePN compatibility

* Wed Oct 31 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 2.0.0-0
- Initial RPM package
