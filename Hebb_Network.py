
import numpy as np
import glob
import imageio

for image_path in glob.glob("G:/python project/Heb_net_img\\*.png"):              # set path of all image
    im = imageio.imread(image_path)                                           # read all the image
    print (im.shape)                                                          #check shape and data type all image
    print (im.dtype)

print("ASSUME OUTPUT OF 1ST IMAGE IS ",-1,"AND 2nd IMAGE IS " ,1)
y1 = -1         # there are 2 image so we put output of first image 1
y2 = 1        # output of 2nd image is -1
b = 0       # initialize bias is 0
w = 0       # initialize weight is 0





## for image 1st output is 1
print("FOR FIRST IMAGE")
print(im[0])
result1 = np.array(im[0]).flatten()# convert matrix in a single row
print("convert matrix in single coloumn \n",result1)
ln = len(result1)
new_r1 = []
for n in range(ln):
    if result1[n] == 255:
        new_r1.append(-1)
    else:
        new_r1.append(1)
print("Convert value in -1 or 1 \n",new_r1)
uw = []
ub = []
for i in range(ln):
    uw.append(w +(new_r1[i]*y1))
    ub.append(b + y1)
print("print the update Weight and update Bias after evaluate 1st image")
print("update weight: \n",uw,"\n update bias \n",ub)

#for(j = 0, j <= result1[-1], j++):
    





## for image 2nd output is 1
print("FOR SECOND IMAGE")
print(im[1])
result2 = np.array(im[1]).flatten()       # convert matrix in a single row
print("convert matrix in single coloumn \n",result2)
ln = len(result2)
new_r2 = []
for n in range(ln):
    if result2[n] == 255:
        new_r2.append(-1)
    else:
        new_r2.append(1)
print("Convert value in -1 or 1 \n",new_r2)
n_uw = []
n_ub = []

for i in range(ln):
    n_uw.append(uw[i] +(new_r2[i]*y2))
    n_ub.append(ub[i] + y2)
print("print the update Weight and update Bias after evaluate 2st image")
print("update weight: \n",n_uw," \n update bias \n",n_ub)





# check function is correct or not
y11 = 0
y22 = 0
for i in range(ln):
    y11 += (new_r1[i]*n_uw[i]) + n_ub[i]
    y22 += (new_r2[i]*n_uw[i]) + n_ub[i]

print("output of 1st image",y11)
print("output of 2nd image",y22)
