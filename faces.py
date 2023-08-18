import cvlearn.FaceMesh as fm
import cv2

cap = cv2.VideoCapture(0)
detector = fm.FaceMeshDetector()

while True:
    ret, frame = cap.read()
    frame, faces = detector.findFaceMesh(frame)

    if faces:
        for face in faces:
            for i in range(len(face)):
                cv2.circle(frame, (face[i][0], face[i][1]), 2, (255,0,255), cv2.FILLED)

    cv2.imshow("result", frame)
    cv2.waitKey(1)