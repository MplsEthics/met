#!/usr/bin/perl

# Copyright 2010 John J. Trammell.
#
# This file is part of the Mpls-ethics software package.  Mpls-ethics is free
# software: you can redistribute it and/or modify it under the terms of the GNU
# General Public License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version.
#
# Mpls-ethics is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License
# along with Mpls-ethics.  If not, see <http://www.gnu.org/licenses/>.

use strict;
use warnings FATAL => 'all';

for my $file (@ARGV) {
    if (-e $file) {
        if (not has_gpl($file)) {
            print "file '$file' lacks GPL boilerplate\n";
        }
    }
    else {
        die "file '$file' does not exist\n";
    }
}

sub has_gpl {
    my $file = shift;
    my $slurp = do { local(@ARGV,$/) = $file; <> } || q();
    $slurp =~ s{#}{ }g;
    $slurp =~ s{\s+}{ }g;
    my @strings = (
        "Copyright 2010 John J. Trammell.",
        "This file is part of the Mpls-ethics software package.",
        "Mpls-ethics is free software: you can redistribute it and/or",
        "Mpls-ethics is distributed in the hope that it will be useful",
        "See the GNU General Public License for more details.",
        "You should have received a copy of the GNU General Public",
        "If not, see <http://www.gnu.org/licenses/>.",
    );
    for my $string (@strings) {
        return undef if index($slurp,$string) < 0;
    }
    return 1;
}
