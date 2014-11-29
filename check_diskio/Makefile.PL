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

requires 'Array::Unique'             => 0;
requires 'English'                   => 0;
requires 'Fcntl'                     => 0;
requires 'File::Slurp'               => 0;
requires 'List::MoreUtils'           => 0;
requires 'Nagios::Plugin'            => 0;
requires 'Nagios::Plugin::Getopt'    => 0;
requires 'Nagios::Plugin::Threshold' => 0;
requires 'Number::Format'            => 0;
requires 'POSIX'                     => 0;
requires 'Readonly'                  => 0;

install_script  'check_diskio';

tests 't/*.t';
test_requires 'Test::More'       => 0;
test_requires 'File::Spec'       => 0;

WriteMakefile(
    INSTALLSCRIPT        => '/usr/lib/nagios/plugins/contrib',
    INSTALLSITESCRIPT    => '/usr/lib/nagios/plugins/contrib',
    MAN1PODS             => { 'check_diskio.pod' => 'blib/man1/check_diskio.1', },
    MAN3PODS             => { },
);
