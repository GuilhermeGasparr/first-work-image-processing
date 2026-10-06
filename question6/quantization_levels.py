import matplotlib.pyplot as plt
import numpy as np

image = plt.imread('question6/original-image.jpg')
r, g, b = image[:,:,0], image[:,:,1], image[:,:,2]

image_gray = (0.299 * r) + (0.587 * g) + (0.114 * b)

niveis_testados = [64, 32, 16, 8, 4, 2]
letras = ['b', 'c', 'd', 'e', 'f', 'g']

fig, eixos = plt.subplots(3, 3, figsize=(15, 15))

eixos[0, 0].axis('off') 

eixos[0, 1].imshow(image_gray, cmap='gray', vmin=0, vmax=255)
eixos[0, 1].set_title('(a) 256 níveis', pad=10) 
eixos[0, 1].axis('off')

eixos[0, 2].axis('off')

for idx, L in enumerate(niveis_testados[0:3]):
    img_q = np.round((image_gray / 255.0) * (L - 1)) * (255.0 / (L - 1))
    img_q = img_q.astype(np.uint8)
    
    eixos[1, idx].imshow(img_q, cmap='gray', vmin=0, vmax=255)
    eixos[1, idx].set_title(f'({letras[idx]}) {L} níveis', pad=10)
    eixos[1, idx].axis('off')

for idx, L in enumerate(niveis_testados[3:6]):
    img_q = np.round((image_gray / 255.0) * (L - 1)) * (255.0 / (L - 1))
    img_q = img_q.astype(np.uint8)
    
    eixos[2, idx].imshow(img_q, cmap='gray', vmin=0, vmax=255)
    eixos[2, idx].set_title(f'({letras[idx + 3]}) {L} níveis', pad=10)
    eixos[2, idx].axis('off')

fig.subplots_adjust(hspace=0.4, wspace=0.2)

plt.show()
