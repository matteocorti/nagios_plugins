%define version 2.0.0
%define release 0
%define name    check_tcptraffic
%define _prefix /usr/lib/nagios/plugins/contrib

Summary:   A Nagios plugin to monitor the amount of TCP traffic
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
check_tcptraffic is a Nagios plugin to monitor the amount of TCP traffic

check_tcptraffic uses the /proc/net/dev Linux entry to compute the
amount of transferred bytes from the last plugin execution (temporary
data is stored in the /tmp/check_tcptraffic-iface file)

%prep
%setup -q

%build
%__perl Makefile.PL  INSTALLSCRIPT=%{buildroot}%{_prefix} INSTALLSITEMAN1DIR=%{buildroot}/usr/share/man/man1
make

%install
make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0644)
%doc AUTHORS Changes NEWS README INSTALL TODO COPYING VERSION
%attr(0755, root, root) %{_prefix}/%{name}
%attr(0755, root, root) /usr/share/man/man1/%{name}.1.gz

%changelog
* Fri Nov 30 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 2.0.0-0
- Major rewrite which is compatible with embedded perl and uses the Nagios::Plugin modules

* Wed Apr 25 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0-1
- Initial release
