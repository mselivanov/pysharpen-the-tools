"""
Setup for playing with cpython
"""
from distutils.core import setup
from Cython.Build import cythonize

setup(
        ext_modules=cythonize("./pysharpen/performance/cysqrt.pyx")
)
