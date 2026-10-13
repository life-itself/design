#!/bin/zsh
# usage: mask.sh SRC OUTMASK LOW HIGH  — flat-field the paper, then alpha = ink density
set -e
SRC=$1; OUT=$2; LO=${3:-8%}; HI=${4:-80%}
W=$(dirname $OUT)
magick $SRC -channel R -separate +channel -strip $W/r.png 2>/dev/null
# paper estimate: local max (removes ink) then smooth
magick $W/r.png -statistic Maximum 31x31 -blur 0x20 $W/bg.png
# ratio r/bg -> paper = white; invert to ink density
magick $W/r.png $W/bg.png -compose DivideSrc -composite -negate -level $LO,$HI $OUT
