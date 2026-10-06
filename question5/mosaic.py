import matplotlib.pyplot as plt
import numpy as np
image = plt.imread("question5/original-image.jpg")

r = image[:,:,0]
g = image[:,:,1]
b = image [:,:,2]

image_gray = (0.299 * r) + (0.587 * g) + (0.114 * b) # obter a imagem em níveis de cinza

H, W = image_gray.shape
H = (H // 4) * 4
W = (W // 4) * 4
image_gray = image_gray[0:H, 0:W]

h_bloco = H // 4
w_bloco = W // 4

blocos = {}
index = 1

# Varrendo a imagem e recortando cada bloco na ordem original (1 a 16)
for i in range(4):
    for j in range(4):
        # Define os limites do bloco atual
        y_ini, y_fim = i * h_bloco, (i + 1) * h_bloco
        x_ini, x_fim = j * w_bloco, (j + 1) * w_bloco
        
        # Recortando o bloco da matriz original e salvando no dicionário
        blocos[index] = image_gray[y_ini:y_fim, x_ini:x_fim]
        index += 1

# Nova ordem da matriz
nova_ordem = [
    [6,11,13,3], [8,16,1,9], [12,14,2,7], [4,15,10,5]
]

mosaico = np.zeros((H, W), dtype=image_gray.dtype)

# Preenche a matriz vazia com os blocos na nova disposição
for i in range(4):
    for j in range(4):
        y_ini, y_fim = i * h_bloco, (i + 1) * h_bloco
        x_ini, x_fim = j * w_bloco, (j + 1) * w_bloco
        
        # Pega o número do bloco que deve ir para essa posição
        num_bloco = nova_ordem[i][j]
        
        # Insere o bloco correspondente no mosaico
        mosaico[y_ini:y_fim, x_ini:x_fim] = blocos[num_bloco]

plt.figure(figsize=(8, 8))
plt.imshow(mosaico, cmap='gray')
plt.title('Questão 5: Mosaico 4x4')
plt.axis('off')
plt.show()