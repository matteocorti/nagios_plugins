# Load the Module::Install bundled in ./inc/
use inc::Module::Install;

##############################################################################
# Define metadata (we read it from the binary and the POD)

name         'check_procs_multi';

version_from 'check_procs_multi';
all_from     'check_procs_multi.pod';

##############################################################################
# Specific dependencies

include 'version';

requires 'Carp'                      => 0;
requires 'English'                   => 0;
requires 'Getopt::Long'              => 0;
requires 'Nagios::Plugin'            => 0;
requires 'Nagios::Plugin::Threshold' => 0;
requires 'Pod::Usage'                => 0;
requires 'version'                   => 0;

install_script  'check_procs_multi';

WriteMakefile(
    INSTALLSCRIPT        => '/usr/lib/nagios/plugins/contrib',
);
