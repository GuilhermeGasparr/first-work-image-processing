import matplotlib.pyplot as plt

image = plt.imread('question2/original-image.jpg')

r = image[:,:,0]
g = image[:,:,1]
b = image[:,:,2]

image_A = (0.299 * r + 0.587 * g + 0.114 * b)
    
image_A_in_range = image_A/255.0

gamma_values = [1.5,2.5,3.5]
fig, eixos = plt.subplots(1, 3 , figsize = (15,5))
for i, gamma in enumerate(gamma_values): 
    image_B_in_range = image_A_in_range ** (1/gamma)
    image_B = image_B_in_range * 255
    
    eixos[i].imshow(image_B, cmap= 'gray', vmin = 0, vmax = 255)
    eixos[i].set_title(f'Gama ($\gamma$) = {gamma}')
    eixos[i].axis('off')

plt.tight_layout()
plt.show()