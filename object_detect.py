# coding: utf-8

# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2

# construct the arguement parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True,
               help='path to Caffe "deploy" prototxt file')
ap.add_argument("-m", "--model", required=True,
               help='path to Caffe pre-trained model')
ap.add_argument("-c", "--confidence", type=float, default=0.2,
               help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

# list of class labels MobileNet SSD was trained to detect
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

# list of class labels you want to ignore
IGNORE = set([])

# assigning random label/box colors
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# load our serialized model from disk
print('[INFO] loading model...')
net = cv2.dnn.readNetFromCaffe(args['prototxt'], args['model'])

# initialize the video stream
# allow the camera sensor to warmup
# initialize the FPS counter
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)
fps = FPS().start()

# looping over the frames from the Video Stream
while True:
    # grab the frame from the threaded video stream and resize it
    # to have a max width of 400 px

    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    # grab the frame dim and convert it to a blob
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame,
                    (300, 300)) , scalefactor=0.007843,
                     size=(300,300), mean=127.5)

    # pass the blob through the network
    # obtain the detections and predictions
    net.setInput(blob)
    detections = net.forward()

    # loop over the detections
    for i in np.arange(0, detections.shape[2]):
        # extract the confidence
        confidence = detections[0, 0, i, 2]

        # filter out w.r.t confidence threshold
        if confidence > args['confidence']:
            # extract the index of the class label from the
            # 'detections'
            idx = int(detections[0, 0, i, 1])

            # if the predicted class label is in the set of IGNORE
            if CLASSES[idx] in IGNORE:
                continue

    # compute the (x, y)-coordinates of the bounding box for the object
    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
    (startX, startY, endX, endY) = box.astype('int')

    # draw the predictions on the frame
    label = "{}: {:.2f}%".format(CLASSES[idx],
        confidence * 100)
    cv2.rectangle(frame, (startX, startY), (endX, endY),
        COLORS[idx], thickness=2)

    # drawing the predicted label
    if startY - 15 > 15:
        text_y = startY - 15
    else:
        text_y = startY + 15

    cv2.putText(frame, label, (startX, text_y),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

    # show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # press 'q' to quit
    if key == ord("q"):
        break

    # update the FPS counter
    fps.update()

# stop the timer and display the FPS information
fps.stop
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# destroy windows
cv2.destroyAllWindows()
vs.stop()
