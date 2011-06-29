# Load the Module::Install bundled in ./inc/
use inc::Module::Install;

################################################################################
# Version information:
#
# $Id: Makefile.PL 1238 2011-05-24 06:40:44Z corti $
# $Revision: 1238 $
# $HeadURL: https://svn.id.ethz.ch/nagios_plugins/check_updates/Makefile.PL $
# $Date: 2011-05-24 08:40:44 +0200 (Tue, 24 May 2011) $
#

##############################################################################
# Define metadata (we read it from the binary)

name              'check_dir';
version_from      'check_dir';
perl_version_from 'check_dir';
all_from          'check_dir.pod';

##############################################################################
# Specific dependencies

include 'version';

requires 'English'                   => 0;
requires 'Getopt::Long'              => 0;
requires 'Nagios::Plugin'            => 0;
requires 'Nagios::Plugin::Range'     => 0;
requires 'Nagios::Plugin::Threshold' => 0;

install_script  'check_dir';

tests 't/*.t';
test_requires 'Carp'                 => 0;
test_requires 'File::Path'           => '2.06';
test_requires 'File::Spec'           => 0;
test_requires 'Test::More'           => 0;

WriteMakefile(
    INSTALLSCRIPT        => '/usr/lib/nagios/plugins/contrib',
    INSTALLSITESCRIPT    => '/usr/lib/nagios/plugins/contrib',
    MAN1PODS             => { 'check_dir.pod' => 'blib/man1/check_dir.1', },
    MAN3PODS             => { },
);
