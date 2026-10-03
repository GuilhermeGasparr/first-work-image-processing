import matplotlib.pyplot as plt
import numpy as np

image_A = plt.imread('question3/original-image1.jpg')
image_B = plt.imread('question3/original-image2.jpg')

#Padronizando tamanho das imagens para o menor tamanho entre as duas aqui Prof ;)
altura_min = min(image_A.shape[0], image_B.shape[0])
largura_min = min(image_A.shape[1], image_B.shape[1])
image_A_normalized = image_A[0:altura_min, 1:largura_min] 
image_B_normalized = image_B[0:altura_min, 1:largura_min]

#tons de cinza

r_A = image_A_normalized[:,:,0]
g_A = image_A_normalized[:,:,1]
b_A = image_A_normalized[:,:,2]

r_B = image_B_normalized[:,:,0]
g_B = image_B_normalized[:,:,1]
b_B = image_B_normalized[:,:,2]

image_A_gray = (0.299 * r_A + 0.587 * g_A + 0.114 * b_A)
image_B_gray = (0.299 * r_B + 0.587 * g_B + 0.114 * b_B)

image_A_in_range = image_A_gray/255.0
image_B_in_range = image_B_gray/255.0

weights = [0.2, 0.5, 0.8]

combination1 = ((image_A_in_range * weights[0]) + (image_B_in_range * weights[2]))
combination2 = ((image_A_in_range * weights[1]) + (image_B_in_range * weights[1]))  
combination3 = ((image_A_in_range * weights[2]) + (image_B_in_range * weights[0])) 

combination1 = np.clip(combination1, 0.0, 1.0)
combination2 = np.clip(combination2, 0.0, 1.0)
combination3 = np.clip(combination3, 0.0, 1.0)

fig, eixos = plt.subplots(1, 3, figsize = (15,5))

eixos[0].imshow(combination1, cmap="gray")
eixos[0].set_title(f'A({weights[0]}) + B({weights[2]})')
eixos[0].axis('off')

eixos[1].imshow(combination2, cmap="gray")
eixos[1].set_title(f'A({weights[1]}) + B({weights[1]})')
eixos[1].axis('off')

eixos[2].imshow(combination3, cmap="gray")
eixos[2].set_title(f'A({weights[2]}) + B({weights[0]})')
eixos[2].axis('off')

plt.tight_layout()
plt.show()