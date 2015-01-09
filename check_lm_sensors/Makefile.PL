# Load the Module::Install bundled in ./inc/
use inc::Module::Install;

##############################################################################
# Define metadata (we read it from the binary)

name              'check_lm_sensors';
version_from      'check_lm_sensors';
perl_version_from 'check_lm_sensors';
all_from          'check_lm_sensors.pod';

##############################################################################
# Specific dependencies

include 'version';

requires 'Carp'                          => 0;
requires 'English'                       => 0;
requires 'Getopt::Long'                  => 0;
requires 'List::MoreUtils'               => 0;
requires 'Monitoring::Plugin'            => 0.31;
requires 'Monitoring::Plugin::Threshold' => 0;
requires 'version'                       => 0;

install_script  'check_lm_sensors';

WriteMakefile(
    INSTALLSCRIPT        => '/usr/lib/nagios/plugins/contrib',
    INSTALLBIN           => '/usr/lib/nagios/plugins/contrib',
    INSTALLSITESCRIPT    => '/usr/lib/nagios/plugins/contrib',
);
