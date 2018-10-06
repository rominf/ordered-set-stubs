from setuptools import setup
import sys


if sys.version_info < (2, 7, 0) or (3, 0, 0) <= sys.version_info < (3, 5, 0):
    sys.stderr.write('ERROR: You need Python 2.7 or 3.5+ to install the typing package.\n')
    exit(1)


DESCRIPTION = open('README.md').read()

setup(
    name="ordered-set-stubs",
    version='1.0.0',
    maintainer='Roman Inflianskas',
    maintainer_email='infroma@gmail.com',
    license="LICENSE",
    url='https://github.com/rominf/ordered_set-stubs',
    platforms=["any"],
    description="Stubs with type annotations for ordered-set Python library",
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    package_data={'ordered_set-stubs': ['__init__.pyi']},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
