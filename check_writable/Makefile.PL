# Load the Module::Install bundled in ./inc/
use inc::Module::Install;

##############################################################################
# Define metadata (we read it from the binary)

name              'check_writable';
version_from      'check_writable';
perl_version_from 'check_writable';
all_from          'check_writable.pod';

##############################################################################
# Specific dependencies

include 'version';

requires 'Carp'                          => 0;
requires 'Data::Random'                  => 0;
requires 'English'                       => 0;
requires 'File::Temp'                    => 0;
requires 'Getopt::Long'                  => 0;
requires 'Monitoring::Plugin'            => 0;
requires 'Monitoring::Plugin::Getopt'    => 0;
requires 'Monitoring::Plugin::Threshold' => 0;
requires 'Pod::Usage'                    => 0;
requires 'version'                       => 0;

install_script  'check_writable';

WriteMakefile(
    INSTALLSCRIPT        => '/usr/lib/nagios/plugins/contrib',
    INSTALLBIN           => '/usr/lib/nagios/plugins/contrib',
    INSTALLSITESCRIPT    => '/usr/lib/nagios/plugins/contrib',
);
