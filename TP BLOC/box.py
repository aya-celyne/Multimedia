import cv2 as cv
import numpy as np
from  PIL import Image
import math

def MSE(bloc1, bloc2):
    sum = 0
    h = bloc1.shape[0]
    w = bloc1.shape[1]
    return np.square(np.subtract(bloc1,bloc2)).mean()





#start and end du bloc rouge
Deb = (231, 367)
Fin = (319, 550)

# cordonnées début et fin de box vert à partir du box rouge en ajoutant ou decrementant 100
Deb2 = (131, 267)
Fin2 = (419, 650)

# le bloc1 représente le box rouge de l'image 072
Img = Image.open('image072.png').convert('L')
mat = np.array(Img)

bloc1 = []
for i in range(Deb[1], Fin[1]):
    for j in range(Deb[0], Fin[0]):
        bloc1.append(mat[i][j])
bloc1 = np.reshape(bloc1, (Fin[1]-Deb[1], Fin[0]-Deb[0]))

height = bloc1.shape[0]
width = bloc1.shape[1]


# le blocG represente le box vert

Img = Image.open('image092.png').convert('L')
mat = np.array(Img)

blocG=[]
for i in range(Deb2[1], Fin2[1]):
    for j in range(Deb2[0], Fin2[0]):
        blocG.append(mat[i][j])
blocG = np.reshape(blocG, (Fin2[1]-Deb2[1], Fin2[0]-Deb2[0]))
#Image.fromarray(blocG).show()

#parcourir blocG et calculer le MSE dans chaque sous-bloc rouge
heightG = blocG.shape[0]
widthG = blocG.shape[1]
bloc2 = []
Min = math.inf

for i in range(heightG-height):
    for j in range(widthG-width):
        bloc2 = blocG[i:i+height, j:j+width]
        #Image.fromarray(bloc2).show()
        MSe = MSE(bloc2,bloc1)
        if  MSe < Min :
            Min = MSe
            z = i
            v = j

found = []
found = blocG[z:z+height , v:v+width]
Image.fromarray(found).show()
print(Min)
