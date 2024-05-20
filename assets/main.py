from keras.layers import Conv2D, UpSampling2D
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from skimage.color import rgb2lab, lab2rgb
from skimage.transform import resize
from skimage.io import imsave
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import os
import io
import glob
from PIL import Image, ImageTk

def output_model(path, window, output_label, status_lab):
    
    size = 256
    disp_size = 256
    img_channels = 1
    np.random.seed(42)
    status_lab.configure(text="Colorizing the image...")

    model = tf.keras.models.load_model(
        'colorize_autoencoder.model',
        custom_objects=None,
        compile=True)

    img1_color=[]

    img1 = img_to_array(load_img(path=path))
    img1 = resize(img1 ,(size,size))
    img1_color.append(img1)

    img1_color = np.array(img1_color, dtype=float)
    img1_color = rgb2lab(1.0/255*img1_color)[:,:,:,0]
    img1_color = img1_color.reshape(img1_color.shape+(1,))

    pred = model.predict(img1_color)
    pred = pred*128

    result = np.zeros((size, size, 3))
    result[:,:,0] = img1_color[0][:,:,0]
    result[:,:,1:] = pred[0]
    result = lab2rgb(result)
    result = cv2.resize(result, (disp_size, disp_size))
    
    output_pl = Image.fromarray(np.uint8(result*255))
    output_tk = ImageTk.PhotoImage(output_pl)
    output_label.configure(image=output_tk)
    output_label.photo = output_tk
    status_lab.configure(text="DONE")