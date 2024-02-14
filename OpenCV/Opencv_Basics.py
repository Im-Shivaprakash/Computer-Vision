#Importing Modules
import cv2
from PIL import Image

my_image = 'OpenCV/cyber_girl.jpeg'
image = cv2.imread(my_image)
print(type(image))

import matplotlib.pyplot as plt
plt.imshow(image)               #picture array format BGR but in PIL - RGB

#change color space
new_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(new_image)

#gray image
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_img)
cv2.imwrite('cyber_bnw.jpg', gray_img)

#Slicing channels
r, b, g = image[::0], image[::1], image[::2]



