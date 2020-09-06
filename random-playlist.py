#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Version: 0.3

import os
from random import randrange
import argparse

allfiles = []
data = []
output = []

########################################
########### Argument parser ############
########################################

parser = argparse.ArgumentParser()
parser.add_argument('sourcedir', help='Source directory')

parser.add_argument('-p', '--playlist-file', default='/data/playlist/random',
		    action='store', dest='plstname',
                    help='Destination file')

parser.add_argument('-n',type=int,
		    action='store', default=50,
                    dest='trackcount',
                    help='Number of tracks to generate')

parser.add_argument('-d', '--debug',
		    action='store_true', default=False,
                    dest='deb',
                    help='Write parsed items')

parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.3')

results = parser.parse_args()

########################################
####### Read all files to array ########
########################################

for r, d, f in os.walk(results.sourcedir):
 for file in f:
  if file.endswith('.flac') or file.endswith('.dsf'):
   r=(r.replace('/mnt/', '', 1))
   allfiles.append(os.path.join(r, file))

########################################
############ Random array ##############
########################################

for rand in range(results.trackcount):
 data.append(allfiles[randrange(len(allfiles))])

########################################
########## Write volumio file ##########
########################################

o = open(results.plstname, encoding='utf-8', mode='w')
o.write('[')

for pth in data:
 if results.deb:
  print("Path: " + pth)
 artist = pth.split('/')[2]
 if results.deb:
  print("Artist: " + artist)
 if '/' in pth and pth.count('/') > 2:
  album = pth.split('/')[3]
  if ' - ' in album and album.count(' - ') > 0:
   album = album.split(' - ')[1]
   album = album.split('(')[0]
 else:
  album=''
 if results.deb:
  print("Album: " + album)
 title = pth.split('/')[-1]
 title = title.split('-')[-1]
 title = title.split('.')[-2]
 if results.deb:
  print("Title: " + title)
  print("-------")
 output.append('{"service":"mpd","title":"' + title.strip() + '","artist":"' + artist.strip() + '","album":"' + album.strip() + '","uri":"' + pth.strip() + '"}')

o.write(','.join(output))
o.write(']')
o.close()
print('Successfully added to ' + results.plstname)
