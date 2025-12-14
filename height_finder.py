import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import cv2
import math

def open_file():
    global img_path, img
    img_path = filedialog.askopenfilename()
    img = cv2.imread(img_path)
    process_image()

def process_image():
    global points, i,img
    points = []
    i = 0

    def pointer(event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            size = len(points)
            if (size % 3) != 0:
                cv2.line(img, tuple(points[0]), (x, y), (0, 0, 255), 2)
            cv2.circle(img, (x, y), 5, (0, 0, 255), cv2.FILLED)
            points.append([x, y])
            global i

    def slope(pt1, pt2):
        return ((pt2[1] - pt1[1]) / (pt2[0] - pt1[0]))

    def degFinder(points):
        global radian, degree
        pt1, pt2, pt3 = points[-3:]
        m1 = slope(pt1, pt2)
        m2 = slope(pt1, pt3)
        radian = abs(math.atan(((m2 - m1) / (1 + (m1 * m2)))))
        degree = abs(round(math.degrees(radian)))
        global i
        i += 1

    while i != 1:
        if len(points) % 3 == 0 and len(points) != 0:
            degFinder(points)
        cv2.imshow('HeightFinder', img)
        cv2.setMouseCallback('HeightFinder', pointer)

        if cv2.waitKey(1) & 0xFF == ord('z'):
            points = []
            img = cv2.imread(img_path)

    dist = simpledialog.askstring("Input Prompt", "Enter the object's Distance:\t\t\t\t")
    x = (float(dist) * (math.tan(radian)))
    messagebox.showinfo("Answer", "The Height of the Object is :" + str(x))
    cv2.destroyAllWindows()

root = tk.Tk()
root.geometry('600x300')
root.title("Height Finder")

lab1 = tk.Label(text="\nWelcome to HeightFinder\n\nPlease select an Image to proceed:", font=("Helvetica", 18))
lab1.pack()
but1 = tk.Button(root, text="Open Image", command=open_file, width=13, height=2)
but1.pack(pady=70)
root.mainloop()