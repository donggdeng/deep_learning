import matplotlib.pyplot as plt
from matplotlib.image import imread
image = imread('./dataset/bird.jpeg')
plt.imshow(image)

plt.show()