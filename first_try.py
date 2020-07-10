import cv2
cap = cv2.VideoCapture(0); #веб камерf

cap.set(3, 1280) #размера окна
cap.set(4, 700)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened(): #статус видеопотока

diff = cv2.absdiff(frame1,
frame2) #разницы двух кадров

gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (9, 9), 0)

_, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

dilated = cv2.dilate(thresh, None,
iterations=3)
сontours, _ = cv2.findContours(dilated, cv2.RETR_TREE,
cv2.CHAIN_APPROX_SIMPLE)

for contour in сontours:
(x, y, w, h) = cv2.boundingRect(
contour)

print(cv2.contourArea(contour))

if cv2.contourArea(contour) < 10000:
continue
cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2) # получение прямоугольника из точек
cv2.putText(frame1, "Status: {}".format("Dvigenie"), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3,
cv2.LINE_AA)


cv2.imshow("frame1", frame1)
frame1 = frame2 #
ret, frame2 = cap.read() #

if cv2.waitKey(40) == 27:
break

cap.release()
cv2.destroyAllWindows()
