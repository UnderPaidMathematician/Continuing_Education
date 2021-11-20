# Adapted from: https://medium.com/@iKhushPatel/convert-video-to-images-images-to-video-using-opencv-python-db27a128a481

import cv2
vidcap = cv2.VideoCapture('Yolo5\largeff7.mp4')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("Yolo5\\Data\\"+"image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames
sec = 0

# I changed fps to instead be the fps from the video this used to be hard coded to .05
fps = vidcap.get(cv2.CAP_PROP_FPS)
frameRate = 1/fps
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)

print("Finished converting video to images.")