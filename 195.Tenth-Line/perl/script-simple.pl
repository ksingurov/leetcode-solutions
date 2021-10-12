#!/usr/bin/perl

# loop of the lines of an input file
# $. is a variable holding current line number
while (<>) {
    print if $. == 10;
}
