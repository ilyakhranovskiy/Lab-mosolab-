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
