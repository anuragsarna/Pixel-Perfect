import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import glob
import cv2
from main import output_model
import customtkinter as ctk
import tkinter.font as tkfont


window = ttk.Window(themename='darkly')
window.title("Pixel Perfect")
window.geometry('1000x600')

bg = ttk.PhotoImage(file = "assets/bg1.png") 
  
# Show image using label 
label1 = ttk.Label(window, image = bg) 
label1.place(x = 0, y = 0) 

path = None
person_img = 'assets/u2.jpg'
img_size = 256
custom_font = tkfont.Font(family="Helvetica", size=12, weight="bold")


def import_img(labelname):
    global path
    path = filedialog.askopenfile().name
    image_org = Image.open(path).resize((img_size,img_size))
    image = ImageTk.PhotoImage(image_org)
    labelname.configure(image=image)
    labelname.photo = image
    status_lab.configure(text="Click on Color Image.")


window.columnconfigure(0, weight=5)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=5)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)

input_pl = Image.open(person_img).resize((img_size,img_size))
input_tk = ImageTk.PhotoImage(input_pl)
input_label = ttk.Label(image=input_tk)

status_lab = ttk.Label(anchor="center", text="Please Import image.")

output_pl = Image.open(person_img).resize((img_size,img_size))
output_tk = ImageTk.PhotoImage(output_pl)
output_label = ttk.Label(image=output_tk,)

import_button = ttk.Button(window, text='Import image', command=lambda:import_img(input_label))
title = ttk.Label(window, text="Autoencoder-Driven Colorization: Transforming Monochrome Images to RGB Spectrums", font=custom_font)
colorize_button = ttk.Button(window, text='Color Image', command=lambda:output_model(path=path, window=window, output_label=output_label, status_lab=status_lab))


#--------------------------------Placement-----------------------------------------------

title.grid(row=0, column=0, columnspan=3)
import_button.grid(row=1, column=0)
input_label.grid(row=2, column=0)
status_lab.grid(row=2, column=1, sticky='n')
output_label.grid(row=2, column=2)
colorize_button.grid(row=2, column=1)

window.mainloop()