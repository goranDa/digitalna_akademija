import cv2
from PIL import Image
import glob

kaskada = "haarcascade_frontalface_default.xml"
kaskadaLice = cv2.CascadeClassifier(kaskada)

images = [cv2.imread(file) for file in glob.glob("slike/*.jpg")]

brojac = 0
for n in range(0, len(images)):
    slika = images[n]
    brojac = brojac +1
    crnoBijelo = cv2.cvtColor(slika, cv2.COLOR_BGR2GRAY)

    lica = kaskadaLice.detectMultiScale(
        crnoBijelo,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (30, 30)
    )
    for (x, y, w, h) in lica:
        izrezana = crnoBijelo[y:y+h, x:x+w]
        mala = cv2.resize(izrezana,(300,300))
        ime = "ImeUcenika" + str(brojac) + ".jpg"
        brojac = brojac + 1
        cv2.imwrite(ime, mala)
        cv2.waitKey(0)
