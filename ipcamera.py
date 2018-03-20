
import numpy as np
import cv2


cap = cv2.VideoCapture()
cap.open("https://192.168.0.113:8080/video?x.mjpeg")

if not (cap.isOpened()):
	print("Error : Improvise, adapt, overcome")
	cap.release()

else:
	while (True):
		ret, frame = cap.read()
		if not ret:
			print("Error : Cannot read Frame")
			break
		cv2.imshow('frame', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
cv2.destroyAllWindows()