from logging import root
import os
from tkinter import *
from tkinter import ttk
import tkinter as Tk
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector



def main():
    win=Tk.Tk()
    app=Login_window(win)
    win.mainloop()



class Login_window:


    def __init__(self,root):
         self.root=root
         self.root.title("Login")
         self.root.geometry("1550x800+0+0")

     #    self.bg = ImageTk.PhotoImage(file="background.png")
    #     bg_lbl = Label(self.root, image=self.bg)
   #      bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)


         frame=Frame(self.root,bg="black")
         frame.place(x=550,y=120,width=400,height=450)

         get_str=Label( frame ,text="Login Details",font=("times new roman",25,"bold"),fg="white",bg="black")
         get_str.place(x=100,y=50)

         username=lbl=Label(frame,text="E-Mail",font=("times new roman",15,"bold"),fg="white",bg="black")
         username.place(x=30,y=130)

         self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
         self.txtuser.place(x=35,y=158,width=300)



         password = lbl = Label(frame, text="PASSWORD", font=("times new roman", 15, "bold"), fg="white", bg="black")
         password.place(x=30, y=200)

        
    
         self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"),show="*")
         self.txtpass.place(x=35, y=230, width=300)
         

         loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
         loginbtn.place(x=120,y=280,width=150,height=35)

         registerbtn = Button(frame, text="New User Register",command=self.register_window, font=("times new roman", 13, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
         registerbtn.place(x=30, y=320, width=150, height=35)

         forgetbtn = Button(frame, text="Forgot Password",command=self.forgot_password_window, font=("times new roman", 13, "bold"),borderwidth=0, fg="white",bg="black", activeforeground="white", activebackground="black")
         forgetbtn.place(x=30, y=350, width=150, height=35)



    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):

        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("error","all the field required")

        elif self.txtuser.get()=="adithi" and self.txtpass.get()=="123456":
            messagebox.showinfo("sucess","welccome ")


        else:
            conn = mysql.connector.connect(host="Localhost", user="root", password="",database="id_generator")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s and password=%s")
            value=(self.txtuser.get(),self.txtpass.get())
            my_cursor.execute(query,value)

            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                messagebox.showinfo("sucess","welccome ")
                self.root.destroy()
                conn.commit()
            conn.close()

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","select security Question")
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","please enter a answer")
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error","please enter the new password")
        else:
            conn = mysql.connector.connect(host="Localhost", user="root", password="",  database="id_generator")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","please enter correct answer")
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()

                messagebox.showinfo("Info","Your password has been reset,please login with new password")




    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter email address to reset password")
        else:
            conn = mysql.connector.connect(host="Localhost", user="root", password="", database="id_generator")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
           # print(row)

            if row==None:
                messagebox.showerror("My Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+580+150")
                self.root2.configure(bg="#4dff4d")


                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="black",bg="#4dff4d")
                l.place(x=0,y=10,relwidth=1)

                security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"),bg="#4dff4d", fg="black")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2,font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ( "select", "your birth place", "your bestfriend name", "your pet name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Select Answer", font=("times new roman", 15, "bold"), bg="#4dff4d", fg="black")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)

                new_password= Label(self.root2, text="New Password", font=("times new roman", 15, "bold"),bg="#4dff4d", fg="black")
                new_password.place(x=50, y=220)

                self.txt_new_password = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_new_password.place(x=50, y=250, width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman", 15, "bold"),fg="white",bg="green")
                btn.place(x=125,y=300)



class Register():
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        self.var_fname=StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()



        self.bg=ImageTk.PhotoImage(file="register background.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=300,y=60,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="white",bg="black")
        register_lbl.place(x=20,y=20)

        #----------------------------------------------------------------------

        fname=Label(frame,text=" Name",font=("times new roman",15,"bold"),bg="black",fg="white")
        fname.place(x=50,y=100)

        self.txt_fname=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Address",font=("times new roman",15,"bold"),bg="black",fg="white")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="black",fg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email-ID",font=("times new roman",15,"bold"),bg="black",fg="white")
        email.place(x=370,y=170)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="black",fg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("select","your birth place","your bestfriend name","your pet name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text=" Security Answer",font=("times new roman",15,"bold"),bg="black",fg="white")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370 ,y=270, width=250)

        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold") ,bg="black",fg="white")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_pass, font=("times new roman", 15),show="*")
        self.txt_pswd.place(x=50, y=340, width=250)

        comfirm_pswd = Label(frame, text=" Comfirm Password", font=("times new roman", 15, "bold"), bg="black",fg="white")
        comfirm_pswd.place(x=370, y=310)

        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_confpass, font=("times new roman", 15),show="*")
        self.txt_pswd.place(x=370, y=340, width=250)

        #self.var_check=IntVar()
        #checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Term And Condition",font=("times new roman", 15, "bold"), bg="black",fg="white",onvalue=1,offvalue=0)
        #checkbtn.place(x=50,y=380)



        img=Image.open(r"register background.png")
        img=img.resize((200,150),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",bg="black",activebackground="black")
        b1.place(x=200,y=380,width=300)

       # img1 = Image.open(r"login now.png")
        #img1 = img1.resize((200, 70), Image.ANTIALIAS)
        #self.photoimage1 = ImageTk.PhotoImage(img1)
        #b1 = Button(frame, image=self.photoimage1,command=self.return_login, borderwidth=0, cursor="hand2", bg="black",activebackground="black")
        #b1.place(x=350, y=460, width=300)

    def register_data(self):
        if self.var_fname.get()==""or self.var_email.get()==""or self.var_securityQ.get()=="select":
            messagebox.showerror("error","all field are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password and comfirm password must be same")
        elif len(str(self.txt_contact.get()))<10 or len(str(self.txt_contact.get()))>10:
            messagebox.showinfo("Phone","phone number should contain 10 digits")
        else:
            conn=mysql.connector.connect(host="Localhost",user="root",password="",database="id_generator")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","user already exits, please try another email")
            else:
                my_cursor.execute("insert into register (name,address,contact,email,securityQ,securityA,password)values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                      ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Sucess","Register Sucessfully")

    def return_login(self):
        self.root.destroy()






if __name__ == '__main__':
    main()
    from select_2 import*
    root.mainloop()
#-----------------------------------------------------------------------------