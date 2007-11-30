# Load the Module::Install bundled in ./inc/
use inc::Module::Install;

##############################################################################
# Define metadata (we read it from the binary)

name     'check_tcptraffic';
all_from 'check_tcptraffic';

##############################################################################
# Specific dependencies

include 'version';

requires 'English'                   => 0;
requires 'Getopt::Long'              => 0;
requires 'Nagios::Plugin'            => 0;
requires 'Nagios::Plugin::Threshold' => 0;
requires 'Number::Format'            => 0;
requires 'Pod::Usage'                => 0;
requires 'version'                   => 0;

install_script  'check_tcptraffic';

WriteMakefile(
    INSTALLSCRIPT        => '/usr/lib/nagios/plugins/contrib',
);
