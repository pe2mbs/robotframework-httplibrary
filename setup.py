#!/usr/bin/env python

from distutils.core import setup

CLASSIFIERS = """
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]

from os.path import join, dirname
long_description = open(join(dirname(__file__), 'README.rst',)).read()
filename = 'src/HttpLibrary/version.py'
exec( open( filename ).read() )

setup(
    name='robotframework-httplibrary',
    version = __version__,
    description='Robot Framework keywords for HTTP requests',
    long_description=long_description,
    author='Filip Noetzel',
    author_email='filip+rfhttplibrary@j03.de',
    url='https://github.com/peritus/robotframework-httplibrary',
    license='Beerware',
    keywords='robotframework testing testautomation web http webtest',
    platforms='any',
    zip_safe=False,
    classifiers=CLASSIFIERS.splitlines(),
    package_dir={'': 'src'},
    install_requires=['robotframework', 'webtest>=2.0', 'jsonpatch',
                      'jsonpointer'],
    packages=['HttpLibrary']
)
