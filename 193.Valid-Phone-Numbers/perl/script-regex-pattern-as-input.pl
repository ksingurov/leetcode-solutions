#!/usr/bin/perl
# Usage: ./script.pl <pattern> <file-name>

# my $pattern = '^(\(\d{3}\) |\d{3}-)\d{3}-\d{4}$';
my $pattern = shift @ARGV;

while (<>) {
    print if /$pattern/;
}
