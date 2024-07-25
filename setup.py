# SPDX-FileCopyrightText: 2024 M5Stack Technology CO LTD
#
# SPDX-License-Identifier: MIT

import setuptools

AUTHOR = 'M5Stack Systems'
MAINTAINER = 'M5Stack'
EMAIL = 'tinyu@m5stack.com'

NAME = 'check-copyright'
SHORT_DESCRIPTION = 'The script for checking SPDX license header'
LICENSE = 'MIT'
URL = 'https://github.com/Tinyu-Zhao/check-copyright'
REQUIRES = [
    'comment_parser == 1.2.3',
    'thefuzz == 0.19.0',
    'thefuzz[speedup] == 0.19.0; sys_platform != "win32"',
    # don't depend on python-Levenshtein on Windows, as it requires Microsoft C++ Build Tools to install
    'pyyaml == 6.0.1',
    'pathspec == 0.9.0'
]

setuptools.setup(
    name=NAME,
    description=SHORT_DESCRIPTION,
    long_description_content_type='text/markdown',
    license=LICENSE,
    version='1.0.3',
    author=AUTHOR,
    maintainer=MAINTAINER,
    author_email=EMAIL,
    url=URL,
    install_requires=REQUIRES,
    py_modules=['check_copyright'],
    scripts=['check_copyright.py'],
    entry_points={'console_scripts': ['check-copyright=check_copyright:main']},
)
