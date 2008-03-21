%define version 1.0.3
%define release 0
%define name    check_afs_rpc
%define _prefix /usr/lib/nagios/plugins/contrib

Summary:   Nagios plugin for checking AFS file servers to see if there are client connections waiting for a free thread
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
check_afs_rpc is a Nagios plugin for checking AFS file servers to see if
there are client connections waiting for a free thread.  If there are more
than a few of these, AFS performance tends to be very slow; this is a fairly
reliable way to catch overloaded file servers.  By default, check_rxdebug
returns a critical error if there are more than eight connections waiting
for a free thread and a warning if there are more than two.  These
thresholds can be changed with the --critical and --warning options.

check_afs_rpc will always print out a single line of output including the
number of blocked connections, displaying whether this is critical, a
warning, or okay.

%prep
%setup -q

%build
%__perl Makefile.PL  INSTALLSCRIPT=%{buildroot}%{_prefix} INSTALLSITEMAN3DIR=%{buildroot}/usr/share/man/man3
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
* Fri Mar 21 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0.3-0
- use subs qw() to avoid redeclaration errors

* Fri Mar 21 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0.2-0
- usage no longer using POD (which is now in a separate file)

* Thu Mar 20 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0.1-0
- ePN compatibility

* Tue Nov  6 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0.0-0
- Initial release
