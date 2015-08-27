# Load the Module::Install bundled in ./inc/
use inc::Module::Install;

##############################################################################
# Define metadata (we read it from the binary)

name              'check_cpu';
version_from      'check_cpu';
perl_version_from 'check_cpu';
all_from          'check_cpu.pod';

##############################################################################
# Specific dependencies

include 'version';

my %prereqs = (
    'Carp'                          => 0,
    'English'                       => 0,
    'File::Temp'                    => 0,
    'File::Copy'                    => 0,
    'Getopt::Long'                  => 0,
    'version'                       => 0,    
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

install_script 'check_cpu';

WriteMakefile(
    PREREQ_PM            => \%prereqs,
    INSTALLSCRIPT        => '/usr/lib/nagios/plugins/contrib',
    INSTALLSITESCRIPT    => '/usr/lib/nagios/plugins/contrib',
    MAN1PODS             => { 'check_cpu.pod' => 'blib/man1/check_cpu.1', },
    MAN3PODS             => { },
);
