# Load the Module::Install bundled in ./inc/
use inc::Module::Install;

##############################################################################
# Define metadata (we read it from the binary)

name         'check_nethz.pl';
version_from 'check_nethz.pl';
all_from     'check_nethz.pod';

##############################################################################
# Specific dependencies

include 'version';

requires 'Carp'                      => 0;
requires 'English'                   => 0;
requires 'DBI'                       => 0;
requires 'Nagios::Plugin'            => 0;
requires 'Nagios::Plugin::Getopt'    => 0;
requires 'Nagios::Plugin::Threshold' => 0;
requires 'Number::Format'            => 0;
requires 'Readonly'                  => 0;
requires 'version'                   => 0;

install_script  'check_nethz.pl';

WriteMakefile(
    INSTALLSCRIPT        => '/usr/lib/nagios/plugins/contrib',
    INSTALLBIN           => '/usr/lib/nagios/plugins/contrib',
    INSTALLSITESCRIPT    => '/usr/lib/nagios/plugins/contrib',
);
