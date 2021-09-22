#!/usr/bin/perl
# Usage: ./script.pl <file-name>

my $pattern = '^(\(\d{3}\) |\d{3}-)\d{3}-\d{4}$';

while (<>) {
    print if /$pattern/;
}
