#!/usr/bin/env ruby
# This is a script that must match the pattern "htn,hbtn,htn,hbbtn,hbbbtn"

puts ARGV[0].scan(/h?tn/).join
