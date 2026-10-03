import matplotlib.pyplot as plt 
import numpy as np
import cv2

image = plt.imread('question1/original-image.png')

r = image[:,:,0]
g = image[:,:,1]
b = image[:,:,2]

image_gray = (0.299 * r + 0.587 * g + 0.114 * b)
image_blur = cv2.GaussianBlur(image_gray, (21, 21), 0)
pencil_sketch_image = image_gray/image_blur
pencil_sketch_image = np.clip(pencil_sketch_image, 0.0, 1.0)

plt.figure(figsize=(10,10))
plt.imshow(pencil_sketch_image, cmap = 'gray') #usando cmap = 'gray' para corrigir plotagem da biblioteca, sem o cmap fica tudo roxo e amarelo
plt.axis('off') #só pra tirar os eixos x e y do gráfico que mostra no plt prof :)
plt.show()
