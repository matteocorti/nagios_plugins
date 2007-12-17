#!/usr/bin/perl -w
#
# check_dhcp.pl - Nagios Plugin
#
# Copyright (C) 2006 Carlos Vicente.  University of Oregon.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
#
# Report bugs to:
#
# Carlos Vicente <cvicente@ns.uoregon.edu>
# 
#
use strict;
use IO::Socket;
use IO::Interface;
use Net::DHCP::Watch;
use Getopt::Long qw(:config no_ignore_case);

my ($status, $host, $interface, $mac, $ip, $verbose, $timeout);
my $VERSION     = 0.1;
my $HELP        = 0;
my $DOTTED_QUAD = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}';

# Default values
$timeout = 5;

my %STATUSCODE = (  'OK'       => '0',
                    'WARNING'  => '1',
                    'CRITICAL' => '2',
		    'UNKNOWN'  => '3');

my $usage = <<EOF;
 
Copyright (C) 2006 Carlos Vicente.  University of Oregon.

This plugin tests the availability of a given DHCP server using unicast delivery.
This is necessary if the monitoring host is on a different subnet. Using broadcast
and a DHCP relay would also prevent the check from probing individual servers.

Usage: check_dhcp -H|--host  -i|--interface [-t|--timeout]
 -H, --host=ADDRESS
   IP address of DHCP server that we must hear from
 -i, --interface=STRING
   Interface to to use for listening (i.e. eth0)
 -t, --timeout=INTEGER
   Seconds to wait for DHCPOFFER before timeout occurs (default: $timeout)
 -h, --help
   Print detailed help screen

Note: This plugin will need to run with root permissions in order to access priviledge
      ports 67 & 68.  Since Nagios by default runs its plugins under unpriviledged
      user 'nagios', you will need to setuid root like:

           % chown root:root check_dhcp.pl
           % chmod 4755 check_dhcp.pl


EOF

# handle cmdline args
my $result = GetOptions( "H|host=s"        => \$host,
			 "i|interface=s"   => \$interface,
			 "t|timeout:i"     => \$timeout,
			 "h|help"          => \$HELP,
			 );

if( !$result ) {
    print "ERROR: Problem with cmdline args\n";
    print $usage;
    exit($STATUSCODE{'UNKNOWN'});
}
if( $HELP ) {
    print $usage;
    exit($STATUSCODE{'UNKNOWN'});
}

if ( !($host && $interface) ){
    print "ERROR: Missing required arguments\n";
    print $usage;
    exit($STATUSCODE{'UNKNOWN'});
}
if ( $host =~ /($DOTTED_QUAD)/ ){
    $host = $1;
}else{ 
    print "Invalid IP Address: $host\n";
    exit($STATUSCODE{'UNKNOWN'});
} 

# Get the mac and IP address for the given interface
my $s = IO::Socket::INET->new(Proto => 'udp');
if ( !($ip  = $s->if_addr($interface)) ){
    print "Error: $!\n";
    exit($STATUSCODE{'CRITICAL'});
}
if ( !($mac  = $s->if_hwaddr($interface)) ){
    print "Error: $!\n";
    exit($STATUSCODE{'CRITICAL'});
}
# This is needed in order to avoid sperl complaining
# about "Insecure dependencies"
if ( $ip =~ /($DOTTED_QUAD)/ ){
    $ip = $1;
}else{ 
    print "Invalid IP Address: $ip\n";
    exit($STATUSCODE{'UNKNOWN'});
} 

# Initialize object
my $dhcp = Net::DHCP::Watch->new({
    client  => $ip,
    server  => $host,
    ether   => $mac,
    timeout => $timeout
    });

# Open network
# If something is wrong above, this one will fail.
# I wish this module did a better job of error handling
unless( $dhcp->watch() ){
    exit($STATUSCODE{'CRITICAL'});
}

# Get status
my $stat = $dhcp->status;

if ( $stat->{Ok}  ) {
    print "Received DHCPOFFER at ", $stat->{Time}, "\n";
    exit($STATUSCODE{'OK'});
}elsif ( $stat->{Bad} ){
    print "No response from server\n";
    exit($STATUSCODE{'CRITICAL'});
}else{
    print "Undetermined error\n";
    exit($STATUSCODE{'UNKNOWN'});
}

