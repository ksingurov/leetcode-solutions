#!/usr/bin/perl

while (<>) {
    print if /^(\(\d{3}\) |\d{3}-)\d{3}-\d{4}$/;
}
