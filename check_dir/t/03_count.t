#!perl

# $Id: README 1103 2009-12-07 07:49:19Z corti $
# $Revision: 1103 $
# $HeadURL: https://svn.id.ethz.ch/nagios_plugins/check_updates/README $
# $Date: 2009-12-07 08:49:19 +0100 (Mon, 07 Dec 2009) $

use 5.00800;

use strict;
use warnings;

use Test::More tests => 8;
use Carp;
use File::Spec;
use File::Path;
use English qw(-no_match_vars);

our $VERSION = '3.0.0';

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
}

sub create_file {

    my $filename = shift;

    if ( -f $filename ) {
        return;
    }

    open my $FH, '>', $filename
      or croak "Cannot create $filename: $OS_ERROR";

    close $FH
      or croak "Cannot close $filename: $OS_ERROR";

    return;

}

sub create_dir {

    my $dirname = shift;

    if ( -d $dirname ) {
        return;
    }

    mkdir $dirname
      or croak "Cannot create $dirname: $OS_ERROR";

    return;

}

my $check_dir = File::Spec->catfile(qw(blib script check_dir));

require_ok($check_dir);

################################################################################
# Initialize

create_dir('t/tests');

################################################################################
# Permission checks

# Directory should be a directory
create_file('t/tests/file');
is(
    check_permissions('t/tests/file'),
    't/tests/file is not a directory',
    'File type'
);

# Unreadable directories
my $dirname = 't/tests/unreadable';
if ( !-d $dirname ) {
    ## no critic (ProhibitMagicNumbers)
    mkdir $dirname, 0000
      or croak "Cannot create $dirname: $OS_ERROR";
    ## use critic
}
my $expected_result = "$dirname is not readable";
if ( whoami() eq 'root' ) {

    # root can read dirs with 000
    $expected_result = undef;
}
is( check_permissions($dirname), $expected_result, 'File type' );
rmdir $dirname
  or croak "Cannot remove $dirname: $OS_ERROR";

# Missing executable permission
$dirname = 't/tests/unexecutable';
if ( !-d $dirname ) {
    ## no critic (ProhibitMagicNumbers)
    mkdir $dirname, 0644
      or croak "Cannot create t/tests/unexecutable: $OS_ERROR";
    ## use critic
}
$expected_result = "$dirname is not executable";
if ( whoami() eq 'root' ) {

    # -x does not fail for root
    $expected_result = undef;
}
is( check_permissions($dirname), $expected_result, 'File type' );

rmdir $dirname
  or croak "Cannot remove $dirname: $OS_ERROR";

################################################################################
# Count files

my $prefix = 't/tests/counts';
create_dir($prefix);

$dirname = "$prefix/files";
create_dir($dirname);
create_file("$dirname/1");
create_file("$dirname/2");
is( scalar get_entries($dirname), 2, 'Files' );

$dirname = "$prefix/empty";
create_dir($dirname);
is( scalar get_entries($dirname), 0, 'Empty' );

$dirname = "$prefix/hidden";
create_dir($dirname);
create_file("$dirname/.1");
create_file("$dirname/.2");
is( scalar get_entries($dirname), 2, 'Hidden files' );

$dirname = "$prefix/dirs";
create_dir($dirname);
create_dir("$dirname/1");
create_dir("$dirname/2");
is( scalar get_entries($dirname), 2, 'Directories' );

################################################################################
# Finalize

File::Path::remove_tree( 't/tests', { error => \my $error } );
if ( @{$error} ) {
    croak "Error deleting $prefix: " . ( join q{, }, @{$error} );
}

1;
