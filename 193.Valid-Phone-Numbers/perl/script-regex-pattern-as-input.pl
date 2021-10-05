#!/usr/bin/perl
# Usage: ./script.pl <regex-pattern> <file-name>

my $pattern = shift @ARGV;
my $regex;

# unless (defined $pattern) {
#     die "Error: regex-pattern was not provided\nUsage: $0 <regex-pattern> <file-name>\n";
# }

eval {$regex = qr/$pattern/};
if ($@) {
    die "Error: invalid regex pattern:\n $@";
    }

# print "$pattern\n";
# print $regex;

while (<>) {
    # print
    print if /$regex/;
}
