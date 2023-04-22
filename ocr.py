import cv2


if __name__ == '__main__':
    img = cv2.imread('./resource/shotcut/shotcut.png')
    thresh,result=cv2.threshold (img, 230, 255, cv2.THRESH_BINARY)
    cv2.imshow("test", result)
    cv2.waitKey(0)

