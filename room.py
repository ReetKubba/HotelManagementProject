from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk

import mysql.connector
from time import strftime
from datetime import datetime
from mysql.connector import Error
import random
from tkinter import messagebox

class RoomBooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        #variables
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noOfdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()



        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",38,"bold"),bg="seashell4",fg="white")
        lbl_title.place(x=0,y=0,width=1295,height=60)

        img2=Image.open(r"C:\Users\dell\Downloads\savoylogoo.png")
        img2=img2.resize((100,60),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbling.place(x=0,y=0,width=100,height=60)

        LabelFrameLeft=Label(self.root,bd=2,relief=RIDGE,font=("times new roman",20,"bold"),padx=2,pady=6)
        LabelFrameLeft.place(x=10,y=60,width=425,height=480)


#customer contact
        lbl_Cust_contact=Label(LabelFrameLeft,text="Customer contact",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbl_Cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(LabelFrameLeft,textvariable=self.var_contact,width=16,font=("times new roman",14,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

#fetch data button
        btnFetchData=Button(LabelFrameLeft,text="FETCH DATA",command=self.Fetch_contact,font=("times new roman",12,"bold"),bg="seashell4",fg="white",width=10)
        btnFetchData.place(x=320,y=4,height=30,width=100)

#check in date
        check_in_date=Label(LabelFrameLeft,text="Check in Date:",font=("times new roman",14,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        txtcheck_in_date=ttk.Entry(LabelFrameLeft,width=20,textvariable=self.var_checkin,font=("times new roman",14,"bold"))
        txtcheck_in_date.grid(row=1,column=1)

#check out date
        lbl_Check_out=Label(LabelFrameLeft,text="Check out Date:",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbl_Check_out.grid(row=2,column=0,sticky=W)

        txt_check_out=ttk.Entry(LabelFrameLeft,width=20,textvariable=self.var_checkout,font=("times new roman",14,"bold"))
        txt_check_out.grid(row=2,column=1)

#Room type
        label_RoomType=Label(LabelFrameLeft,text="Room Type:",font=("times new roman",14,"bold"),padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="@@Reet2002",database="demo")
        my_cursor=conn.cursor()
        my_cursor.execute("select roomtype from details")
        ide=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(LabelFrameLeft,font=("times new roman",14,"bold"),textvariable=self.var_roomtype,width=18,state="readonly")
        combo_RoomType["value"]=ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

#Available room
        lblRoomAvailable=Label(LabelFrameLeft,text="Available Room",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="@@Reet2002",database="demo")
        my_cursor=conn.cursor()
        my_cursor.execute("select roomno from details")
        rows=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(LabelFrameLeft,font=("times new roman",14,"bold"),textvariable=self.var_roomavailable,width=18,state="readonly")
        combo_RoomType["value"]=rows
        combo_RoomType.current(0)
        combo_RoomType.grid(row=4,column=1)


#Meal  
        lblMeal=Label(LabelFrameLeft,text="Meal",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)

        txtMeal=ttk.Entry(LabelFrameLeft,width=20,textvariable=self.var_meal,font=("times new roman",14,"bold"))
        txtMeal.grid(row=5,column=1)

#noOfdays
        lbldays=Label(LabelFrameLeft,text="No of days:",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbldays.grid(row=6,column=0,sticky=W)

        txtMeal=ttk.Entry(LabelFrameLeft,width=20,textvariable=self.var_noOfdays,font=("times new roman",14,"bold"))
        txtMeal.grid(row=6,column=1)


#Paid tax
        lblNoofDays=Label(LabelFrameLeft,text="Paid Tax",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblNoofDays.grid(row=7,column=0,sticky=W)

        txtNoofDays=ttk.Entry(LabelFrameLeft,width=20,textvariable=self.var_paidtax,font=("times new roman",14,"bold"))
        txtNoofDays.grid(row=7,column=1)


#Sub total       
        lblNoofDays=Label(LabelFrameLeft,text="Sub Total",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblNoofDays.grid(row=8,column=0,sticky=W)

        txtNoofDays=ttk.Entry(LabelFrameLeft,width=20,textvariable=self.var_actualtotal,font=("times new roman",14,"bold"))
        txtNoofDays.grid(row=8,column=1)


#TotalCost      
        lblNoofDays=Label(LabelFrameLeft,text="Total Cost",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblNoofDays.grid(row=9,column=0,sticky=W)

        txtNoofDays=ttk.Entry(LabelFrameLeft,width=20,textvariable=self.var_total,font=("times new roman",14,"bold"))
        txtNoofDays.grid(row=9,column=1)
        btnBill=Button(LabelFrameLeft,text="BILL",command=self.Total,font=("times new roman",13,"bold"),bg="seashell4",fg="white",width=4)
        btnBill.grid(row=9,column=2,padx=5,pady=6,sticky=W)


        btn_frame=Frame(LabelFrameLeft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=380,width=412,height=48)

        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("times new roman",20,"bold"),bg="seashell4",fg="white",width=12)
        btnAdd.grid(row=0,column=0,padx=5,pady=6)

        btnUpdate=Button(btn_frame,text="UPDATE",command=self.update,font=("times new roman",20,"bold"),bg="seashell4",fg="white",width=12)
        btnUpdate.grid(row=0,column=1,padx=5,pady=6)

        btn_frame1=Frame(LabelFrameLeft,bd=2,relief=RIDGE)
        btn_frame1.place(x=0,y=430,width=412,height=48)

        btnDelete=Button(btn_frame1,text="DELETE",command=self.deletedata,font=("times new roman",20,"bold"),bg="seashell4",fg="white",width=12)
        btnDelete.grid(row=0,column=0,padx=5,pady=6)

        btnReset=Button(btn_frame1,text="RESET",command=self.reset,font=("times new roman",20,"bold"),bg="seashell4",fg="white",width=12)
        btnReset.grid(row=0,column=1,padx=5,pady=6)
#right side image
        img3=Image.open(r"C:\Users\dell\Downloads\dublinn.png")
        img3=img3.resize((500,225),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbling=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lbling.place(x=680,y=70,width=600,height=225)


#Table frame
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="                         VIEW DETAILS AND SEARCH HISTORY                     ",font=("times new roman",20,"bold"),padx=2)
        Table_Frame.place(x=435,y=260,width=910,height=400)


        lblSearchby=Label(Table_Frame,text="SEARCH BY:",font=("times new roman",14,"bold"),bg="seashell4",fg="white")
        lblSearchby.grid(row=0,column=0,sticky=W,padx=2)

        self.Search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.Search_var,font=("times new roman",14,"bold"),width=18)
        combo_Search["value"]=("Contact","Roomavailable")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_Search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_Search,font=("times new roman",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)


        btnSearch=Button(Table_Frame,text="SEARCH",command=self.search,font=("times new roman",15,"bold"),bg="seashell4",fg="white",width=8)
        btnSearch.grid(row=0,column=3,padx=7)

        btnShowAll=Button(Table_Frame,text="SHOW ALL",command=self.fetch_data,font=("times new roman",15,"bold"),bg="seashell4",fg="white",width=8)
        btnShowAll.grid(row=0,column=4,padx=7)

        details_Table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_Table.place(x=0,y=50,width=800,height=300)

        scroll_x=ttk.Scrollbar(details_Table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_Table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_Table,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check_In")
        self.room_table.heading("checkout",text="Check_Out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room no")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="noOfdays")


        self.room_table["show"]="headings"


        self.room_table.column("contact",width=120)
        self.room_table.column("checkin",width=120)
        self.room_table.column("checkout",width=120)
        self.room_table.column("roomtype",width=120)
        self.room_table.column("roomavailable",width=120)
        self.room_table.column("meal",width=120)
        self.room_table.column("noOfdays",width=120)

        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        self.room_table.pack(fill=BOTH,expand=1)
     
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter the contact number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="@@Reet2002",database="demo")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","This number not found",parent=self.root)
            else:
                conn.commit()
                conn.close()
                
                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=435,y=70,width=300,height=190)

                lblName=Label(showDataframe,text="Name:",font=("times new roman",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("times new roman",12,"bold"))
                lbl.place(x=90,y=0)

                conn=mysql.connector.connect(host="localhost",username="root",password="@@Reet2002",database="demo")
                my_cursor=conn.cursor()
                query=("select gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblgender=Label(showDataframe,text="Gender:",font=("times new roman",12,"bold"))
                lblgender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("times new roman",12,"bold"))
                lbl2.place(x=90,y=30)

                conn=mysql.connector.connect(host="localhost",username="root",password="@@Reet2002",database="demo")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblemail=Label(showDataframe,text="Email:",font=("times new roman",12,"bold"))
                lblemail.place(x=0,y=60)

                lbl3=Label(showDataframe,text=row,font=("times new roman",12,"bold"))
                lbl3.place(x=90,y=60)

                conn=mysql.connector.connect(host="localhost",username="root",password="@@Reet2002",database="demo")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblNationality=Label(showDataframe,text="Nationality:",font=("times new roman",12,"bold"))
                lblNationality.place(x=0,y=90)

                lbl4=Label(showDataframe,text=row,font=("times new roman",12,"bold"))
                lbl4.place(x=90,y=90)

                conn=mysql.connector.connect(host="localhost",username="root",password="@@Reet2002",database="demo")
                my_cursor=conn.cursor()
                query=("select address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lbladdress=Label(showDataframe,text="Address:",font=("times new roman",12,"bold"))
                lbladdress.place(x=0,y=120)

                lbl5=Label(showDataframe,text=row,font=("times new roman",12,"bold"))
                lbl5.place(x=90,y=120)


    def add_data(self):
        if self.var_roomtype.get()=="select" or  self.var_checkin.get()=="" or self.var_checkout.get()=="" or self.var_noOfdays.get()=="" or self.var_roomavailable.get()=="" or self.var_meal.get()=="" :
            messagebox.showerror("Error","All fields are to be entered",parent=self.root)
        else:
            try:

                conn=mysql.connector.connect(host="localhost",username="root",password="@@Reet2002",database="demo")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_contact.get(),                                                                                            
                                                                                        self.var_checkin.get(),
                                                                                        self.var_checkout.get(),
                                                                                        self.var_roomtype.get(),
                                                                                        self.var_roomavailable.get(),
                                                                                        self.var_meal.get(),
                                                                                        self.var_noOfdays.get() 
                                                                                                   ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Details added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning","Something went wrong")


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@@Reet2002",database="demo")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
                self.room_table.delete(*self.room_table.get_children())
                for i in rows:
                    self.room_table.insert("",END,values=i)
                conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0])  
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noOfdays.set(row[6])
    def update(self):
        if self.var_contact.get()=="":
                messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="@@Reet2002",database="demo")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(

                                                                                                                                            self.var_checkin.get(),
                                                                                                                                            self.var_checkout.get(),
                                                                                                                                            self.var_roomtype.get(),
                                                                                                                                            self.var_roomavailable.get(),
                                                                                                                                            self.var_meal.get(),
                                                                                                                                            self.var_noOfdays.get(),
                                                                                                                                            self.var_contact.get()
                                                                                                                                                                             

                                                                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details have been updated successfully",parent=self.root)

    def deletedata(self):
        deletedata=messagebox.askyesno("HMS","Do You want to delete this ?",parent=self.root)
        if deletedata>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="@@Reet2002",database="demo")
            my_cursor=conn.cursor()
            query="delete from room where contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not deletedata:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_roomtype.set("select"),
        self.var_checkout.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noOfdays.set(""),
        self.var_total.set(""),
        self.var_actualtotal.set(""),
        self.var_paidtax.set("")



    def Total(self):


        if self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single":
            q1=float(30000)
            q2=float(70000)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double":
            q1=float(40000)
            q2=float(80000)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxury":
            q1=float(40000)
            q2=float(100000)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single":
            q1=float(50000)
            q2=float(70000)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double":
            q1=float(50000)
            q2=float(80000)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxury":
            q1=float(50000)
            q2=float(100000)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single":
            q1=float(60000)
            q2=float(70000)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double":
            q1=float(60000)
            q2=float(80000)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        else:
            q1=float(60000)
            q2=float(100000)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@@Reet2002",database="demo")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room where "+str(self.Search_var.get())+" LIKE '%"+str(self.txt_Search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()





    
  
    
if __name__=="__main__":
    root=Tk()
    app=RoomBooking(root)
    root.mainloop()