import re
import os
import glob
import shutil

ARCHIVE_DIR = './legacy'
EXCLUDING_FILE = ['./convert.py', './make.bat', './Makefile',
                  './build', './source', './LICENSE', ARCHIVE_DIR]
EXCLUDING_MD_FILE = ['./README.md', './00_Zsh-开发指南（目录）.md']

if not os.path.exists(ARCHIVE_DIR):
    os.makedirs(ARCHIVE_DIR)
legacy_files = list(set(glob.glob('./*')) - set(EXCLUDING_FILE))
content_files = list(set(glob.glob('./*.md')) - set(EXCLUDING_MD_FILE))

for src in legacy_files:
    if src in content_files:
        chapter = os.path.basename(src)
        ch_index = chapter[0:2]
        ch_name = re.findall(r'（(第\S*篇-\S*)）', chapter)[0]
        with open(src, 'r') as f:
            content = f.readlines()
            content[0] = f'## {ch_name}'
        with open(f'./source/ch{ch_index}.md', 'w') as f:
            f.writelines(content)
    dst = os.path.join(ARCHIVE_DIR, os.path.basename(src))
    shutil.move(src, dst)
