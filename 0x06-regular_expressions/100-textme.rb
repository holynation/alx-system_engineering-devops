#!/usr/bin/env ruby
# This script should parse the logfile with the output
# [sender],[receiver],[flags]

puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(",")
