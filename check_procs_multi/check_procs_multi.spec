################################################################################
# File version information:
# $Id$
# $Revision$
# $HeadURL4
# $Date$
################################################################################


%define version 1.1.1
%define release 1
%define name    check_procs_multi
%define nagiospluginsdir %{_libdir}/nagios/plugins

# No binaries in this package
%define debug_package %{nil}

Summary:   Nagios plugin similar to check_procs able to check several processes at once.
Name:      %{name}
Version:   %{version}
Release:   %{release}%{?dist}
License:   GPLv3+
Packager:  Matteo Corti <matteo.corti@id.ethz.ch>
Group:     Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
URL:       http://trac.id.ethz.ch/projects/nagios_plugins/wiki/check_procs_multi
Source:    http://www.id.ethz.ch/people/allid_list/corti/%{name}-%{version}.tar.gz

# Fedora build requirement (not needed for EPEL{4,5})
BuildRequires: perl(ExtUtils::MakeMaker)

Requires:  nagios-plugins

%description
check_procs_multi is a Nagios plugin similar to check_procs able to
check several processes at once.

%prep
%setup -q

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor INSTALLSCRIPT=%{nagiospluginsdir} INSTALLVENDORSCRIPT=%{nagiospluginsdir}
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
%doc AUTHORS Changes NEWS README INSTALL  TODO COPYING COPYRIGHT VERSION
%{nagiospluginsdir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Mon Jan 25 2010 Matteo Corti <matteo.corti@id.ethz.ch> - 1.1.1-0
- Updated to 1.1.1 + several spec file fixes 

* Tue Jul  7 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 1.1.0-0
- check with pgrep if ps fails

* Mon Jun 15 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0.1-0
- removed dep on Net::DNS

* Mon Jun  9 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0.0-0
- grepping in perl

* Mon May 26 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.5-0
- fixed a bug when command name != proc name

* Fri Mar 21 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.4-0
- fixed the missing usage message

* Thu Mar 20 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.3-0
- ePN compatibility

* Tue Feb 12 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.2-0
- fixed a bug in the sanity checks

* Tue Feb 12 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.1-0
- version 0.9.1 (default min 1)

* Mon Feb 11 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.0-0
- Initial release
