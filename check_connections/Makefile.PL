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
# Define metadata (we read it from the binary)

name         'check_connections';
version_from 'check_connections';
all_from     'check_connections.pod';

##############################################################################
# Specific dependencies

include 'version';

requires 'Carp'                      => 0;
requires 'English'                   => 0;
requires 'File::Slurp'               => 0;
requires 'Nagios::Plugin::Getopt'    => 0;
requires 'Nagios::Plugin'            => 0;
requires 'Nagios::Plugin::Threshold' => 0;
requires 'version'                   => 0;

install_script  'check_connections';

WriteMakefile(
    INSTALLSCRIPT        => '/usr/lib/nagios/plugins/contrib',
    INSTALLSITESCRIPT    => '/usr/lib/nagios/plugins/contrib',
    MAN1PODS             => { 'check_connections.pod' => 'blib/man1/check_connections.1', },
    MAN3PODS             => { },
);
