#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import shutil

if len(sys.argv) == 1 or sys.argv[1] not in ('--install', '--uninstall', '--list'):
	print('Opsss! This is not a valid command. Should be `--install`, `--uninstall` or `--list`.')
	exit(0)

command = sys.argv[1]

print('\n')

curr_dir = dir_path = os.path.dirname(os.path.realpath(__file__))
themes_dir = curr_dir + "/themes"
print('Themes folder:\n%s\n' % (themes_dir))

dest_dir = os.path.expandvars("$HOME/Library/Developer/Xcode/UserData/FontAndColorThemes")
print('Destination folder:\n%s' % dest_dir)

# Check and create themes folder if needed
if not os.path.exists(dest_dir):
	print('Xcode themes directory not found. Creating...')
	os.makedirs(dest_dir)

if command == '--list':
	print('\nFound themes: \n')

for theme_file in os.listdir(themes_dir):
	if theme_file.endswith(".xccolortheme"):
		if command == '--install':
			print('→ Installing theme: %s' % theme_file)
			#os.symlink(themes_dir + '/' + theme_file, dest_dir + '/' + theme_file)
			shutil.copyfile(themes_dir + '/' + theme_file, dest_dir + '/' + theme_file)
		elif command == '--uninstall':
			print('→ Uninstalling theme: %s' % theme_file)
			#os.unlink(dest_dir + '/' + theme_file)
			os.remove(dest_dir + '/' + theme_file)
		elif command == '--list':
			print('\t → ' + theme_file)

print('\n')