from LandmarkDataUnit import LandmarkDataUnit
import numpy as np
import cv2
import os
import copy
import h5py
import random
# import resource

from BBox import BBox 

def ReadHDF5(idx, h5_dir, h5_prefix):
    h5_file = os.path.join(h5_dir, h5_prefix + '_' + str(idx) + '.h5')
    F_data = h5py.File(h5_file, 'r')
    return F_data

h5_dir = '/home/dehim/Downloads/datasets/landmark_h5'
prefix_test = 'test_aug'
prefix_train = 'train_aug'
h5_file_idx = 0
F_data = ReadHDF5(h5_file_idx, h5_dir, prefix_train)
i = 2

for d in F_data:
    print(d)
img = F_data['data'][i]
img = cv2.merge(img)
if not(np.array_equal(F_data['lossgate_98'][i], np.zeros((), np.float32))):
    F_landmarks = F_data['landmarks_98'][i]
else:
    F_landmarks = F_data['landmarks_68'][i]

print(F_landmarks)
print(F_data['attributes_98'][i])

lm = F_landmarks
lm = np.reshape(lm, (len(F_landmarks)//2, 2))
bbox = BBox(np.array([0, 0, 400, 400]))

img = cv2.resize(img, (400, 400), interpolation=cv2.INTER_NEAREST)
ldu = LandmarkDataUnit(img, None, lm, bbox)
ldu.ProjectBBoxLandmarksToImg()
ldu.DrawLandmarks((0, 0, 255))

cv2.imshow('image', img)
cv2.waitKey(0)