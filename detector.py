import numpy as np
import cv2
import lane_utils
from PIL import Image, ImageDraw, ImageFont

####################################################

useCamera = False
cameraNum = 0

videoPath = 'lane_detection.mp4'

frameWidth = 800
frameHeight = 500

if useCamera:
    intialTracbarVals = [24, 55, 12, 100]  # wT,hT,wB,hB
else:
    intialTracbarVals = [42, 63, 14, 87]  # wT,hT,wB,hB

###################################################ก#
if useCamera:
    cap = cv2.VideoCapture(cameraNum)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
else:
    cap = cv2.VideoCapture(videoPath)
count = 0
noOfArrayValues = 10
global arrayCurve, arrayCounter, directionText
averageCurve = 0
arrayCounter = 0
directionText = ''
arrayCurve = np.zeros([noOfArrayValues])
myVals = []
lane_utils.initializeTrackbars(intialTracbarVals)

while True:

    success, img = cap.read()
    if useCamera == False: img = cv2.resize(img, (frameWidth, frameHeight), None)
    imgWarpPoints = img.copy()
    imgFinal = img.copy()
    imgCanny = img.copy()

    imgUndis = lane_utils.undistort(img)
    imgThres, imgCanny, imgColor = lane_utils.thresholding(imgUndis)
    src = lane_utils.valTrackbars()
    imgWarp = lane_utils.perspective_warp(imgThres, dst_size=(frameWidth, frameHeight), src=src)
    imgWarpPoints = lane_utils.drawPoints(imgWarpPoints, src)
    imgSliding, curves, lanes, ploty = lane_utils.sliding_window(imgWarp, draw_windows=True)

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

        cv2.putText(imgFinal, str(int(averageCurve)), (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2,
                    cv2.LINE_AA)

        directionText = 'No lane'
        if averageCurve > 10:
            directionText = 'Turn right'

        elif averageCurve < -10:
            directionText = 'Turn left'

        elif averageCurve < 10 and averageCurve > -10:
            directionText = 'ตรง'

        elif averageCurve == -1000000:
            directionText = 'Lane not found'

    except:
        lane_curve = 00
        pass

    # แสดงข้อความ ภาษาไทย
    # font = ImageFont.truetype('TP_Kubua.ttf', 45)
    img_pil = Image.fromarray(imgFinal)
    draw = ImageDraw.Draw(img_pil)
    draw.text((20, 30), directionText, fill=(0, 255, 255))
    imgFinal = np.array(img_pil)

    # แสดง Lane Curve Lines
    # imgFinal = lane_utils.drawLines(imgFinal,lane_curve)

    imgThres = cv2.cvtColor(imgThres, cv2.COLOR_GRAY2BGR)
    imgBlank = np.zeros_like(img)
    imgStacked = lane_utils.stackImages(0.7, ([img, imgUndis, imgWarpPoints],
                                              [imgColor, imgCanny, imgThres],
                                              [imgWarp, imgSliding, imgFinal]
                                              ))

    # แสดงขั้นตอน
    # cv2.imshow("PipeLine",imgStacked)

    cv2.imshow("Result", imgFinal)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
