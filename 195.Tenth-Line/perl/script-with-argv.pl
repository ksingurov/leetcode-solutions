#!/usr/bin/perl
# Usage: ./script.pl [line-number] [file-name]

# get line number from the command line input
# ARGV is an array which stores parameters passed to the script
my $n_line_to_print = $ARGV[0];

# loop of the lines of an input file
# $. is a variable holding current line number
while (<>) {
    if ($. == $n_line_to_print) {
        print;
        last;
    }
}
