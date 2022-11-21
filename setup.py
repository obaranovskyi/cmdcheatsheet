from setuptools import setup, find_packages
import codecs
import os

curr_location = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(curr_location, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.9'
DESCRIPTION = 'Terminal commands cheat sheet helper'

setup(
    name="cmdcheatsheet",
    version=VERSION,
    author="obaranovskyi (Oleh Baranovskyi)",
    author_email="<oleh.baranovskyi.dev.acc@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/obaranovskyi/cmdcheatsheet",
    packages=find_packages(),
    install_requires=['rich'],
    keywords=['python', 'command', 'terminal', 'console', 'utilities'],
    entry_points={
        'console_scripts': [
            'cmdcheatsheet=cmdcheatsheet.cmdcheatsheet:main'
        ]
    },
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Topic :: Utilities"
    ]
)
