%define _use_internal_dependency_generator 0

%define module Net-DHCP-Watch

Name: perl-%{module}
Version: 2.03
Release: 0
Summary: A class for monitoring a remote DHCP server
License: distributable
Group: Development/Libraries
URL: http://search.cpan.org/search?mode=module&query=Math%3a%3aCalc%3a%3aUnits
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: perl >= 0:5.00503
BuildRequires: perl-version

Source0: %{module}-%{version}.tar.gz

%description
Net::DHCP::Watch is a module to help monitor REMOTE DHCP servers. It
opens an udp socket to send and receive responses to and from a DHCP
server. It stores the last connection status information.

At the time of this writing, the DHCP protocol has not implemented yet a
failover protocol (it is in proposal stage). This module helps to write 
some simple code to implement this feature.

%prep
%setup -q -n %{module}-%{version} 

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL PREFIX=$RPM_BUILD_ROOT/usr INSTALLDIRS=vendor
make
make test


%clean
rm -rf $RPM_BUILD_ROOT
%install

rm -rf $RPM_BUILD_ROOT
make install

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

find $RPM_BUILD_ROOT \( -name perllocal.pod -o -name .packlist \) -exec rm -v {} \;

find $RPM_BUILD_ROOT/usr -type f -print | \
	sed "s@^$RPM_BUILD_ROOT@@g" | \
	grep -v perllocal.pod | \
	grep -v "\.packlist" > %{module}-%{version}-filelist
if [ "$(cat %{module}-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit -1
fi

%files -f %{module}-%{version}-filelist
%defattr(-,root,root)

%changelog
* Mon Dec 17 2007 root <matteo.corti@id.ethz.ch> - 2.03-0
- Initial release
