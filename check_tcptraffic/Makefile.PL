# Load the Module::Install bundled in ./inc/
use inc::Module::Install;

################################################################################
# Version information:
#
# $Id: Makefile.PL 1111 2009-12-09 07:12:23Z corti $
# $Revision: 1111 $
# $HeadURL: https://svn.id.ethz.ch/nagios_plugins/check_updates/Makefile.PL $
# $Date: 2009-12-09 08:12:23 +0100 (Wed, 09 Dec 2009) $
#

##############################################################################
# Define metadata (we read it from the binary)

name         'check_tcptraffic';
version_from 'check_tcptraffic';
all_from     'check_tcptraffic.pod';

##############################################################################
# Specific dependencies

include 'version';

requires 'Carp'                      => 0;
requires 'English'                   => 0;
requires 'Nagios::Plugin'            => 0;
requires 'Nagios::Plugin::Range'     => 0;
requires 'Nagios::Plugin::Threshold' => 0;
requires 'Readonly'                  => 0;
requires 'version'                   => 0;

install_script  'check_tcptraffic';

WriteMakefile(
    INSTALLSCRIPT        => '/usr/lib/nagios/plugins/contrib',
    INSTALLSITESCRIPT    => '/usr/lib/nagios/plugins/contrib',
    MAN1PODS             => { 'check_tcptraffic.pod' => 'blib/man1/check_tcptraffic.1', },
    MAN3PODS             => { },
);
