from tkinter import Tk
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
import numpy as np

Tk().withdraw()
file_path = askopenfilename(title="Enter the image")

if not file_path:
    print("No file selected. Exiting.")
    exit()

img = plt.imread(file_path)

if img.ndim == 2 :
    gray = img 
else:
    R = img[:,:,0]
    G = img[:,:,1]
    B = img[:,:,2]

gray = 0.299*R + 0.587*G + 0.114*B
h, w = gray.shape

#For Blur
kernel = np.ones((3,3)) / 9
padded = np.pad(gray, 1, mode='edge')
blurred = np.zeros((h,w))

for i in range(h):
    for j in range(w):
        patch = padded[i:i+3, j:j+3]
        blurred[i,j] = np.sum(patch * kernel)

#Edge Detection
kx = np.array([
[-1,0,1],
[-2,0,2],
[-1,0,1]])

ky = np.array([
[-1,-2,-1],
[0,0,0],
[1,2,1]])

edges = np.zeros((h,w))
blurred_edges = np.pad(blurred, 1, mode='edge')

for i in range(h):
    for j in range(w):
        patch = blurred_edges[i:i+3, j:j+3]
        gx = np.sum(patch * kx)
        gy = np.sum(patch * ky)
        edges[i,j] = np.sqrt(gx**2 + gy**2)

#Normalize and threshold
edges = edges / np.max(edges)
edges = edges > 0.2
edges = edges.astype(float)



#This is for Display
plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.title("Original")
plt.imshow(img)

plt.subplot(2,2,2)
plt.title("Gray")
plt.imshow(gray, cmap='gray')

plt.subplot(2,2,3)
plt.title("Blurred")
plt.imshow(blurred, cmap='gray')

plt.subplot(2,2,4)
plt.title("Edges")
plt.imshow(edges, cmap='gray')

save = input("Do you want to save the image (y/n)?? ")

if save.lower() == 'y':
    plt.savefig("edges_output.png")
    print("Your image is saved as edges_output.png")

plt.show()


