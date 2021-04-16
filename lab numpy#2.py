import cv2 
import numpy as np
horizontal_gradient1=np.zeros((255,255))
w = horizontal_gradient1.shape[1]
h = horizontal_gradient1.shape[0]
for i in range(w):
    for j in range(h):
        horizontal_gradient1[j][i] = horizontal_gradient1[j][i]+ j
cv2.imwrite('horizontal_grad1.jpg', horizontal_gradient1)


horizontal_gradient2=np.full((255,255),255)
w = horizontal_gradient2.shape[1]
h = horizontal_gradient2.shape[0]
for i in range(w):
    for j in range(h):
        horizontal_gradient2[j][i] = horizontal_gradient2[j][i]-j
cv2.imwrite('horizontal_grad2.jpg', horizontal_gradient2)


vertical_gradient1=np.zeros((255,255))
w = vertical_gradient1.shape[1]
h = vertical_gradient1.shape[0]
for i in range(w):
    for j in range(h):
        vertical_gradient1[i][j] = vertical_gradient1[i][j]+ j
cv2.imwrite('vertical_gradient1.jpg', vertical_gradient1)


vertical_gradient2=np.full((255,255),255)
w = vertical_gradient2.shape[1]
h = vertical_gradient2.shape[0]
for i in range(w):
    for j in range(h):
        vertical_gradient2[i][j] = vertical_gradient2[i][j]-j
cv2.imwrite('vertical_gradient2.jpg', vertical_gradient2)
