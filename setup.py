#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='make_qt_ui',
    packages=['make_qt_ui'],
    entry_points = {
        'console_scripts': [
            'make_pyqt_ui = make_qt_ui:make_pyqt',
            'make_pyside_ui = make_qt_ui:make_pyside',
        ],
    },
    version='0.1.0',
    description='Scripts to simplify conversion of *.ui and *.qrc files to Python',
    author='Roman Haritonov',
    author_email='reclosedev@gmail.com',
    url='https://github.com/reclosedev/make_qt_ui',
    keywords=['qt', 'pyside', 'pyqt'],
    license='BSD License',
    include_package_data=True,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
#        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
#        'Programming Language :: Python :: 3.0',
#        'Programming Language :: Python :: 3.1',
#        'Programming Language :: Python :: 3.2',
        ],
    long_description=open('README.rst').read(),
)
