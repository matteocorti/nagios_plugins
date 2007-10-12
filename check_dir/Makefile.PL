# Load the Module::Install bundled in ./inc/
use inc::Module::Install;

##############################################################################
# Define metadata (we read it from the binary)

name     'check_dir';
all_from 'check_dir';

##############################################################################
# Specific dependencies

requires 'Carp'                      => 0;
requires 'English'                   => 0;
requires 'File::stat'                => 0;
requires 'Getopt::Long'              => 0;
requires 'Nagios::Plugin'            => 0;
requires 'Nagios::Plugin::Threshold' => 0;
requires 'Pod::Usage'                => 0;
requires 'version'                   => 0;

install_script  'check_dir';

WriteMakefile(
    INSTALLDIRS    => 'site',
    INSTALLSITEBIN => '/usr/lib/nagios/plugins/contrib',
    INSTALLSCRIPT  => '/usr/lib/nagios/plugins/contrib',        
);
