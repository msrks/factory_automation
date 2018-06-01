import numpy as np
import cv2

cap = cv2.VideoCapture(0)
W, H = 480, 640
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, H)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, W)

CROP_W, CROP_H = 140,80


while(True):
    ret, frame = cap.read()
    W, H, _ = frame.shape
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mask = cv2.inRange(frame, (0,0,0), (250,250,250))
    frame_canny = cv2.Canny(mask, threshold1=150, threshold2=300)

    # crop RoI
    roi = frame_canny[CROP_H:-CROP_H, CROP_W:-CROP_W]

    num_white = cv2.countNonZero(roi)
    print(num_white)
    is_exist = True if num_white > 800 else False

    if is_exist:
        # find moments
        mu = cv2.moments(roi, False)
        x, y = int(mu["m10"]/mu["m00"])+CROP_W, int(mu["m01"]/mu["m00"])+CROP_H
        frame = cv2.circle(frame, (x, y), 20, (0, 0, 255), -1)

    output_image = np.zeros((W*2, H*2, 3))
    output_image[:W, :H] = frame/255
    output_image[W:, :H] = np.stack((mask, mask, mask), axis=-1)
    output_image[:W, H:] = np.stack((frame_canny, frame_canny, frame_canny), axis=-1)
    output_image[W+CROP_H:-CROP_H, H+CROP_W:-CROP_W] = np.stack((roi, roi, roi), axis=-1)
    cv2.imshow('demo', output_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
