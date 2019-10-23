#!/usr/bin/env bash

hex=$1 # assign first arg to hex
hex=${hex:1:8} # remove hash from the beggining
alpha=$((16#${hex:6:2})) # perform operation: 16#"last two letters", e.g. 16#FF returns 255
LC_NUMERIC=C
printf "rgb(%d,%d,%d,%.2f)\n" 0x${hex:0:2} 0x${hex:2:2} 0x${hex:4:2} $(bc <<< "scale=3;${alpha}/255")
# 0x${hex:0:2} returns first 0x"2 letters", e.g. 0xFF, when passed to %d it gets converted to decimal
# $(...) means execute the command in the parentheses in a subshell and return its stdout.
# <<< The strings is expanded and supplied to the command on its standard input.