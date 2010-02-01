################################################################################
# File version information:
# $Id$
# $Revision$
# $HeadURL$
# $Date$
################################################################################

%define version 2.1.1
%define release 0
%define name    check_connections
%define nagiospluginsdir %{_libdir}/nagios/plugins

# No binaries in this package
%define debug_package %{nil}

Summary:   Nagios plugin to monitor the number of network connections
Name:      %{name}
Version:   %{version}
Release:   %{release}%{?dist}
License:   GPLv3+
Packager:  Matteo Corti <matteo.corti@id.ethz.ch>
Group:     Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source:    http://www.id.ethz.ch/people/allid_list/corti/%{name}-%{version}.tar.gz

# Fedora build requirement (not needed for EPEL{4,5})
BuildRequires: perl(ExtUtils::MakeMaker)

Requires:  nagios-plugins

%description
Nagios plugin to monitor the number of network connections

%prep
%setup -q

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
%{nagiospluginsdir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Mon Feb  1 2010 Matteo Corti <matteo.corti@id.ethz.ch> - 2.1.1-0
- updated to 2.1.1: several ePN and RPM fixes

* Wed Dec 17 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 2.1.0-0
- Updated to 2.1.0

* Mon Sep 24 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.2.0-0
- First RPM package

