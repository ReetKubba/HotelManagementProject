from atexit import register
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error


class Registerapp:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #variables declaration
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        


        #bg image
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\dell\Downloads\picc.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        #left image
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\dell\Downloads\irelandhotel.jfif")
        bg_lbl1=Label(self.root,image=self.bg1)
        bg_lbl1.place(x=180,y=110,width=370,height=450)
        

        frame=Frame(self.root,bg="white")
        frame.place(x=550,y=110,width=500,height=450)
        register_lbl=Label(frame,text="Register Now!!",font=("times new roman",20,"bold"),fg="black",bg="white")
        register_lbl.place(x=140,y=20)
        #row
        fname=Label(frame,text="First name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=80)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=110,width=150)

        l_name=Label(frame,text="Last name",font=("times new roman",15,"bold"),bg="white")
        l_name.place(x=275,y=80)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=275,y=110,width=150)

        contact=Label(frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=150)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=180,width=150)


        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email.place(x=275,y=150)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=275,y=180,width=150)

        security_Q=Label(frame,text="Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=220)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your best friend","Your Mother's name")
        self.combo_security_Q.place(x=50,y=250,width=150)
        self.combo_security_Q.current(0)


        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=275,y=220)
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=275,y=250,width=150)


        security_Q=Label(frame,text="Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=220)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=275,y=250,width=150)


        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=290)

        self.txt_confirm=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_confirm.place(x=50,y=320,width=150)


        confirm_pswd=Label(frame,text=" Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=275,y=290)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=275,y=320,width=150)


        ##checkbutton
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree with the terms and conditions",font=("times new roman",11,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=350)

        #button
        img=Image.open(r"C:\Users\dell\Downloads\loginbutton.jfif")
        img=img.resize((200,55),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=20,y=380,width=200)


        img1=Image.open(r"C:\Users\dell\Downloads\registerbutton.png")
        img1=img1.resize((200,55),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=280,y=380,width=180)
    def register_data(self):
        if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_confpass.get()=="" or self.var_pass.get()==0 or self.var_email.get()=="" or self.var_contact.get()=="" or self.var_securityQ.get()=="Select" or self.var_securityA=="":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm Password should be same") 
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree with our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="@@Reet2002",database="demo")    
            my_cursor=conn.cursor()
            #print("connected to my sql server")
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists , Please try with some other email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
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
            messagebox.showinfo("Success","Registered Succesfully")   
    def return_login(self):
        self.root.destroy()                                                                      
if __name__=="__main__":
    root=Tk()
    app=Registerapp(root)
    root.mainloop()
