#!/usr/local/bin/python3
from tkinter import Tk, Button, Label
from PIL import Image, ImageTk
from requests import get
from json import loads
from io import BytesIO

def load_image():
    try:
        response = get(loads(get('https://randomfox.ca/floof').text)['image'])
        print(response.raise_for_status())
        img_tk = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))
        image_label.config(image=img_tk)
        image_label.image = img_tk
    except Exception as e:
        error_label.config(text=f"Error: {e}")

root = Tk()
root.title("Random fox image")
Button(root, text="Load", command=load_image).pack(pady=5)
image_label = Label(root)
image_label.pack()
error_label = Label(root)
error_label.pack()
root.mainloop()
