#!/usr/bin/perl
# Usage: ./script.pl [filename]

# loop of the lines of an input file
# $. is a variable holding current line number
while (<>) {
    print if $. == 10;
    last if $. == 10; # stops after tenth line
}
