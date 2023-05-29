import shutil
import os


SPECIAL_LOCATIONS = {
}
IGNORE_FILES = [
    'symlink.py',
    '.git',
    '.gitignore',
    '.davmailbackup'
]

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
