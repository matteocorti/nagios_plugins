#!/bin/sh

# rm -rf rpms
mkdir -p rpms

for d in check_* ; do
    
    echo "------------------------------------------------------------------------------"
    echo "Building $d"
    
    tarball=
    
    cd $d
    
    echo "- updating"
    svn up > /dev/null
    
    if [ -f Makefile.PL ] ; then
        
        # perl

        echo "- generating makefile"
        perl Makefile.PL > /dev/null 2>&1
        if [ $? != 0 ] ; then
            perl Makefile.PL
            exit;
        fi
        
        echo "- building"
        make > /dev/null
        if [ $? != 0 ] ; then
            exit;
        fi
        make manifest > /dev/null
        
        echo "- packaging"
        tarball=$(make dist | grep 'gzip' | sed -e "s/gzip\ --best\ //")
        if [ $? != 0 ] ; then
            exit;
        fi
        tarball="${tarball}.gz"

    else
    
        echo "- packaging"
        make dist > /dev/null
        if [ $? != 0 ] ; then
            exit;
        fi
        tarball=${d}-$(cat VERSION).tar.gz

    fi;

    if [ ! -f $tarball ] ; then
        echo "Error: ${tarball} not found";
        make dist
        exit
    fi

    if [ -f $d.spec ] ; then

        echo "- building RPMs"

        rpms=$(rpmbuild -ta $tarball 2>&1 | grep ^Wrote: | sed -e "s/^Wrote:\ //")
        
        if [ -z "${rpms}" ] ; then
            rpmbuild -ta $tarball
            exit;
        fi    
        
        echo "- copying"
        cp $rpms ../rpms
        if [ $? != 0 ] ; then
            exit;
        fi

    fi

    cd ..

done

