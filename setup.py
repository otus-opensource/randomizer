import os
from setuptools import setup, find_packages

def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    try:
        file = open(path, encoding='utf-8')
    except TypeError:
        file = open(path)
    return file.read()


setup(
    name='otus-radomizer',
    version='0.1.0',
    description='Random utility for dod events',
    long_description=read('README.md'),
    author='Vitaly Chibrikov, Grigory Ozhegov',
    author_email='code@otus.ru',
    url='https://github.com/otus-opensource/randomizer',
    packages=find_packages(),
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    zip_safe=False,
    include_package_data=True
)
