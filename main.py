#! /usr/bin/python

import csv
import os

import csv
with open('AXA_members_1.csv', 'rb') as csvfile:
  csvdata = csv.reader(csvfile, delimiter=',', quotechar='|')
  for row in csvdata:
    print "Creating image for " + row[0]  + ", id:" +row[1] 
    command = "convert AXA_jasenkirja_empty.jpg -stroke \'#0000\' -fill black -font \'Kauno\' -pointsize 72 -gravity center -draw \'text 0,230 \"" + row[0] + "\"' -draw \'text 0,700 \"~ " + row[1] + " ~\"\' out/" + row[1] +".jpg"
    os.system(command)
    print row[1] + " is done"
