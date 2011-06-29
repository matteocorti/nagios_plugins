#!perl

# $Id: README 1103 2009-12-07 07:49:19Z corti $
# $Revision: 1103 $
# $HeadURL: https://svn.id.ethz.ch/nagios_plugins/check_updates/README $
# $Date: 2009-12-07 08:49:19 +0100 (Mon, 07 Dec 2009) $

use 5.00800;

use strict;
use warnings;

use Test::More tests => 5;
use Carp;
use File::Spec;
use File::Path;
use English qw(-no_match_vars);

our $VERSION = '3.0.0';

sub create_file {

    my $filename = shift;

    if ( -f $filename ) {
        return;
    }

    my $FH;
    open $FH, '>', $filename
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

create_dir ( 't/tests' );
my $prefix = 't/tests/counts';
create_dir ( $prefix );

my $dirname;

$dirname = "$prefix/files";
create_dir ( $dirname );
create_file("$dirname/1");
create_file("$dirname/2");
is(
    scalar get_entries( $dirname ),
    2,
    'Files'
);

$dirname = "$prefix/empty";
create_dir ( $dirname );
is(
    scalar get_entries( $dirname ),
    0,
    'Empty'
);

$dirname = "$prefix/hidden";
create_dir ( $dirname );
create_file("$dirname/.1");
create_file("$dirname/.2");
is(
    scalar get_entries( $dirname ),
    2,
    'Hidden files'
);

$dirname = "$prefix/dirs";
create_dir ( $dirname );
create_dir ( "$dirname/1" );
create_dir ( "$dirname/2" );
is(
    scalar get_entries( $dirname ),
    2,
    'Directories'
);

File::Path::remove_tree( $prefix, { error => \my $error } );
if ( @{$error} ) {
    croak "Error deleting $prefix: " . ( join q{, }, @{$error} );
}

1;
