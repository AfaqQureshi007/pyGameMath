import os
from setuptools import setup, find_packages
setup(
  name = 'gem',
  packages = find_packages(where="gem"),
  package_dir = {'':'gem'},
  version = 'v0.1.2',
  description = 'Math library for game programming in python. ',
  author = 'Alex Marinescu',
  author_email = 'ale632007@gmail.com',
  license='BSD 2-Clause',
  url = 'https://github.com/explosiveduck/pyGameMath',
  download_url = 'https://github.com/explosiveduck/pyGameMath/releases',
  install_requires=['six'],
  keywords = ['math', 'game', 'library'],
  classifiers = [
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: Scientific/Engineering :: Mathematics',
            'Topic :: Software Development :: Libraries',
            'License :: OSI Approved :: BSD License',

            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.0',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            ],
)