#!perl

# $Id: README 1103 2009-12-07 07:49:19Z corti $
# $Revision: 1103 $
# $HeadURL: https://svn.id.ethz.ch/nagios_plugins/check_updates/README $
# $Date: 2009-12-07 08:49:19 +0100 (Mon, 07 Dec 2009) $

use 5.00800;

use strict;
use warnings;

use Test::More tests => 6;

use File::Spec;

our $VERSION = '3.2.4';

my $check_diskio = File::Spec->catfile(qw(blib script check_diskio));

## no critic (ValuesAndExpressions::ProhibitMagicNumbers)

require_ok($check_diskio);

# any user is OK
like( whoami(), '/[\w]/mxs', 'whoami' );

my @result;

@result = shortenrate( 2048, 1024 );
is( $result[0], 2,   'shortenrate value' );
is( $result[1], 'K', 'shortenrate unit' );

@result = shortenrate( 4096 * 1024, 1024 );
is( $result[0], 4,   'shortenrate value' );
is( $result[1], 'M', 'shortenrate unit' );

1;
