import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist --formats=gztar upload')
    sys.exit()

version = '0.1.0'
requires = ['Pillow']

with open('README.md') as f:
    readme = f.read()
with open('LICENSE') as f:
    license = f.read()

setup(
    name='dronemapp-gpsimage',
    version=version,
    description="Retrieves GPS data from geo-referenced images",
    long_description=readme,
    author='Cléber Zavadniak',
    author_email='cleberman@gmail.com',
    url='https://github.com/Dronemapp/gpsimage',
    license=license,
    packages=['gpsimage'],
    package_data={'': ['LICENSE', 'README.md']},
    package_dir={'gpsimage': 'gpsimage'},
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    keywords='gps image exif lat lng georeferenced geo',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),
)
