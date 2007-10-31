%define _use_internal_dependency_generator 0

Name: perl-Number-Format
Version: 1.52
Release: 0
Summary: Automated accessor generation
License: distributable
Group: Development/Libraries
URL: http://search.cpan.org/search?mode=module&query=Class%3a%3aAccessor
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: perl >= 0:5.00503
BuildRequires: perl-version

Source0: Number-Format-%{version}.tar.gz

%description
Automated accessor generation

%prep
%setup -q -n Number-Format-%{version} 

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
	grep -v "\.packlist" > Number-Format-%{version}-filelist
if [ "$(cat Number-Format-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit -1
fi

%files -f Number-Format-%{version}-filelist
%defattr(-,root,root)

%changelog
* Wed Oct 31 2007 root <matteo.corti@id.ethz.ch> - 1.52-0
- initial release
