from PIL import Image, ImageDraw, ImageFont,ImageTk
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
top.title("Student Id Card Generator")

# To Get Logo Onto a Tkinter Window
img = PIL.Image.open("Id.png")
img = ImageTk.PhotoImage(img)
panel = Label(top, image=img)
panel.image = img
panel.pack(side = TOP)

# To get Date and Time
d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("  %d-%m-%Y \t %I:%M:%S %p")


# For Labelling
##ourMessage ='Please Provide the Data in Capital Letters and make sure you enter the data properly'
#messageVar = Message(top, text = ourMessage) 
#messageVar.config(bg='lightgreen')
clg_name = Label(top, text = "College Name").place(x = 30,y = 80)
id = Label(top, text = "I'd").place(x = 30,y = 110)
branch = Label(top, text = "Branch").place(x = 30,y = 140)
name = Label(top, text = "Name").place(x = 30, y = 170)
yof = Label(top, text = "Year Of Adm").place(x = 30,y = 200)
dob = Label(top, text = "DOB").place(x = 30,y = 230)
grno = Label(top, text = "GR No.").place(x = 30,y = 260)
blood_group = Label(top, text = "Blood Gr.").place(x = 30,y = 290)
mob_num = Label(top, text = "Mobile Number").place(x = 30,y = 320)
#city = Label(top, text = "City").place(x = 30,y = 320)
#To Get Entered Text in a Entry Widget
str1=tk.StringVar()
str2=tk.StringVar()
str3=tk.StringVar()
str4=tk.StringVar()
str5=tk.StringVar()
str6=tk.StringVar()
str7=tk.StringVar()
str8=tk.StringVar()
str9=tk.StringVar()

#For Entry Widget
e1= ttk.Combobox(top,textvariable=str1,values=["Saraswati college of engineering", "AC Patil college of engineering", "Bharatiya vidya bhavans", "wilson college","SIES","DY Patil","KJ Somaiya","lokmanya Tilak of engineering","pilla's college of engineering","Sardar Patel College of Engineering","Terna college of engineering"]).place(x = 120, y = 80)# Add more colleges as needed
e2 = Entry(top,textvariable=str2).place(x = 120, y = 110)
e3 = Entry(top,textvariable=str3).place(x = 120, y = 140)
e4 = Entry(top,textvariable=str4).place(x = 120, y = 170)
e5 = Entry(top,textvariable=str5).place(x = 120, y = 200)
e6 = Entry(top,textvariable=str6).place(x = 120, y = 230)
e7 = Entry(top,textvariable=str7).place(x = 120, y = 260)
e8 = Entry(top,textvariable=str8).place(x = 120, y = 290)
e9 = Entry(top,textvariable=str9).place(x = 120, y = 320)



def register():

        if str1.get()==""or str2.get()==""or str3.get()=="select":
            messagebox.showerror("error","all field are required")
        elif len(str(str9.get()))<10 or len(str(str9.get()))>10:
            messagebox.showinfo("Phone","phone number should contain 10 digits")


        else:
            conn = mysql.connector.connect(host="Localhost", user="root", password="",database="id_generator")
            my_cursor = conn.cursor()
            query=("select * from student where id=%s")
            value=(str2.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row!=None:
                messagebox.showerror("Error","I'D already exits, please try with another")

            else:
                 my_cursor.execute("insert into student (clg_name,id,branch,name,yof,dob,grno,blood_group,mob_num)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                      str1.get(),
                                                                                      str2.get(),
                                                                                      str3.get(),
                                                                                      str4.get(),
                                                                                      str5.get(),
                                                                                      str6.get(),
                                                                                      str7.get(),
                                                                                      str8.get(),
                                                                                      str9.get()
                                                                                      ))
            conn.commit()
            conn.close()
       #     messagebox.showinfo("Sucess","Register Sucessfully")

            
            image = PIL.Image.new('RGB', (1100,1000), (255, 255, 255))
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype('arial.ttf', size=45)
            #Clg_Name
            (x, y) = (50, 50)
            message = str('Clg_name:- '+str(str1.get()))
            color = 'rgb(0, 0, 0)'
            font = ImageFont.truetype('arial.ttf', size=40)
            draw.text((x, y),message, fill=color, font=font)
            #Idno
            (x, y) = (50, 150)
            message = str('ID:- '+str(str2.get()))
            color = 'rgb(0, 0, 0)' # black color
            font = ImageFont.truetype('arial.ttf', size=40)
            draw.text((x, y), message, fill=color, font=font)
            #Name
            (x, y) = (50, 250)
            message = str('Branch:- '+str(str3.get()))
            color = 'rgb(0, 0, 0)' # black color
            font = ImageFont.truetype('arial.ttf', size=45)
            draw.text((x, y), message, fill=color, font=font)
            #Gender
            (x, y) = (50, 350)
            message = str('Name:- '+str(str4.get()))
            color = 'rgb(0, 0, 0)' # black color 
            draw.text((x, y),message, fill=color, font=font)
            #Age
            (x, y) = (50, 450)
            message = str('YOF:- '+str(str5.get()))
            color = 'rgb(0, 0, 0)' # black color
            draw.text((x, y), message, fill=color, font=font)
            #DOB
            (x, y) = (50, 550)
            message = str('DOB:- '+str(str6.get()))
            draw.text((x, y),  message, fill=color, font=font)
            #Blood  Group
            (x, y) = (50, 650)
            message = str('Grno.:- '+str(str7.get()))
            color = 'rgb(0, 0, 0)' # black color 
            draw.text((x, y), message, fill=color, font=font)
            #Mobile Number
            (x, y) = (50, 750)
            message = str('Blood_group:- '+str(str8.get()))
            color = 'rgb(0, 0, 0)' # black color
            draw.text((x, y), message, fill=color, font=font)
            #Address
            (x, y) = (50, 850)
            message=str('mob_num:- '+str(str9.get()))
            color = 'rgb(0, 0, 0)' # black color 
            draw.text((x, y), message, fill=color, font=font)
            #Date and Time
            (x, y) = (600,800)
            font = ImageFont.truetype('arial.ttf', size=20)
            color = 'rgb(0, 0, 0)' # black color 
            draw.text((x, y),reg_format_date , fill=color, font=font)

    

            image.save(str(str3.get())+'.png')
            img = qrcode.make(str(str1.get())+"\n"+str(str2.get())+"\n"+str(str3.get()))   # this info. is added in QR code, also add other things
            img.save(str(str2.get())+'.bmp')
            til = PIL.Image.open(str3.get()+'.png')
            im = PIL.Image.open(str(str2.get())+'.bmp') #25x25
            im1 = PIL.Image.open("logo.png")#25x25
            til.paste(im1,(640,250))
            til.paste(im,(600,350))
            til.save(str3.get()+'.png')
            mylist=[f for f in glob.glob("*.bmp")]
            os.remove(mylist[0])
            mb.showinfo("Id Card Generator","Your ID card  has been Generated as : ** "+str4.get()+'.png **')
            str1.set("")
            str2.set("")
            str3.set("")
            str4.set("")
            str5.set("")
            str6.set("")
            str7.set("")
            str8.set("")
            str9.set("")
                

    
    

def reset():
    str1.set("")
    str2.set("")
    str3.set("")
    str4.set("")
    str5.set("")
    str6.set("")
    str7.set("")
    str8.set("")
    #str9.set("")

b1 = tk.Button(top,text = "Submit",state=ACTIVE,command = register,activeforeground = "red",activebackground = "pink",font="Baskerville_Old_Face").place(x=100,y=350)
#b2 = tk.Button(top,text = "Submit",state=ACTIVE,command = submit,activeforeground = "red",activebackground = "pink",font="Baskerville_Old_Face").place(x=150,y=320)
b3 = tk.Button(top,text = "Reset",state=ACTIVE,command = reset,activeforeground = "red",activebackground = "pink",font="Baskerville_Old_Face").place(x=200,y=350)

top.mainloop()   
    