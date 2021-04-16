import numpy as np
a=np.zeros((11,11))
#print(a)
for i in range(11):
	for j in range(11):
		if (i==j):
			a[i][j] = 1
		elif(i!=j):
			a[i][11-1-i] = 1
			
print(a)

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
