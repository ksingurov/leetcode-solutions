#!/usr/bin/perl
# Usage: ./script.pl <file-name>

my $pattern = shift @ARGV;

while (<>) {
    print if /$pattern/;
}
