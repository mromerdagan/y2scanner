#! /usr/bin/python

from distutils.core import setup
import glob


setup(name='y2scanner',
    version='1.0',
    maintainer='Omer Dagan',
    maintainer_email='mr.omer.dagan@gmail.com',
    packages=["y2scanner"],
    package_dir={'': "python"},
    data_files=[
    	('/usr/bin', glob.glob('tree/usr/bin/*')),
    ],
)
