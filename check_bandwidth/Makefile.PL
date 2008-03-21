# Load the Module::Install bundled in ./inc/
use inc::Module::Install;

##############################################################################
# Define metadata (we read it from the binary)

name     'check_bandwidth';
version_from 'check_bandwidth';
all_from 'check_bandwidth.pod';

##############################################################################
# Specific dependencies

include 'version';

requires 'Carp'                      => 0;
requires 'English'                   => 0;
requires 'Getopt::Long'              => 0;
requires 'Nagios::Plugin'            => 0;
requires 'Nagios::Plugin::Threshold' => 0;
requires 'Net::DNS::Resolver'        => 0;
requires 'version'                   => 0;

install_script  'check_bandwidth';

WriteMakefile(
    INSTALLSCRIPT        => '/usr/lib/nagios/plugins/contrib',
);
