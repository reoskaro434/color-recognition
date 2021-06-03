from image_recognizer.image_recognizer import ImageRecognizer
from path_getter.path_getter import PathGetter
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter as tk


def show_image():
    my_image = Image.open(file_path[0]).resize((200, 200))
    my_image_tk = ImageTk.PhotoImage(my_image)
    image_label = tk.Label(image=my_image_tk)
    image_label.image = my_image_tk
    image_label.place(x=50, y=50)


def open_file():
    file_path.clear()
    file_path.append(path_getter.get_file_path())

    show_image()


def predict_color():
    messagebox.showinfo("color name", [model.recognize_image(file_path[0])])

    return


if __name__ == '__main__':

    # init necessary variables
    model = ImageRecognizer()
    path_getter = PathGetter()
    file_path = []
    root = tk.Tk()

    # create window app
    canvas = tk.Canvas(root, height=300, width=300)
    canvas.pack()

    frame = tk.Frame(root)
    frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

    buttonOpenFile = tk.Button(root, text="Load Image", padx=10, pady=5, command=open_file)
    buttonOpenFile.pack()

    buttonPredict = tk.Button(root, text="Predict", padx=10, pady=5, command=predict_color)
    buttonPredict.pack()

    root.mainloop()
