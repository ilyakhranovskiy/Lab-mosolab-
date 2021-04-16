import cv2
import numpy as np
import matplotlib.pyplot as plt

#Зчитаємо та завантажимо тестове чорно-біле та кольорове зображення.
img1= cv2.imread(r"C:\Users\Public\Pictures\Sample Pictures\sample3.png", cv2.IMREAD_GRAYSCALE)
img2= cv2.imread(r"C:\Users\Public\Pictures\Sample Pictures\Penguins.jpg", cv2.IMREAD_COLOR)

#Відобразимо чорно-біле та кольорове зображення.
cv2.imshow("Image1", img1)
cv2.imshow("Image2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Перетворимо зображення з колірної моделі BGR в колірні моделі RGB і HSV та відобразимо.
plt.figure(figsize=(5,5))
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.show();

img2_hsv=cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
plt.figure(figsize=(5, 5))
plt.imshow(img2_hsv)
plt.show();

#Окремо відобразимо колірні канали для зображень із колірними моделями RGB та HSV.
#RGB
plt.figure(figsize=(5, 5))

plt.subplot(131);
R = np.zeros(img2.shape, dtype='uint8')
R[:, :, 0] = img2[:, :, 0]
plt.imshow(R)

plt.subplot(132);
G = np.zeros(img2.shape, dtype='uint8')
G[:, :, 1] = img2[:, :, 1]
plt.imshow(G)

plt.subplot(133);
B = np.zeros(img2.shape, dtype='uint8')
B[:, :, 2] = img2[:, :, 2]
plt.imshow(B)

plt.show()
#HSV
plt.figure(figsize=(5, 5))

plt.subplot(131);
R = np.zeros(img2_hsv.shape, dtype='uint8')
R[:, :, 0] = img2_hsv[:, :, 0]
plt.imshow(R)

plt.subplot(132);
G = np.zeros(img2_hsv.shape, dtype='uint8')
G[:, :, 1] = img2_hsv[:, :, 1]
plt.imshow(G)

plt.subplot(133);
B = np.zeros(img2_hsv.shape, dtype='uint8')
B[:, :, 2] = img2_hsv[:, :, 2]
plt.imshow(B)

plt.show()
#Скопіюємо область інтересу (Region of Interest) чорно-білого зображення,
#використовуючи наступні діапазони 0:img.shape[0]/2, 0:img.shape[1]/2.
img1_crop = img1[0:int(img1.shape[0]/2), 0:int(img1.shape[1]/2)]
plt.figure(figsize=(5,5))
plt.imshow(img1_crop, cmap='gray')
plt.show()

#Збережемо область інтересу (Region of Interest).
cv2.imwrite("img1_crop.png", img1_crop)


