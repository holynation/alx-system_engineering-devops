#!/usr/bin/env ruby
# This is a script that must match the pattern
# "hbn,hbtn,hbttn,hbtttn, hbttttn, hbtttttn"

puts ARGV[0].scan(/hb{2,5}n/).join
