#!perl

# $Id: README 1103 2009-12-07 07:49:19Z corti $
# $Revision: 1103 $
# $HeadURL: https://svn.id.ethz.ch/nagios_plugins/check_updates/README $
# $Date: 2009-12-07 08:49:19 +0100 (Mon, 07 Dec 2009) $

use 5.00800;

use strict;
use warnings;

use Test::More tests => 5;

use File::Spec;

our $VERSION = '3.0.0';

my $check_dir = File::Spec->catfile(qw(blib script check_dir));

require_ok($check_dir);

is( max( 0, 1 ), 1, 'max' );
is( max( 1, 0 ), 1, 'max' );
is( max( 1, 1 ), 1, 'max' );

#<<<
is( max( -1, -2 ), -1, 'max with negative numbers' );    ## no critic (ProhibitMagicNumbers)
#>>>
1;
