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
use English qw(-no_match_vars);

our $VERSION = '3.0.0';

my $check_dir = File::Spec->catfile(qw(blib script check_dir));

sub whoami {
    my $output;
    my $pid = open $output, q{-|}, 'whoami'
      or croak "Cannot determine the user: $OS_ERROR";
    while (<$output>) {
        chomp;
        return $_;
    }
    if ( !( close $output ) && ( $OS_ERROR != 0 ) ) {

        # close to a piped open return false if the command with non-zero
        # status. In this case $! is set to 0
        croak "Error while closing pipe to whoami: $OS_ERROR\n";

    }

    croak 'Cannot determine the user';
    return;
}

require_ok($check_dir);

is(
    check_permissions('t/tests/file'),
    't/tests/file is not a directory',
    'File type'
);

my $dirname = 't/tests/unreadable';
if (! -d $dirname ) {
    mkdir $dirname, 0000
        or croak "Cannot create $dirname: $OS_ERROR";
}
my $expected_result = "$dirname is not readable";
if ( whoami() eq 'root' ) {
    # root can read dirs with 000
    $expected_result = undef;
}
is(
    check_permissions( $dirname ),
    $expected_result,
    'File type'
);

$dirname = 't/tests/unexecutable';
if (! -d $dirname ) {
    mkdir $dirname, 0644
        or croak "Cannot create t/tests/unexecutable: $OS_ERROR";
}
$expected_result = "$dirname is not executable";
if ( whoami() eq 'root' ) {
    # -x does not fail for root
    $expected_result = undef;
}
is(
    check_permissions( $dirname ),
    $expected_result,
    'File type'
);

1;
