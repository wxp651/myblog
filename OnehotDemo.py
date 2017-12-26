#coding=utf-8
# -*- coding: utf-8 -*-
import numpy as np
from sklearn import preprocessing
labels = np.array([1,5,3,2,1,4,2,1,3])

lb = preprocessing.LabelBinarizer()
lb.fit(labels)

lb.transform(labels)