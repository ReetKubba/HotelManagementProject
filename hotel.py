from tkinter import *
from PIL import Image,ImageTk
from customer import Customerclass
import mysql.connector
from mysql.connector import Error
from room import RoomBooking
from details import Detailsroom


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        #1st image
        img1=Image.open(r"C:\Users\dell\Downloads\savoyentrance.png")
        img2=img1.resize((1150,180),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=1550,height=180)

        img3=Image.open(r"C:\Users\dell\Downloads\SVYLOGO.png")
        img4=img3.resize((260,180),Image.ANTIALIAS)
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

        details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=22,font=("times new roman",14,"bold"),bg="white",fg="seashell4",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="REPORT",width=22,font=("times new roman",14,"bold"),bg="white",fg="seashell4",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="white",fg="seashell4",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)


        #mainimage
        img5=Image.open(r"C:\Users\dell\Downloads\lob1.png")
        img6=img5.resize((1100,420),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        lbling=Label(self.root,image=self.photoimg6,bd=4,relief=RIDGE)
        lbling.place(x=250,y=230,width=1100,height=420)


        img7=Image.open(r"C:\Users\dell\Downloads\poool.png")
        img8=img7.resize((255,210),Image.ANTIALIAS)
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

    
if __name__=="__main__":
    root=Tk()
    app=HotelManagementSystem(root)
    root.mainloop()