import tkinter as tk
from tkinter.constants import ANCHOR
from PIL import Image
from PIL import ImageTk
from PIL import ImageEnhance
from tkinter import filedialog
import cv2
import numpy as np

def yellowButton_callback():
    opencvImage = cv2.cvtColor(np.array(originalImage), cv2.COLOR_RGB2BGR)
    opencvImage[:, :, 0] = 20
    global outputImage
    outputImage = Image.fromarray(cv2.cvtColor(opencvImage, cv2.COLOR_BGR2RGB))
    dispayImage(outputImage)

def blueButton_callback():
    opencvImage = cv2.cvtColor(np.array(originalImage), cv2.COLOR_RGB2BGR)
    opencvImage[:, :, 2] = 100
    global outputImage
    outputImage = Image.fromarray(cv2.cvtColor(opencvImage, cv2.COLOR_BGR2RGB))
    dispayImage(outputImage)

def pinkButton_callback():
    opencvImage = cv2.cvtColor(np.array(originalImage), cv2.COLOR_RGB2BGR)
    opencvImage[:, :, 1] = 100
    global outputImage
    outputImage = Image.fromarray(cv2.cvtColor(opencvImage, cv2.COLOR_BGR2RGB))
    dispayImage(outputImage)

def orangeButton_callback():
    opencvImage = cv2.cvtColor(np.array(originalImage), cv2.COLOR_RGB2BGR)
    opencvImage[:, :, 2] = 200
    global outputImage
    outputImage = Image.fromarray(cv2.cvtColor(opencvImage, cv2.COLOR_BGR2RGB))
    dispayImage(outputImage)

def noneButton_callback():
    pass

def dispayImage(displayImage):
    ImagetoDisplay = displayImage.resize((800,500), Image.ANTIALIAS)
    ImagetoDisplay = ImageTk.PhotoImage(ImagetoDisplay)
    showWindow.config(image=ImagetoDisplay)
    showWindow.photo_ref = ImagetoDisplay
    showWindow.pack()

def importButton_callback():
    global originalImage
    filename = filedialog.askopenfilename()
    originalImage = Image.open(filename)
    dispayImage(originalImage)

def saveButton_callback():
    savefile = filedialog.asksaveasfile(defaultextension=".jpg")
    outputImage.save(savefile)

def closeButton_callback():
    window.destroy()

def brightness_callback(brightness_pos):
    brightness_pos = float(brightness_pos)
    print(brightness_pos)
    global outputImage
    enhancer = ImageEnhance.Brightness(originalImage)
    outputImage = enhancer.enhance(brightness_pos)
    dispayImage(outputImage)

def contrast_callback(contrast_pos):
    contrast_pos = float(contrast_pos)
    print(contrast_pos)
    global outputImage
    enhancer = ImageEnhance.Contrast(originalImage)
    outputImage = enhancer.enhance(contrast_pos)
    dispayImage(outputImage)
 
def color_callback(color_pos):
    color_pos = float(color_pos)
    print(color_pos)
    global outputImage
    enhancer = ImageEnhance.Color(originalImage)
    outputImage = enhancer.enhance(color_pos)
    dispayImage(outputImage)

window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.title("IMAGE EDITOR")
window['background']='#8EE5EE'
window.geometry(f'{screen_width}x{screen_height}')

Frame1 = tk.Frame(window, height=20, width=screen_width)
Frame1.pack(anchor=tk.NW)

Frame2 = tk.Frame(window, height=20)
Frame2.pack(anchor=tk.NW)

Frame3 = tk.Frame(window, height=20)
Frame3.pack(anchor=tk.N)

welcome = tk.Label(Frame1, text="WELCOME TO YOUR OWN IMAGE EDITOR", font=("ariel 12 bold"),pady=5, padx=407, bg="#8EE5EE")
welcome.grid(row=0, column=2)

importButton = tk.Button(Frame1 , bg="#FFD700",text="Import", padx=10, pady=5, command=importButton_callback)
importButton.grid(row=0, column=0)

saveButton = tk.Button(Frame1,bg="#FFD700",text="Save", padx=10, pady=5, command=saveButton_callback)
saveButton.grid(row=0, column=1)

closeButton = tk.Button(Frame1,bg="#FFD700", text="Close", padx=32, pady=5, command=closeButton_callback)
closeButton.grid(row=0, column=3)

brightnessSlider = tk.Scale(Frame2, bg="#8ED2C9",fg="black",troughcolor="#006495", label="Brightness", from_=0, to=2, orient=tk.HORIZONTAL, length=screen_width,
                            resolution=0.1, command=brightness_callback)
brightnessSlider.set(1)
brightnessSlider.pack(anchor=tk.N)

contrastSlider = tk.Scale(Frame2, bg="#8ED2C9",fg="black",troughcolor="#006495",label="Contrast", from_=0, to=2, orient=tk.HORIZONTAL, length=screen_width,
                            command=contrast_callback, resolution=0.1)
contrastSlider.set(1)
contrastSlider.pack(anchor=tk.N)

ColorSlider = tk.Scale(Frame2, bg="#8ED2C9",fg="black",troughcolor="#006495",label="Saturation", from_=0, to=2, orient=tk.HORIZONTAL, length=screen_width,
                            resolution=0.1, command=color_callback)
ColorSlider.set(1)
ColorSlider.pack(anchor=tk.N)

yellowButton = tk.Radiobutton(Frame3, bg="#FFD700", text="Yellow Filter",font=("ariel 10 bold"), width=30, value=1, command=yellowButton_callback)
yellowButton.grid(row=0, column=0)

blueButton = tk.Radiobutton(Frame3, bg="#006495", text="Blue Filter",font=("ariel 10 bold"), width=30, value=2, command=blueButton_callback)
blueButton.grid(row=0, column=1)

pinkButton = tk.Radiobutton(Frame3, bg="#EE1289", text="Pink Filter",font=("ariel 10 bold"), width=30, value=3, command=pinkButton_callback)
pinkButton.grid(row=0, column=2)

orangeButton = tk.Radiobutton(Frame3, bg="#FF7D40",text="Orange Filter",font=("ariel 10 bold"), width=30, value=4, command=orangeButton_callback)
orangeButton.grid(row=0, column=3)

noneButton = tk.Radiobutton(Frame3, bg="#474747",fg="white", text="None", width=30,font=("ariel 10 bold"), value=5, command=noneButton_callback)
noneButton.grid(row=0, column=4)
noneButton.select()

showWindow = tk.Label(window)
showWindow.pack()
tk.mainloop() 