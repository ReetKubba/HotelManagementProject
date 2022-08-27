from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Registerapp
import mysql.connector
from mysql.connector import Error
from customer import Customerclass
from hotel import HotelManagementSystem
from room import RoomBooking
from details import Detailsroom
def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        #1st image
        img1=Image.open(r"C:\Users\dell\Downloads\savoyentrance.png")
        img2=img1.resize((1150,180),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=1550,height=180)

        img3=Image.open(r"C:\Users\dell\Downloads\SVYLOGO.png")
        img4=img3.resize((260,180),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lbling=Label(self.root,image=self.photoimg4,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=250,height=180)

        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM                  ",font=("times new roman",40,"bold"),bg="seashell4",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=180,width=1550,height=50)

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=230,width=250,height=430)

        ##btn frame
        lbl_menu=Label(self.root,text="MENU",font=("times new roman",20,"bold"),bg="seashell4",fg="white",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=230,width=250)

        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=250,height=190)

        #buttons
        cust_btn=Button(btn_frame,text="CUSTOMER",width=22,font=("times new roman",14,"bold"),command=self.cust_details,bg="white",fg="seashell4",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",width=22,font=("times new roman",14,"bold"),command=self.roombooking,bg="white",fg="seashell4",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",width=22,font=("times new roman",14,"bold"),command=self.details_room,bg="white",fg="seashell4",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="REPORT",width=22,font=("times new roman",14,"bold"),bg="white",fg="seashell4",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",width=22,font=("times new roman",14,"bold"),bg="white",fg="seashell4",command=self.logout,bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)


        #mainimage
        img5=Image.open(r"C:\Users\dell\Downloads\lob1.png")
        img6=img5.resize((1100,420),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        lbling=Label(self.root,image=self.photoimg6,bd=4,relief=RIDGE)
        lbling.place(x=250,y=230,width=1100,height=420)


        img7=Image.open(r"C:\Users\dell\Downloads\poool.png")
        img8=img7.resize((255,210),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        lbling=Label(self.root,image=self.photoimg8,bd=4,relief=RIDGE)
        lbling.place(x=0,y=455,width=255,height=210)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app1=Customerclass(self.new_window)        


      

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=RoomBooking(self.new_window)

    
    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=Detailsroom(self.new_window)
    def logout(self):
        self.root.destroy()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\dell\Downloads\picc.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=480,y=100,width=340,height=420)

        img1=Image.open(r"C:\Users\dell\Downloads\logo.jfif")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbling1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lbling1.place(x=600,y=105,width=100,height=100)
        
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=120)

        username=lbl=Label(frame,text="Username",font=("times new roman",12,"bold"),fg="white",bg="black")
        username.place(x=60,y=162)

        self.txtuser=ttk.Entry(frame,font=("times new roman",12,"bold"))
        self.txtuser.place(x=40,y=182,width=270)
        print(self.txtuser.get())
        password=lbl=Label(frame,text="Password",font=("times new roman",12,"bold"),fg="white",bg="black")
        password.place(x=60,y=212)

        self.txtpass=ttk.Entry(frame,font=("times new roman",14,"bold"))
        self.txtpass.place(x=40,y=232,width=270)
#icon image
        img2=Image.open(r"C:\Users\dell\Downloads\userr.jfif")
        img2=img2.resize((22,22),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbling1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lbling1.place(x=520,y=260,width=22,height=22)

        img3=Image.open(r"C:\Users\dell\Downloads\lock.jfif")
        img3=img3.resize((22,22),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbling1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lbling1.place(x=520,y=310,width=22,height=22)

        #login button
        loginbtn=Button(frame,text="Login",relief=RAISED,command=self.login,cursor="hand2",font=("times new roman",15,"bold"),bd=3,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=90,y=277,width=160)
        #register button
        registerbtn=Button(frame,command=self.register_window,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=17,y=330,width=160)
        #forgetpassbtn
        registerbtn=Button(frame,text="Forgot Password",command=self.forgot_pass_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=13,y=355,width=160)
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Registerapp(self.new_window)
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required ")
        #elif self.txtuser.get()=="Reet" and self.txtpass.get()=="@@Reet2002":
        # messagebox.showinfo("success","Welcome to hotel management system")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="@@Reet2002",database="demo")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and pass=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                                     ))
            print(self.txtuser.get())
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username or password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
#**************reset********
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="@@Reet2002",database="demo")
            my_cursor=conn.cursor()
            query1=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value1=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query1,value1)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update register set pass=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset , You can login with the new password",parent=self.root2)
                self.root2.destroy()
#*****************forgot password window***********************
    def forgot_pass_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="@@Reet2002",database="demo")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("My Error","Please enter valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="FORGOT PASSWORD",font=("times new roman",20,"bold"),fg="white",bg="black")
                l.place(x=0,y=10,relwidth=1)


                security_Q=Label(self.root2,text="Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your best friend","Your Mother's name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)


                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)
                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="black")
                btn.place(x=140,y=290)
    def return_login(self):
        self.root.destroy()

    def hotel_screen(self):
        self.new_window=Toplevel(self.root)
        self.app1=HotelManagementSystem(self.new_window)  


if __name__=="__main__":
    main()