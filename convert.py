import os
import glob
import shutil

ARCHIVE_DIR = './legacy'
EXCLUDING_FILE = ['./convert.py', './LICENSE', ARCHIVE_DIR]
EXCLUDING_MD_FILE = ['./README.md', '00_Zsh-开发指南（目录）.md']

if not os.path.exists(ARCHIVE_DIR):
    os.makedirs(ARCHIVE_DIR)
legacy_files = list(set(glob.glob(os.path.join('./*'))) - set(EXCLUDING_FILE))
content_files = list(set(glob.glob(os.path.join('./*.md'))) - set(EXCLUDING_MD_FILE))

for src in legacy_files:
    dst = os.path.join(ARCHIVE_DIR, os.path.basename(src))
    shutil.move(src, dst)