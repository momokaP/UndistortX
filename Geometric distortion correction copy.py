import numpy as np
import cv2 as cv

video_file = './KakaoTalk_20250405_210903239.mp4'
K = np.array([[627.9110147, 0, 628.71703011],
              [0, 637.91247595, 405.01966982],
              [0, 0, 1]]) # Derived from `calibrate_camera.py`
dist_coeff = np.array([0.00645102, 0.08530672, -0.00891972, 0.00220997, -0.09186439])

video = cv.VideoCapture(video_file)
assert video.isOpened(), 'Cannot read the given input, ' + video_file

show_rectify = True
map1, map2 = None, None

while True:
    valid, img = video.read()
    if not valid:
        break

    info = "Original"
    if show_rectify:
        if map is None or map2 is None:
            map1, map2 = cv.initUndistortRectifyMap(K, dist_coeff, None, None, (img.shape[1], img.shape[0]), cv.CV_32FC1)
        img = cv.remap(img, map1, map2, interpolation=cv.INTER_LINEAR)
        info = "Rectified"
    cv.putText(img, info, (10,25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))

    cv.imshow("Geometric Distortion Correction", img)
    key = cv.waitKey(10)
    if key == ord(' '):
        key = cv.waitKey()
    if key == 27:
        break
    elif key == ord('\t'):
        show_rectify = not show_rectify 

video.release()
cv.destroyAllWindows()