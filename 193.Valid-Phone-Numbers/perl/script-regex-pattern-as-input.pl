#!/usr/bin/perl
# Usage: ./script.pl <regex-pattern> <file-name>

my $pattern = shift @ARGV;
my $regex;
eval {$regex = qr/$pattern/};
if ($@) {
    die "Invalid regex pattern: $@";
    }

# print "$pattern\n";
# print $regex;

while (<>) {
    print if /$regex/;
}
