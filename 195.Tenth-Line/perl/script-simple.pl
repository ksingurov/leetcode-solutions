#!/usr/bin/perl
# Usage: ./script.pl [filename]

# loop of the lines of an input file
# $. is a variable holding current line number
while (<>) {
    if ($. == 10) {
        print;
        last;
    }
}
