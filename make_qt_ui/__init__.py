from .converter import main

# Entry points for setuptools:
def make_pyqt():
    main('pyqt')
    
    
def make_pyside():
    main('pyside')