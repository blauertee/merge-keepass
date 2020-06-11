from setuptools import setup, find_packages
setup(
    name='merge-keepass',
    version='0.1',
    # packages=find_packages(),
    # package_dir = {'':'src'},
    scripts=[ 'merge-keepass.py' ],
    py_modules = [ 'keepassmerge' ],

    install_requires=["libkeepass"],

    # metadata to display on PyPI
    author='Scott Hamilton',
    author_email='sgn.hamilton+python@protonmail.com',
    description='Keepass Databases 2.x Merging module and command line utility',
    keywords='keepass merge',
    url='https://github.com/SCOTT-HAMILTON/merge-keepass',
    project_urls={
        'Source Code': 'https://github.com/SCOTT-HAMILTON/merge-keepass',
    },
    classifiers=[
        'License :: OSI Approved :: Python Software Foundation License'
    ]
)
