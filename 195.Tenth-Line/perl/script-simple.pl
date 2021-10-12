#!/usr/bin/perl

while (<>) {
    print if $. == 10;
}
