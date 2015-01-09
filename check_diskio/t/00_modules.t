#!perl

# $Id: README 1103 2009-12-07 07:49:19Z corti $
# $Revision: 1103 $
# $HeadURL: https://svn.id.ethz.ch/nagios_plugins/check_updates/README $
# $Date: 2009-12-07 08:49:19 +0100 (Mon, 07 Dec 2009) $

use 5.00800;

use strict;
use warnings;

use Test::More tests => 24;

our $VERSION = '3.2.4';

use_ok('Array::Unique');

use_ok('Carp');

use_ok('English');

use_ok('File::Slurp');

use_ok('List::MoreUtils');
can_ok( 'List::MoreUtils', 'any' );

use_ok('Monitoring::Plugin');
can_ok( 'Monitoring::Plugin', 'new' );
can_ok( 'Monitoring::Plugin', 'nagios_exit' );
can_ok( 'Monitoring::Plugin', 'add_perfdata' );
can_ok( 'Monitoring::Plugin', 'perfdata' );

use_ok('Monitoring::Plugin::Getopt');
can_ok( 'Monitoring::Plugin::Getopt', 'new' );
can_ok( 'Monitoring::Plugin::Getopt', 'arg' );
can_ok( 'Monitoring::Plugin::Getopt', 'getopts' );
can_ok( 'Monitoring::Plugin::Getopt', 'get' );

use_ok('Monitoring::Plugin::Threshold');
can_ok( 'Monitoring::Plugin::Threshold', 'new' );
can_ok( 'Monitoring::Plugin::Threshold', 'set_thresholds' );

use_ok('Number::Format');
can_ok( 'Number::Format', 'format_number' );

use_ok('POSIX');
can_ok( 'POSIX', 'uname' );

use_ok('Readonly');

1;
