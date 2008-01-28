%define _use_internal_dependency_generator 0
%define module Net-Traceroute

Name: perl-%{module}
Version: 1.10
Release: 0
Summary: Net::Traceroute
License: distributable
Group: Development/Libraries
URL: http://search.cpan.org/search?mode=module&query=IO%3a%3aInterface
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: perl >= 0:5.00503
BuildRequires: perl-version

Source0: %{module}-%{version}.tar.gz

%description
Net::Traceroute

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
* Fri Jan 11 2008 root <matteo.corti@id.ethz.ch> - 1.04-0
- initial release

