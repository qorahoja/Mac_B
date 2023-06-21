import tkinter as tk
import cv2
from PIL import Image, ImageTk

# Haqiqiy foydalanuvchining yuz aniqlovchisini yaratish
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Tkinter oynasini yaratish
window = tk.Tk()
window.title("Face Detection")
window.geometry("800x600")

# OpenCV videoni tomosha qilish uchun funksiya
def show_video():
    video_capture = cv2.VideoCapture(0)  # 0 - birinchi videokamera
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Ranglarni o'zgartirish
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))  # Yuzlarni aniqlash

        # Yuzlarni markalash
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # OpenCV ranglarini PIL ranglariga o'tkazish
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo
        if cv2.waitKey(1) == ord('q'):  # 'q' tugmasini bosganda videoni to'xtatish
            break
    video_capture.release()
    cv2.destroyAllWindows()

# Tkinter oynasidagi rasm joylashuvi
label = tk.Label(window)
label.pack()

# "Start" tugmasini yaratish
start_button = tk.Button(window, text="Start", command=show_video)
start_button.pack()

# Dastur oynasini ochish
window.mainloop()
