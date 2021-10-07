#!/usr/bin/perl
# Usage: ./script.pl <regex-pattern> <file-name>

my $pattern = shift @ARGV;
my $regex;
my $file_name = shift @ARGV;

unless (defined $pattern) {
    die "Error: no regex-pattern was provided\nUsage: $0 <regex-pattern> <file-name>\n";
}

eval {$regex = qr/$pattern/};
if ($@) {
    die "Error: invalid regex pattern:\n $@";
    }

unless (defined $file_name) {
    die "Error: no file name was provided\nUsage: $0 <regex-pattern> <file-name>\n";
}

unless (-e $file_name) {
    die "Error: file $file_name doesn't exist\nUsage: $0 <regex-pattern> <file-name>\n";
}

while (<>) {
    print if /$regex/;
}
