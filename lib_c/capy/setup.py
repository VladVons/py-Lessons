from setuptools import setup, Extension


# python3 setup.py build
setup(
    ext_modules = [
        Extension('MyLib', ['lib/test.c']),
        Extension('FS', ['lib/fs.c']) 
    ]
)
