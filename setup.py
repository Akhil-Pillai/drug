import os
from setuptools import setup

readme = open(os.path.join(os.path.dirname(__file__), 'README'), 'r').read()

setup(
    name='drug',
    author='Akhil Pillai',
    author_email='akhilpillai18@gmail.com',
    version='0.1',
    url='http://github.com/Akhil-Pillai/drug',
    py_modules=['drug'],
    description='A data visualisation project',
    long_description=readme,
    entry_points={
        'console_scripts': [
            'drug = drug:main'
        ]
    },
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python'
    ]
)
