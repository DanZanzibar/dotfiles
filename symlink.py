import shutil
import os
import sys
import argparse
import tomllib


if len(sys.argv) > 1:
    file_dir = os.path.expanduser(sys.argv[1])
else:
    file_dir = os.getcwd()

with open(file_dir, 'rb') as file:
    toml_data = tomllib.load(file)

toml_general = toml_data['general']

parser = argparse.ArgumentParser(
    description='Symlink files in a directory to another directory.')
parser.add_argument('file_dir', default=os.getcwd())
parser.add_argument('symlink_dir', default=toml_general['symlink_dir'])

files_dir_path = os.path.expanduser(sys.argv[1])
files_dir = [x for x in files_dir_path.split('/') if x != ''][-1]

backup_dir = toml_general.get('backup-dir', files_dir_path)

ignore_files = ['.git', '.gitignore']
if 'ignore-files' in toml_general:
    ignore_files += toml_general['ignore-files']

special_locations = {}
if 'special-locations' in toml_data:
    toml_special = toml_data['special-locations']
    special_locations = {file: os.path.expanduser(address)
                      for file, address in toml_special.items()}

# Need to get SYMLINKS_DIR from argparse or TOML.

files = os.listdir(dir)
files = {name: f'/home/zan/{name}' for name in files}

for name in ignore_files:
    del files[name]

files.update(SPECIAL_LOCATIONS)

if not os.path.exists(old_dir):
    os.makedirs(old_dir)
    print('making old_dotfiles directory')

for file, address in files.items():
    if not os.path.islink(address):
        if os.path.exists(address):
            shutil.move(address, old_dir + file)
            print(f'archiving old {file} file')
        os.symlink(dir + file, address)
        print(f'{file} is now symlinked')
    else:
        print(f'{file} already symlinked')
