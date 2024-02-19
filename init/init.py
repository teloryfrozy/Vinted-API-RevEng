############################
#   Logistic Version 1.0   #
#   Author: La Bro'tique   #
############################
from importlib import import_module
from os import remove, rmdir, system
from platform import system as sys
from shutil import move, rmtree
from subprocess import call

def checkPackage(package: str) -> str:
    """Check if the required Python package is installed. If not, return the name of the package
    
    Argument:
        - {string} package: name of the associated package
    
    Returns:
        - {string} package: if package can not be imported
    """
    try:
        import_module(package)
    except ImportError:
        return package

def installPackage():
    """Install all the required packages"""
    missing = [p for p in ["pandas", "psutil", "bs4", "selenium", "PyPDF2", "reportlab", "PyQt6", "openpyxl", "requests", "matplotlib"] if checkPackage(p)] # list of all missing packages
    if missing:
        system('pip install ' + ' '.join(missing))

if __name__ == "__main__":
    installPackage()