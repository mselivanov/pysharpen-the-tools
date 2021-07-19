"""
Module for demonstrating working with files
"""

import datetime
from helpers.helpers import print_header
import shutil
from shutil import make_archive
import time

import os
from os import path, pathsep
from zipfile import ZipFile


TEST_FILE_PATH = path.realpath(path.expanduser('~/pyexample.txt'))


def file_example(file_path=TEST_FILE_PATH):
    print_header('Writing to pyexample.txt in a home directory')
    # Open file for writing; create if not exists
    f = open(file_path, 'w+')
    for i in range(10):
        f.write(f'Line number: {i}\n')
    f.close()

    # Open in an append mode
    f = open(file_path, 'a')
    for i in range(10):
        f.write(f'Line number: {i}\n')
    f.close()

    # Reading all content
    f = open(file_path, 'r')
    if f.mode == 'r':
        contents = f.read()
        print(contents)
        f.close()

    # Reading line by line
    f = open(file_path, 'r')
    if f.mode == 'r':
        fl = f.readlines()
        for line in fl:
            print(line.strip())
        f.close()


def file_attributes_example():
    print_header(header='File attributes examples')
    p = path.realpath(path.expanduser('~/pyexample.txt'))
    # Get modification time in seconds from Epoch, convert it to string
    t = time.ctime(path.getmtime(p))
    print(f'Modification time (ctime): {t}')
    t = datetime.datetime.fromtimestamp(path.getmtime(p))
    print(f'Modification time (datetime.fromtimestamp): {t}')


def shell_examples():
    print_header('Shell examples')
    src = TEST_FILE_PATH
    dst = TEST_FILE_PATH + '.bak'
    dst1 = TEST_FILE_PATH + '.bak1'
    # Copy file
    shutil.copy(src, dst)
    #Copy all file attributes
    shutil.copystat(src, dst)
    # Rename file
    root_dir, name = path.split(src)
    # new_name = root_dir + '/pyexample_new.txt'
    # if path.exists(new_name):
    #     os.remove(new_name)
    # os.rename(src, new_name)
    # Make zip archive
    make_archive(base_name='pytestarch', format='zip', root_dir=root_dir,
                 base_dir=path.realpath(path.expanduser('~/Documents')))


def zipfile_examples():
    print_header('zipfile examples')
    root_dir, fn = path.split(TEST_FILE_PATH)
    zip_path = root_dir + os.sep + 'pyexample2.zip' 
    with ZipFile(zip_path, 'w') as zf:
        zf.start_dir
        zf.write(TEST_FILE_PATH)
        zf.write(root_dir + os.sep + fn + '.bak')


def path_examples():
    print_header('Path examples')
    filepath = "~/pyexample.txt"
    # Expand shortcut to an abs path to a home dir
    filepath = path.expanduser(filepath)
    print(f'Path to pyexample: {filepath}')

    # Check if file exists
    print(f'Path {filepath} exists: {path.exists(filepath)}')
    print(f'Path {filepath} is a file: {path.isfile(filepath)}')
    print(f'Path {filepath} is a directory: {path.isdir(filepath)}')
    
    parent_dir = '..'
    print(f'Parent dir abs path: {path.abspath(parent_dir)}')

    # Print relative path 
    current_dir = path.realpath(path.normpath(path.curdir))
    print(f'Relative path to {filepath} from {current_dir}: {path.relpath(filepath)}')
    
    # Symlinks behaviour
    symlink_path = path.expanduser('~/.bashrc')
    print(f'Abspath to a symlink {symlink_path}: {path.abspath(symlink_path)}')
    print(f'Realpath to a symlink {symlink_path}: {path.abspath(symlink_path)}')



def main():
    file_example()
    path_examples()
    file_attributes_example()
    shell_examples()
    zipfile_examples()


if __name__ == '__main__':
    main()

