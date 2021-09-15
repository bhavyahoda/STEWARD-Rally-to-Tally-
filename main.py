import cv2
import numpy as np
import glob

mp4_video = glob.glob(r"./*.mp4")[0]
local_video_capture = cv2.VideoCapture(mp4_video)

while True:
    ret, frame = local_video_capture.read()
    gray = cv2.medianBlur(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 5)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

local_video_capture.release()
cv2.destroyAllWindows()
