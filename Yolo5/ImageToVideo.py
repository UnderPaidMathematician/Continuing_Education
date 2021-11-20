import cv2
import os
import pandas as pd


pathOut = 'video.avi'

# I used this to find the fps
vidcap = cv2.VideoCapture('Yolo5\largeff7.mp4')
fps = vidcap.get(cv2.CAP_PROP_FPS)

imgPaths = []
# Gets all images in the path and builds a list of paths.
d = "C:\\Users\\jason\\Documents\\GitHub\\Continuing_Education\\runs\\detect"
import os
for root, dirs, files in os.walk(d):
    for file in files:
        if file.endswith(".jpg"):
             imgPaths.append(os.path.join(root, file))

# Noticed an odd issue where we lose the order that the images had originally. Here is my fix. 
myData = pd.DataFrame(columns=["Id","Path"])

# Building a sortable index
for i in imgPaths:
    myData = myData.append({"Id": int(str(i).split(".")[0].split("e")[-1]), "Path": i}, ignore_index=True)

# Sort by ID
myData = myData.sort_values(by=["Id"])

frameArray = []

for p in myData["Path"]:

    #reading each files
    img = cv2.imread(p)
    height, width, layers = img.shape
    size = (width,height)
    
    #inserting the frames into an image array
    frameArray.append(img)

out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
for i in range(len(frameArray)):
    # writing to a image array
    out.write(frameArray[i])
out.release()