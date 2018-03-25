"""Build setup tool script."""

from setuptools import setup

setup(
    name='clean',
    version='0.1.1',
    py_modules=['clean'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        clean=clean:cli
    ''',
)
