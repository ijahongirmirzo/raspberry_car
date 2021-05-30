import numpy as np
import cv2
import lane_utils
from PIL import Image, ImageDraw, ImageFont

####################################################
cameraNum = 0

videoPath = 'lane_detection.mp4'

frameWidth = 800
frameHeight = 500

intialTracbarVals = [42, 63, 14, 87]  # wT,hT,wB,hB

cap = cv2.VideoCapture(videoPath)
count = 0
noOfArrayValues = 10
global arrayCurve, arrayCounter, directionText
averageCurve = 0
arrayCounter = 0
directionText = ''
arrayCurve = np.zeros([noOfArrayValues])
myVals = []
lane_utils.initializeTracks(intialTracbarVals)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight), None)
    imgWarpPoints = img.copy()
    imgFinal = img.copy()
    imgCanny = img.copy()

    imgUndis = lane_utils.undistort(img)
    imgThres, imgCanny, imgColor = lane_utils.thresholding(imgUndis)
    src = lane_utils.valTrackbars()
    imgWarp = lane_utils.perspective_warp(imgThres, dst_size=(frameWidth, frameHeight), src=src)
    imgWarpPoints = lane_utils.drawPoints(imgWarpPoints, src)
    imgSliding, curves, lanes, ploty = lane_utils.sliding_window(imgWarp, draw_windows=False)

    try:
        curverad = lane_utils.get_curve(imgFinal, curves[0], curves[1])
        lane_curve = np.mean([curverad[0], curverad[1]])
        imgFinal = lane_utils.draw_lanes(img, curves[0], curves[1], frameWidth, frameHeight, src=src)

        currentCurve = lane_curve // 50
        if int(np.sum(arrayCurve)) == 0:
            averageCurve = currentCurve
        else:
            averageCurve = np.sum(arrayCurve) // arrayCurve.shape[0]
        if abs(averageCurve - currentCurve) > 200:
            arrayCurve[arrayCounter] = averageCurve
        else:
            arrayCurve[arrayCounter] = currentCurve
        arrayCounter += 1
        if arrayCounter >= noOfArrayValues: arrayCounter = 0

        cv2.putText(imgFinal, f'Average curvature: {str(int(averageCurve))}', (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 0, 255), 2,
                    cv2.LINE_AA)

        directionText = 'NO LANE HAS BEEN FOUND'
        if averageCurve > 10:
            directionText = 'TURN RIGHT'

        elif averageCurve < -10:
            directionText = 'TURN LEFT'

        elif averageCurve < 10 and averageCurve > -10:
            directionText = 'GO FORWARD'

        elif averageCurve == -1000000:
            directionText = 'NO LANE HAS BEEN FOUND'

    except:
        lane_curve = 00
        pass

    img_pil = Image.fromarray(imgFinal)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype("arial.ttf", 30)
    draw.text((40, 20), f'Direction: {directionText}', font=font, fill=(0, 0, 255))
    imgFinal = np.array(img_pil)

    imgThres = cv2.cvtColor(imgThres, cv2.COLOR_GRAY2BGR)
    imgBlank = np.zeros_like(img)

    cv2.imshow("Result", imgFinal)

    if 0xFF == ord('q') & cv2.waitKey(1):
        break

cap.release()
cv2.destroyAllWindows()
