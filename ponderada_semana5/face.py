from ultralytics import YOLO
import cv2 as cv

camera = cv.VideoCapture(0)
modelo = YOLO("best.pt")

while True:
    _, frame = camera.read()
    resultados = modelo.predict(frame, conf=0.5)
    cv.imshow("Detecção de Objetos", resultados[0].plot())
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()

cv.destroyAllWindows()