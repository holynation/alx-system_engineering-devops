#!/usr/bin/env ruby
# This is a script that must match the patttern a string
# that starts with "h" and ends with "n" with single char in between

puts ARGV[0].scan(/h.n/).join
