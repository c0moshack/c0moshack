#!/bin/bash
IFS='
'
PDFARGUMENTS=""
fpaths=`echo "$NAUTILUS_SCRIPT_SELECTED_FILE_PATHS" | sort`
for file in $fpaths
do
  if [ -f "$file" ]; then
	base=${file%.*}
	ext=${file##*.}
	if [ "$ext" == "pdf" ]; then
	    PDFARGUMENTS="$PDFARGUMENTS \"$file\""
	    pdfdir=`dirname "$file"`
	fi
  fi
done
if [ -n "$PDFARGUMENTS" ]; then
    cd "$pdfdir"
    eval /usr/bin/pdfjoin $PDFARGUMENTS
fi

