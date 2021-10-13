#!/usr/bin/perl
# Usage: ./script.pl [filename]

# define line number to print
my $n_line_to_print = 10;

# loop of the lines of an input file
# $. is a variable holding current line number
while (<>) {
    if ($. == $n_line_to_print) {
        print;
        last;
    }
}
