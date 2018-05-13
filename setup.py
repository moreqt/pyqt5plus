'''
Created on 13-May-2018

@author: dgraja
'''

from setuptools import setup

setup(name='pyqt5plus',
      version='0.1.180513.2115',
      description='Additional features to PyQt5',
      url='https://github.com/moreqt/pyqt5plus',
      author='Govinda Raja D',
      author_email='',
      license='LGPL 3.0',
      packages=['pyqt5plus'],
      classifiers = [
          'Development Status :: 1 - Planning',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 3.6',
          ],
      install_requires=['PyQt5'],
      keywords='PyQt5 extensions',
      python_requires='>=3.6',
      zip_safe=False)

