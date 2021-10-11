#!/usr/bin/perl
# Usage: ./script.pl <regex-pattern> <file-name>

# get pattern and file name from the command line input
my $pattern = shift @ARGV;
my $file_name = shift @ARGV;

# check that pattern is passed as a parameter
unless (defined $pattern) {
    die "Error: no regex-pattern was provided\nUsage: $0 <regex-pattern> <file-name>\n";
}

# check that pattern is a valid regex
# $@ is a variable which holds the error message from the last eval
# if $@ is empty then pattern is a valid regex pattern
my $regex;
eval {$regex = qr/$pattern/};
if ($@) {
    die "Error: invalid regex pattern:\n $@";
    }

# check that file name is passed as a pareameter
unless (defined $file_name) {
    die "Error: no file name was provided\nUsage: $0 <regex-pattern> <file-name>\n";
}

# loop of the lines of an input file
# $. is a variable holding current line number
# by default while (<>) iterates over @ARGV, at this moment it should be empty
# the next line opens $file_name for reading (<), stores a filehandle in $fh
open(my $fh, '<', $file_name) or die "Error: file '$file_name' doesn't exist.";
# iterate over an opened file
while (<$fh>) {
    print if /$regex/; # when no argement is passed to print, $_ is used
}
close $fh;
