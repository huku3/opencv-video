import cv2

# cap = cv2.VideoCapture("image/kuma.mp4")
cap = cv2.VideoCapture(0)
# 0にするとカメラが起動する

fps = int(cap.get(cv2.CAP_PROP_FPS))
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
video = cv2.VideoWriter("video.mp4", fourcc, fps, (w, h))
while True:
    ret, frame = cap.read()

    # print(ret, frame)
    if ret is False:
        break
    cv2.imshow("Image", frame)
    video.write(frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
