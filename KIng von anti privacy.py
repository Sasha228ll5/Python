import cv2


video_path = "D:\downloads\KingVona.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Не вдалося відкрити відео.")
    exit()

cv2.namedWindow("Video", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    ret, frame = cap.read()
    if not ret:

        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue


    cv2.imshow("Video", frame)


    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()