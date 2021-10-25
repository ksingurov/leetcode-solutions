#!/usr/bin/perl
# Usage: ./script.pl <line-number> <file-name>

# get line number and file name from the command line input
# ARGV is an array which stores parameters passed to the script
# shift @ARGV: removes and returns the first command-line argument
my $n_line_to_print = shift @ARGV;
my $file_name = shift @ARGV;

# checks if line number was passed as a parameter
# also dies if just file-name was provided as the first parameter
unless (defined $n_line_to_print && $n_line_to_print =~ /^\d+$/) {
    die "Error: no line number was provided.\nUsage: $0 <line-number> <filename>\n";
}
unless (defined $file_name) {
    die "Error: no file name was provided.\nUsage: $0 <line-number> <filename>\n"
}

# loop of the lines of an input file
# $. is a variable holding current line number
# by default while (<>) iterates over @ARGV, at this moment it should be empty
# the next line opens $file_name for reading (<), stores a filehandle in $fh
open(my $fh, '<', $file_name) or die "Error: file '$file_name' doesn't exist.";
# iterate over an opened file
while (<$fh>) {
    if ($. == $n_line_to_print) {
        print; # when no argement is passed to print, it print $_ which is current line
        last;
    }
}
close $fh;
