# Load the Module::Install bundled in ./inc/
use inc::Module::Install;

##############################################################################
# Define metadata (we read it from the binary)

name              'check_diskio';
version_from      'check_diskio';
perl_version_from 'check_diskio';
all_from          'check_diskio.pod';

##############################################################################
# Specific dependencies

include 'version';

my %prereqs = (
    'Array::Unique'   => 0,
    'English'         => 0,
    'Fcntl'           => 0,
    'File::Slurp'     => 0,
    'List::MoreUtils' => 0,
    'Number::Format'  => 0,
    'POSIX'           => 0,
    'Readonly'        => 0,
);


if( eval { require Monitoring::Plugin } ) {
    $prereqs{'Monitoring::Plugin'} = 0;
}
else {
    $prereqs{'Nagios::Plugin'} = 0;
}

if( eval { require Monitoring::Plugin::Threshold } ) {
    $prereqs{'Monitoring::Plugin::Threshold'} = 0;
}
else {
    $prereqs{'Nagios::Plugin::Threshold'} = 0;
}

if( eval { require Monitoring::Plugin::Getopt } ) {
    $prereqs{'Monitoring::Plugin::Getopt'} = 0;
}
else {
    $prereqs{'Nagios::Plugin::Getopt'} = 0;
}

install_script  'check_diskio';

tests 't/*.t';
test_requires 'Test::More'       => 0;
test_requires 'File::Spec'       => 0;

WriteMakefile(
    PREREQ_PM            => \%prereqs,
    INSTALLSCRIPT        => '/usr/lib/nagios/plugins/contrib',
    INSTALLSITESCRIPT    => '/usr/lib/nagios/plugins/contrib',
    MAN1PODS             => { 'check_diskio.pod' => 'blib/man1/check_diskio.1', },
    MAN3PODS             => { },
);
