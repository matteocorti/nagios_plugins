#!perl

# $Id: README 1103 2009-12-07 07:49:19Z corti $
# $Revision: 1103 $
# $HeadURL: https://svn.id.ethz.ch/nagios_plugins/check_updates/README $
# $Date: 2009-12-07 08:49:19 +0100 (Mon, 07 Dec 2009) $

use 5.00800;

use strict;
use warnings;

use Test::More tests => 4;

use File::Spec;
use Carp;

our $VERSION = '3.0.0';

my $check_dir = File::Spec->catfile(qw(blib script check_dir));

require_ok($check_dir);

is(
    check_permissions('t/examples/file'),
    't/examples/file is not a directory',
    'File type'
);

my $dirname = 't/examples/unreadable';
if (! -d $dirname ) {
    mkdir $dirname, 0000
        or croak "Cannot create $dirname";
}
is(
    check_permissions( $dirname ),
    "$dirname is not readable",
    'File type'
);

$dirname = 't/examples/unexecutable';
if (! -d $dirname ) {
    mkdir $dirname, 0644
        or croak 'Cannot create t/examples/unexecutable';
}
is(
    check_permissions( $dirname ),
    "$dirname is not executable",
    'File type'
);

1;
