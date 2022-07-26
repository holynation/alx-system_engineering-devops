#!/usr/bin/env ruby
# This is a script that must match the pattern
# "hbn,hbon,hbtn, hbtttttn" not "hbon"

puts ARGV[0].scan(/hb*n/).join
