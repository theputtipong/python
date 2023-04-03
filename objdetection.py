import cv2 as cv
import numpy as np
from wandb import Classes

net = cv.dnn.readNet("pig-yolo.weights","yolo-obj.cfg") #extract file this file "pig-yolo.zip" to get pig-yolo.weights
classes = []
# chk obj in file coco
with open("coco.names","r") as f:
    classes = [line.strip() for line in f.readlines()]
print(classes)
layer_name = net.getLayerNames()
output_layer = [layer_name[i-1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0,255,size=(len(classes),3))

#get file img to test
importfile = "pig/Screenshot (29).png"
img = cv.imread(importfile)
img = cv.resize(img,None,fx=0.8,fy=0.7)
height,width,channel = img.shape

# detect obj
blob = cv.dnn.blobFromImage(img,0.00392,(416,416),(0,0,0),True,crop=False)
net.setInput(blob)
outs = net.forward(output_layer)
print(outs)

class_ids = []
confidences = []
boxes = []
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            # obj detection
            center_x = int(detection[0]*width)
            center_y = int(detection[1]*height)
            w= int(detection[2]*width)
            h= int(detection[3]*height)
            x= int(center_x - w/2)
            y= int(center_y - h/2)
            boxes.append([x,y,w,h])
            confidences.append(float(confidence))
            class_ids.append(class_id)
print(len(boxes))
indexes = cv.dnn.NMSBoxes(boxes,confidences,0.5,0.4)
print(indexes)
font = cv.FONT_HERSHEY_COMPLEX_SMALL
for i in range(len(boxes)):
    if i in indexes:
        x,y,w,h = boxes[i]
        # label = str(classes[class_ids[i]])
        print("pig")
        color = colors[i]
        cv.rectangle(img,(x,y),(x+w,y+h),color,2)
        # cv.putText(img,label,(x,y+30),font,1,color,1)
        cv.putText(img,"pig",(x,y+30),font,1,color,1)
# outputfile = "output/ai_"+importfile+".png"
outputfile = "output/ai_29.png"
status = cv.imwrite(outputfile,img)
print(status)
# cv.imshow("obj detection",img)
# cv.waitKey(0)
# cv.destroyAllWindows()