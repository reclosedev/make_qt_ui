make_qt_ui
----------

Simplifies conversion of \*.ui and \*.qrc files from PySide/PyQt to Python
on \*nix and Windows.

Installation
------------

If you have pip_ installed::

    $ pip install make_qt_ui
    
Else::

    $ python setup.py install

.. _pip: http://www.pip-installer.org/

Usage
-----

If you want to convert all \*.ui and \*.qrc files in some directory, type in console

- for PyQt::

    $ make_pyqt_ui path_with_ui_and_qrc_files another_path
    
- for PySide::

    $ make_pyside_ui path1 path2
    
Also `make_qt_ui` can constantly convert changed files in directory::

    $ make_pyqt_ui --watch some_directory --interval 5

When `make_pyqt_ui` or `make_pyside_ui` launched without pointing to target
directory it will try to convert files in current `'./'` and `'./ui'` directories. 

Other available options::
    
    $ make_pyqt_ui --help

Links
-----

- **Source code and issue tracking** at `GitHub <https://github.com/reclosedev/make_qt_ui>`_.
