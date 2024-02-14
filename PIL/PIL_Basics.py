#Import Modules
from PIL import Image
import matplotlib.pyplot as plt


my_image = 'cyber_girl.jpeg'
image = Image.open(my_image)

# PIL
image.show(title = "CyberGirl")

# Matplotlib
plt.imshow(image)

# Prints the format of the image
print(image.format)

# Prints the size of the image
print(image.size)

# Prints the mode of the image
print(image.mode)

#-------------------------------------------------------------------------------------

from PIL import ImageOps
image_gray = ImageOps.grayscale(image)
image_gray.show(title = "B&W")

#Img - Mode
print(image_gray.mode)

#Save Image
image_gray.save("B&W-CyberGirl.png") #Can save in both jpg and png

#Quantize Image
quan_img = image_gray.quantize(2)  #Adjusts the contrast of the image
quan_img.show()

#Splitting Channels
r, b, g = image.split()
r.show(title='red_channel')
b.show(title='blue_channel')
g.show(title='green_channel')

#Converting Images into array
import numpy as np
array = np.array(image)
print(array)