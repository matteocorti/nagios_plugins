%define _use_internal_dependency_generator 0

Name: perl-Math-Calc-Units
Version: 2.03
Release: 0
Summary: Human-readable unit-aware calculator
License: distributable
Group: Development/Libraries
URL: http://search.cpan.org/search?mode=module&query=Math%3a%3aCalc%3a%3aUnits
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: perl >= 0:5.00503
BuildRequires: perl-version

Source0: Math-Calc-Units-%{version}.tar.gz

%description
Human-readable unit-aware calculator

%prep
%setup -q -n Math-Calc-Units-%{version} 

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
	grep -v "\.packlist" > Math-Calc-Units-%{version}-filelist
if [ "$(cat Math-Calc-Units-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit -1
fi

%files -f Math-Calc-Units-%{version}-filelist
%defattr(-,root,root)

%changelog
* Wed Oct  3 2007 root <matteo.corti@id.ethz.ch> - 0.21-0
- initial release
