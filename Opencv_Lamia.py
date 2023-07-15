import fnmatch
from tkinter import *
from tkinter import filedialog
import customtkinter
from PIL import ImageTk,Image
import numpy as np
import cv2


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.title('Task 1')
root.geometry('600x600')
root.pack_propagate(0)


def open_file():
    global my_image
    root.filename= filedialog.askopenfilename(initialdir="/download",title="Select image")
    my_image= ImageTk.PhotoImage(Image.open(root.filename).resize((400,300),Image.ADAPTIVE))
    my_image_label=Label(image=my_image).place(x=270,y=150)
   

def Bluring():
    Gaussian = cv2.GaussianBlur(np.array(my_image), (7, 7), 0)

def Grayscale():
    my_image=np.array(np.rot90(my_image,-1))
    gray_image = cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY)

Question_Label=Label(root,text="What effect do you want to apply to it?",font=("Time Roman",15)).place(x=250,y=460)
Bluring=customtkinter.CTkButton(master=root,text="Blur Image",width=120,height=30,fg_color="#D35B58",hover_color="#C77C78",command=Bluring).place(x=150,y=350)
GrayScale_B=customtkinter.CTkButton(master=root,text="Grayscale image",width=120,height=30,fg_color="#D35B58",hover_color="#C77C78",command=Grayscale).place(x=350,y=400)
Flip_B=customtkinter.CTkButton(master=root,text="Flip image",width=120,fg_color="#D35B58",hover_color="#C77C78").place(x=150,y=400)
Rotate_B=customtkinter.CTkButton(master=root,text="Rotate image",width=120,fg_color="#D35B58",hover_color="#C77C78").place(x=350,y=350)
Resize_B=customtkinter.CTkButton(master=root,text="Resize image",width=120,fg_color="#D35B58",hover_color="#C77C78").place(x=150,y=450)
shifting_B=customtkinter.CTkButton(master=root,text="Shifting image",width=120,fg_color="#D35B58",hover_color="#C77C78").place(x=350,y=450)

prompt_Label=Label(root,text="Please Upload your image:",font=("Time Roman",15)).place(x=270,y=25)
Upload_button=customtkinter.CTkButton(master=root,text="Upload your picture",width=120,fg_color="#2F5597",hover_color="#8FAADC",command=open_file).place(x=250,y=50)


root.mainloop()