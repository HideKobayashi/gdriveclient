import cv2

# VideoCapture オブジェクトを取得します
capture = cv2.VideoCapture(0)

indexNo = 0
while True:
    ret, frame = capture.read()
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("quit")
        break
    elif cv2.waitKey(1) & 0xFF == ord("c"):
        print(f"save! {indexNo}")
        cv2.imwrite(f"image{indexNo:05d}.jpg", frame)
        indexNo += 1
capture.release()
cv2.destroyAllWindows()
