import matplotlib.pyplot as plt
import numpy as np 

image = plt.imread('question4/original-image.jpg')

r = image[:,:,0]
g = image[:,:,1]
b = image[:,:,2]

image_gray = (0.299 * r) + (0.587 * g) + (0.114 * b) # obter a imagem em níveis de cinza

image_negative = 255 - image_gray # cálculo para obter o negativo da imagem
image_transformed = np.clip(image_gray, 100, 200) # cálculo para converter o intervalo de intensidades entre 100 e 200

image_flipped = np.copy(image_gray)
image_flipped[::2, :] = image_gray[::2, ::-1]

image_half_mirror = np.copy(image_gray)
altura = image_half_mirror.shape[0]
metade = altura // 2
tamanho_fatia = altura - metade
image_half_mirror[metade:altura, :] = image_gray[0:tamanho_fatia, :][::-1, :]

image_vertical_flip = image_gray[::-1, :]
plt.imshow(image_vertical_flip, cmap= 'gray')
plt.axis('off')
plt.show()
