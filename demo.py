import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys
def somatic(im):
    
    plt.imshow(im)
    imrgb = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
    imgray = cv2.cvtColor(imrgb,cv2.COLOR_BGR2GRAY)
    plt.imshow(imrgb)
    
    # RGB Channels

    r = imrgb[:, :, 0]
    g = imrgb[:, :, 1]
    b = imrgb[:, :, 2]

    f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20,10))

    ax1.set_title('Red')
    ax1.imshow(r, cmap='gray')

    ax2.set_title('Green')
    ax2.imshow(g, cmap='gray')

    ax3.set_title('Blue')
    ax3.imshow(b, cmap='gray')
    img = np.copy(g)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    plt.figure(figsize=(10,10))
    plt.subplot(1,2,1),plt.title('Original Image'),plt.imshow(img)#,'red')
    plt.subplot(1,2,2),plt.title('OpenCV.findContours'),plt.imshow(img,'gray')#,'red')
    print('number of cells detected: ',len(contours))
img_name = sys.argv[1]
print(img_name)
img1 = cv2.imread(img_name)
somatic(img1)