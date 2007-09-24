#!/bin/sh

########################################
# error: prints an error and exits
#   msg: an error message
function error {
    echo "Error: $1" 1>&2
    exit 1
}

if [ -z $1 ] ; then error "missing plugin name"; fi

if [ -e $1 ] ; then error "plugin already exists"; fi

echo "creating $1"
mkdir $1

cd $1

echo "linking files"
ln -s ../common/COPYING  .
ln -s ../common/INSTALL  .
ln -s ../common/Makefile .

echo "creating empty files"
touch ChangeLog
touch NEWS
touch README
touch README
touch TODO
touch $1
chmod +x $1

echo $1 > NAME

echo "creating files"

echo "Matteo Corti <matteo.corti@id.ethz.ch>" > AUTHORS
echo "0.9" > VERSION
cp ../common/template.spec $NAME.spec
sed -i -e "s/@VERSION@/0.9/" $NAME.spec
sed -i -e "s/@NAME@/$NAME/"  $NAME.spec
