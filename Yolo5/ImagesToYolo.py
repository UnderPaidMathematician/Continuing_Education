import torch
import os
import pandas as pd

# My solution differed greatly from the medium article here. 
# I built a database and sorted the database by ID so I could maintain the order of the images. 

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Images
imgPaths = []  # batch of images

# Gets all images in the path and builds a list of paths.
d = "C:\\Users\\jason\\Documents\\GitHub\\Continuing_Education\\Yolo5\\Data"

# I had to walk the directory to find the images since I had opted to work on each image seperately. 
for root, dirs, files in os.walk(d):
    for file in files:
        if file.endswith(".jpg"):
             imgPaths.append(os.path.join(root, file))

# Noticed an odd issue where we lose the order that the images had origionally. Here is my fix. 
myData = pd.DataFrame(columns=["Id","Path"])

# Building a sortable index
# This may have been a bit heavy handed but I had named all files image<some number>.jpg
# I built a database with the id as the image number and the path to the image. 
for img in imgPaths:
    myData = myData.append({"Id": int(str(img).split(".")[0].split("e")[-1]), "Path": img}, ignore_index=True)

# Sort by ID
myData = myData.sort_values(by=["Id"])


for i in myData["Path"]:
# Inference
    results = model(i)

    # Results
    results.print()
    results.save()  # or .show()

    results.xyxy[0]  # img1 predictions (tensor)
    results.pandas().xyxy[0]  # img1 predictions (pandas)