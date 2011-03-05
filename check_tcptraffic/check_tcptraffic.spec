################################################################################
# File version information:
# $Id: check_updates.spec 1112 2009-12-10 16:35:09Z corti $
# $Revision: 1112 $
# $HeadURL: https://svn.id.ethz.ch/nagios_plugins/check_updates/check_updates.spec $
# $Date: 2009-12-10 17:35:09 +0100 (Thu, 10 Dec 2009) $
################################################################################

%define version          2.2.3
%define release          0
%define sourcename       check_tcptraffic
%define packagename      nagios-plugins-check-tcptraffic
%define nagiospluginsdir %{_libdir}/nagios/plugins

# No binaries in this package
%define debug_package    %{nil}

Summary:   A Nagios plugin to monitor the amount of TCP traffic
Name:      %{packagename}
Version:   %{version}
Obsoletes: check_tcptraffic
Release:   %{release}%{?dist}
License:   GPLv3+
Packager:  Matteo Corti <matteo.corti@id.ethz.ch>
Group:     Applications/System
BuildRoot: %{_tmppath}/%{packagename}-%{version}-%{release}-root-%(%{__id_u} -n)
Source:    http://www.id.ethz.ch/people/allid_list/corti/%{sourcename}-%{version}.tar.gz

# Fedora build requirement (not needed for EPEL{4,5})
BuildRequires: perl(ExtUtils::MakeMaker)

Requires:  nagios-plugins

%description
check_tcptraffic is a Nagios plugin to monitor the amount of TCP traffic

check_tcptraffic uses the /proc/net/dev Linux entry to compute the
amount of transferred bytes from the last plugin execution (temporary
data is stored in the /tmp/check_tcptraffic-iface file)

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
%doc AUTHORS Changes NEWS README TODO COPYING COPYRIGHT nagiosgrapher
%{nagiospluginsdir}/%{sourcename}
%{_mandir}/man1/%{sourcename}.1*

%changelog
* Thu Feb 17 2011 Matteo Corti <matteo.corti@id.ethz.ch> - 2.2.3-0
- added an optional debug log and corrected a bug in the handling of counter overflows

* Thu Feb 10 2011 Matteo Corti <matteo.corti@id.ethz.ch> - 2.2.2-0
- Added the nagiosgrapher template and renamed the RPM

* Wed Nov  3 2010 Matteo Corti <matteo.corti@id.ethz.ch> - 2.2.1-0
- fixed a minor bug in error handling

* Thu Oct 21 2010 Matteo Corti <matteo.corti@id.ethz.ch> - 2.2.0-0
- --critical and --warning now accept ranges (low:high)

* Sat Jan 30 2010 Matteo Corti <matteo.corti@id.ethz.ch> - 2.1.1-1
- updated to 2.1.1 (removed the double -r command line argument definition)

* Fri Sep 25 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 2.1.0-1
- updated to 2.1.0

* Fri Mar 21 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 2.0.3-0
- fixed missing usage message

* Thu Mar 20 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 2.0.2-0
- ePN compatibility

* Fri Dec  7 2007 root <matteo.corti@id.ethz.ch> - 2.0.1-0
- updated to 2.0.1 (bug fix)

* Fri Nov 30 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 2.0.0-0
- Major rewrite which is compatible with embedded perl and uses the Nagios::Plugin modules

* Wed Apr 25 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0-1
- Initial release
