from PIL import Image, ImageDraw, ImageFont,ImageTk
import random
import os
import datetime
import qrcode
import glob
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import askstring
import PIL. Image
from tkinter import messagebox as mb
import mysql.connector
from tkinter import messagebox


# To create a Window
top=Tk()
top.geometry("700x700")
top.title("Select")

# To Get Logo Onto a Tkinter Window

    
    
        

def student_page():
    top.destroy()
    import student_generator
  
def faculty_page():
    top.destroy()
    import faculty_generator
   

student_button = tk.Button(top,text = "student_page",state=ACTIVE,command = student_page,activeforeground = "white",activebackground = "black",width=20,height=5,font="Algerian").place(x=80,y=250)
faculty_button = tk.Button(top,text = "faculty_page",state=ACTIVE,command = faculty_page,activeforeground = "white",activebackground = "black",width=20,height=5,font="Algerian").place(x=330,y=100)


top.mainloop()   