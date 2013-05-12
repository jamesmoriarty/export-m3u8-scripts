#!/usr/bin/env python
# ./export_m3u8.py path/to/playlist.m3u8

import sys
import os
import shutil

if not os.path.exists(sys.argv[1]):
  print "m3u8 file not found!"
  print "usage: %s path/to/playlist.m3u8" % sys.argv[0]
  sys.exit(1)

playlist_path = sys.argv[1]
playlist_name = os.path.splitext(os.path.basename(playlist_path))[0]

folder_path   = os.path.join(os.getcwd(), playlist_name)
if not os.path.exists(folder_path):
  os.makedirs(folder_path)

playlist_file = open(playlist_path).read().split("\r")
for index, file_path in enumerate(playlist_file):
  if not os.path.exists(file_path):
    continue

  file_name = "%d %s " % (index, os.path.basename(file_path))
  print "Copying... %s" % file_name
  shutil.copy(file_path, os.path.join(folder_path, file_name))

print "Finished."
