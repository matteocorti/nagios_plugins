#!/usr/bin/perl

#

#

# check_cpu.pl [warn] [critical]

# Nagios script to get the cpu usage from procinfo or sar

#

# Changes and Modification

# ========================

# 07-Oct-2003  - Benjamin Jakubowski

#   Adding check sar or procinfo command

# 07-Sept-2002 -  Benjamin Jakubowski

#   Created from check_cpu.pl for LDAP Serveur use 100% CPU



sub print_help ();

sub print_usage ();

$PROGNAME = "check_cpu";

$commande_sar=1;

$commande_procinfo=1;

$STATE_CRITICAL = 2;

$STATE_OK = 0;

$STATE_WARNING = 1;



if (! open(COM,'sar|') )

{

        $error_sar = "Problème à l'ouverture de la commande sar";

        $commande_sar=0;

}

else

{

        close COM;

}



if (! open(COM,'procinfo|') )

{

        $error_procinfo="Problème à l'ouverture de la commande procinfo";

        $commande_procinfo=0;

}

else

{

       close COM;

}



if  ( @ARGV[0] eq "" || @ARGV[1] eq "" )

{

    print_usage ();

    exit 0;

}

$warning = @ARGV[0];

$critik = @ARGV[1];

if ( $commande_sar eq 0 && $commande_procinfo eq 0 )

{

    printf "$error_sar \n$error_procinfo\n";

    exit

    ;;

}



if  (  $commande_sar eq 1 && $commande_procinfo eq 1 )

{

    $commande_sar=0;

}

if ( $commande_procinfo eq 1 )

{

        @toto = `procinfo | grep idle | awk \'{print \$5}\'`;

        @cpu = 100-@toto[0];

}

if ( $commande_sar eq 1 )

{

        @line = `/usr/bin/sar | /usr/bin/tail -n 2 | /usr/bin/head -n 1 | /bin/sed 's/\ \ */ /g'`;

        @data = split(/ /, @line[0]);

        @cpu = (@data[2] + 0.5) +(@data[3])+(@data[2])+(@data[4]+0.5);

        @toto = 100-@cpu[0];

}



if ( $cpu[0] >= $critik )

{

        printf ("CRITICAL : use %3.2f%",@cpu);

        printf " idle : @toto%";

        exit $STATE_CRITICAL

        ;;

}



if (($cpu[0] < $critik)&&($cpu[0] < $warning))

{

        printf ("OK : use %3.2f%",@cpu);

        printf " idle : @toto%\n";

        exit $STATE_OK

        ;;

}

if (($cpu[0] >= $warning)&&($cpu[0] < $critik))

{

        printf ("WARNING : use %3.2f%",@cpu);

        printf " idle : @toto%\n";

        exit $STATE_WARNING

        ;;

}





sub print_help ()

{

        print($PROGNAME,': 1.1');

        printf "\n";

        print "Copyright (c) 2002 Benjamin Jakubowski \

Perl Check CPU Usage plugin for Nagios \

";

}

sub print_usage ()

{

print_help();



printf "\n\nUsage : check_cpu.pl [warn] [critical]\n

warn, INTEGER

   Number of CPU Space at wich a warning will be generated ( No Default )

critical, INTEGER

   Number of CPU Space at wich a critical will be generated ( No Default )\n";

}


