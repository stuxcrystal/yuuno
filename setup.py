#!/usr/bin/env python
import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    if os.path.exists("README.rst"):
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    return ""

setup(
    name = "yuuno",
    version = "0.4.0",
    author = "StuxCrystal",
    author_email = "stuxcrystal@encode.moe",
    description = "Glue for jupyter and vapoursynth",
    license = "MIT",
    keywords = "vapoursynth frameserver jupyter ipython",
    url = "https://github.com/stuxcrystal/yuuno",

    packages=find_packages(),
    include_package_data=True,
    package_data={
        'yuuno': ['data/*.icc', 'data/widgets/*.html'],
    },

    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 4 - Beta",

        "License :: OSI Approved :: MIT License",
        "Environment :: Web Environment",

        "Topic :: Utilities",

        "Topic :: Multimedia :: Video",
        "Topic :: Multimedia :: Video :: Conversion",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: 3 :: Only",
        "Framework :: IPython"
    ],

    install_requires=[
        'notebook', 'Pillow', "ipywidgets", 'setuptools-git'
    ]
)
