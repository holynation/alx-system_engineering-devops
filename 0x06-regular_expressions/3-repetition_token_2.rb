#!/usr/bin/env ruby
# This is a script that must match the pattern
# "hbn,hbtn, hbttn, hbtttn, hbttttn" not "hbn"

puts ARGV[0].scan(/hbt+n/).join
