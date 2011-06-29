################################################################################
# File version information:
# $Id: check_updates.spec 1249 2011-05-25 08:27:23Z corti $
# $Revision: 1249 $
# $HeadURL: https://svn.id.ethz.ch/nagios_plugins/check_updates/check_updates.spec $
# $Date: 2011-05-25 10:27:23 +0200 (Wed, 25 May 2011) $
################################################################################

%define version 3.0.0
%define release 0
%define sourcename       check_dir
%define packagename      nagios-plugins-check-dir
%define nagiospluginsdir %{_libdir}/nagios/plugins

# No binaries in this package
%define debug_package    %{nil}

Summary:       Nagios plugin to monitor the number of files in one or more directories.
Name:          %{packagename}
Obsoletes:     check_dir
Version:       %{version}
Release:       %{release}%{?dist}
License:       GPLv3+
Packager:      Matteo Corti <matteo.corti@id.ethz.ch>
Group:         Applications/System
BuildRoot:     %{_tmppath}/%{packagename}-%{version}-%{release}-root-%(%{__id_u} -n)
URL:           https://trac.id.ethz.ch/projects/nagios_plugins/wiki/check_dir
Source:        https://trac.id.ethz.ch/projects/nagios_plugins/downloads/%{sourcename}-%{version}.tar.gz

# Fedora build requirement (not needed for EPEL{4,5})


BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: perl(Nagios::Plugin)

Requires:      nagios-plugins

%description
Nagios plugin to monitor the number of files in one or more directories.

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
