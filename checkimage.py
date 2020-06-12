# -*- coding: utf-8 -*-
"""checkimage.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/156OL_DUsfQx562kbkni1hkCdxsfrhYDr
"""

# Commented out IPython magic to ensure Python compatibility.
from google.colab import drive
drive.mount('/content/gdrive/', force_remount=True)

!pwd
# %cd /content/gdrive/My\ Drive/EE599finaldata/

import h5py,os, json
with h5py.File('/content/gdrive/My Drive/EE599finaldata/filter_org_img_25.hdf5', 'r') as hf:
  print(hf.keys())
  train_input = hf['ip_data'][:]

import numpy as np
import matplotlib.pyplot as plt
import pylab
pylab.rcParams['figure.figsize'] = (5,5)

print(train_input.shape)
plt.figure()
t = train_input[5892,:,:,:]
plt.imshow(t)


