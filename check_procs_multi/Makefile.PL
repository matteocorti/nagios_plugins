# Load the Module::Install bundled in ./inc/
use inc::Module::Install;

################################################################################
# Version information:
#
# $Id$
# $Revision$
# $HeadURL$
# $Date$
#

##############################################################################
# Define metadata (we read it from the binary and the POD)

name              'check_procs_multi';

version_from      'check_procs_multi';
perl_version_from 'check_procs_multi';
all_from          'check_procs_multi.pod';


##############################################################################
# Specific dependencies

include 'version';

requires 'Carp'                          => 0;
requires 'English'                       => 0;
requires 'Getopt::Long'                  => 0;
requires 'Monitoring::Plugin'            => 0;
requires 'Monitoring::Plugin::Threshold' => 0;
requires 'version'                       => 0;

install_script  'check_procs_multi';

WriteMakefile(
    INSTALLSCRIPT        => '/usr/lib/nagios/plugins/contrib',
    INSTALLSITESCRIPT    => '/usr/lib/nagios/plugins/contrib',
    MAN1PODS             => { 'check_procs_multi.pod' => 'blib/man1/check_procs_multi.1', },
    MAN3PODS             => { },
);
