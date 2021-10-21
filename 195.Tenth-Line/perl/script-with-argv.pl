#!/usr/bin/perl
# Usage: ./script.pl <line-number> <file-name>

# get line number from the command line input
# ARGV is an array which stores parameters passed to the script
# shift @ARGV: removes and returns the first command-line argument
my $n_line_to_print = shift @ARGV;

# checks if line number was passed as a parameter
# also dies if just file-name was provided as the first parameter
unless (defined $n_line_to_print && $n_line_to_print =~ /^\d+$/) {
    die "Error: no line number was provided.\nUsage: $0 <line-number> <filename>\n";
}

# loop of the lines of an input file
# $. is a variable holding current line number
while (<>) {
    if ($. == $n_line_to_print) {
        print;
        last;
    }
}
