import shutil
import os
import sys
import tomllib


CONFIG_PATH = os.path.expanduser(sys.argv[1])
CONFIG_DIR = [x for x in CONFIG_PATH.split('/') if x != ''][-1]

with open(CONFIG_PATH, 'rb') as file:
    TOML_DATA = tomllib.load(file)

if len(sys.argv) == 3:
    SYMLINK_DIR = sys.argv[2]
else:
    SYMLINK_DIR = TOML_DATA['symlink-dir']

SPECIAL_LOCATIONS = {}

IGNORE_FILES = ['.git', '.gitignore']


# with open
# Needed in the config file:
# File to put symlinks
# Special ignore files
# Special location symlinks
# Where to backup existing files

dir = '/home/zan/dotfiles/'
old_dir = '/home/zan/old-dotfiles/'

files = os.listdir(dir)
files = {name: f'/home/zan/{name}' for name in files}

for name in IGNORE_FILES:
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
