import numpy as np, cv2
from functions import processImages, sendMoveInformation, grayish

# Pobieramy kamere
cam = cv2.VideoCapture(0)

# Utworzenie okna
winName = "Wykrywanie ruchu"
cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)

# Odczytujemy 3 obrazy
t_minus = grayish(cam.read()[1])
t = grayish(cam.read()[1])
t_plus = grayish(cam.read()[1])

while True:
    # Wyswietlamy przetworzony obraz
    (move, img) = processImages(t_minus, t, t_plus)
    cv2.imshow( winName,  img)

    # Wysylamy informacje o wykrytym ruchu
    if move:
        sendMoveInformation("Wykryto ruch!")

    # Odczytujemy kolejny obraz
    t_minus = t
    t = t_plus
    t_plus = grayish(cam.read()[1])

    # Esc = wyjscie
    key = cv2.waitKey(10)
    if key == 27:
        cv2.destroyWindow(winName)
        break