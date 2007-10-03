%define _use_internal_dependency_generator 0

Name: perl-Nagios-Plugin
Version: 0.21
Release: 2
Summary: A family of perl modules to streamline writing Nagios plugins
License: distributable
Group: Development/Libraries
URL: http://search.cpan.org/search?mode=module&query=Nagios%3a%3aPlugin
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: perl >= 0:5.00503
BuildRequires: perl-version

Requires:      perl-Math-Calc-Units
Requires:      perl-Class-Accessor

Source0: Nagios-Plugin-%{version}.tar.gz

%description
A family of perl modules to streamline writing Nagios plugins

%prep
%setup -q -n Nagios-Plugin-%{version} 

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
	grep -v "\.packlist" > Nagios-Plugin-%{version}-filelist
if [ "$(cat Nagios-Plugin-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit -1
fi

%files -f Nagios-Plugin-%{version}-filelist
%defattr(-,root,root)

%changelog
* Wed Oct  3 2007 root <matteo.corti@id.ethz.ch> - 0.21-2
- depends on perl-Class-Accessor

* Wed Oct  3 2007 root <matteo.corti@id.ethz.ch> - 0.21-1
- depends on perl-Math-Calc-Units

* Wed Oct  3 2007 root <matteo.corti@id.ethz.ch> - 0.21-0
- initial release
