#!/usr/bin/env python

from distutils.core import setup
setup(name='calibration',
      version='1.0',
      description='NN Model Calibration Utilities',
      author='Jaxon Keeler',
      author_email='jaxonkeeler@gmail.com',
      packages=['metrics.py', 'recalibration.py', 'visualization.py'],
     )
