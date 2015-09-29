# -*- coding: utf-8 -*-

"""setup.py: setuptools control."""

import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('pwman/pwman.py').read(),
    re.M
).group(1)

with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name = "py-pwman",
    packages = ["pwman"],
    package_data={"pwman": ["locale/*/LC_MESSAGES/*"]},
    entry_points = {
        "console_scripts": ['pwman = pwman.pwman:main']
        },
    version = version,
    description = "Python command line password manager.",
    long_description = long_descr,
    author = "Oskar Jauch",
    author_email = "oskar.jauch@gmail.com",
    url = "https://github.com/ossi96/py-pwman",
    install_requires = [
        'pyperclip',
    ])
