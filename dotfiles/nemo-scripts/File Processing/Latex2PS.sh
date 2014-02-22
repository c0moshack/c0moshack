#!/bin/bash
# Bubba's improved nautilus latex2ps script
# V3 - bibtex and re-run for references
# phurd@ualberta.ca

cd $NAUTILUS_SCRIPT_CURRENT_URI

BASENAME=`echo $1 | cut -d"." -f1`

TMPFILE=`echo ~/.latex2ps.$RANDOM.temp`

# something is stripping off a backslashes throughout when posting to
# the g-scripts-devel list... should be two before nonstopmode and two
# before input
latex \\nonstopmode\\input $@ > $TMPFILE

BIBTEX_PRESENT=`grep -c "bibliographystyle" $@`

if [ $BIBTEX_PRESENT ]
then
        bibtex  $BASENAME >> $TMPFILE
        latex \\nonstopmode\\input $@ >> $TMPFILE
fi

UNDEFINED_REFERENCE=`grep -c "undefined references" $TMPFILE`

UNDEFINED_CITATION=`grep -c "undefined citations" $TMPFILE`

UNDEFINED=$UNDEFINED_REFERENCE+$UNDEFINED_CITATION

if [ $UNDEFINED ]
then
        latex \\nonstopmode\\input $@ >> $TMPFILE
fi

BASENAME=`echo $1 | cut -d"." -f1`

dvips $BASENAME -o $BASENAME.ps

gless $TMPFILE
rm $TMPFILE
