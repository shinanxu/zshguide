import re
import os
import glob
import shutil

ARCHIVE_DIR = './legacy'
CONTENT_DIR = './source/content'
EXCLUDING_FILE = ['./convert.py', './make.bat', './Makefile',
                  './build', './source', './LICENSE', './README.md', './legacy']
EXCLUDING_MD_FILE = ['./legacy/README.md', './legacy/00_Zsh-开发指南（目录）.md']

toctree = []
content_files = list(set(glob.glob(f'{ARCHIVE_DIR}/*.md')) - set(EXCLUDING_MD_FILE))
for i in content_files:
    chapter = os.path.basename(i)
    ch_index = chapter[0:2]
    ch_name = ch_index + ' ' +re.findall(r'（第\S*篇-(\S*)）', chapter)[0]
    ch_name = ch_name.replace('-', '').lower().replace('tcp', 'TCP').replace('[]', '[ ]')
    with open(i, 'r') as f:
        content = f.readlines()
        content[0] = f'## {ch_name}'
    with open(f'{CONTENT_DIR}/ch{ch_index}.md', 'w') as f:
        f.writelines(content)
    toctree.append(f'[{ch_name}]({CONTENT_DIR}/ch{ch_index}.md)\n\n')
toctree.sort()
with open(f'README.md', 'r') as f:
        readme = f.readlines()
readme = readme[0:readme.index('## 目录\n')+2]
readme.extend(toctree)
with open(f'README.md', 'w') as f:
    f.writelines(readme)
