from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import random
from tkinter import messagebox

class Detailsroom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        lbl_title=Label(self.root,text="ROOM ADDING DEPARTMENT",font=("times new roman",38,"bold"),bg="seashell4",fg="white")
        lbl_title.place(x=0,y=0,width=1295,height=60)

        img2=Image.open(r"C:\Users\dell\Downloads\savoylogoo.png")
        img2=img2.resize((100,60),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbling.place(x=0,y=0,width=100,height=60)

        img3=Image.open(r"C:\Users\dell\Downloads\toputscreenshot.png")
        img3=img3.resize((600,360),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbling=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lbling.place(x=0,y=295,width=590,height=360)

        img5=Image.open(r"C:\Users\dell\Downloads\rom.jpeg")
        img5=img5.resize((600,260),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lbling=Label(self.root,image=self.photoimg5,bd=0,relief=RIDGE)
        lbling.place(x=550,y=420,width=690,height=230)




        LabelFrameLeft=Label(self.root,bd=2,relief=RIDGE,text="ADDING NEW ROOMS",font=("times new roman",20,"bold"),padx=2)
        LabelFrameLeft.place(x=10,y=60,width=525)

        

        LabelFrameLeftd=Label(self.root,bd=2,relief=RIDGE,font=("times new roman",20,"bold"),padx=2,pady=6)
        LabelFrameLeftd.place(x=10,y=95,width=525,height=200)

        #Floor
        lbl_floor=Label(LabelFrameLeftd,text="Floor",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_Floor=StringVar()
        entry_floor=ttk.Entry(LabelFrameLeftd,textvariable=self.var_Floor,width=16,font=("times new roman",14,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)

        #Room no
        lbl_Roomno=Label(LabelFrameLeftd,text="Room No",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbl_Roomno.grid(row=1,column=0,sticky=W)

        self.var_RoomNo=StringVar()        
        entry_Roomno=ttk.Entry(LabelFrameLeftd,textvariable=self.var_RoomNo,width=16,font=("times new roman",14,"bold"))
        entry_Roomno.grid(row=1,column=1,sticky=W)

        #Room Type
        lbl_RoomType=Label(LabelFrameLeftd,text="Room Type",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)

        self.var_RoomType=StringVar()
        entry_RoomType=ttk.Entry(LabelFrameLeftd,textvariable=self.var_RoomType,width=16,font=("times new roman",14,"bold"))
        entry_RoomType.grid(row=2,column=1,sticky=W)

        btn_frame=Frame(LabelFrameLeftd,bd=2,relief=RIDGE)
        btn_frame.place(x=10,y=120,width=525,height=54)

        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("times new roman",20,"bold"),bg="seashell4",fg="white",width=7)
        btnAdd.grid(row=0,column=0,padx=5,pady=6)

        btnUpdate=Button(btn_frame,text="UPDATE",command=self.update,font=("times new roman",20,"bold"),bg="seashell4",fg="white",width=7)
        btnUpdate.grid(row=0,column=1,padx=5,pady=6)

        btnDelete=Button(btn_frame,text="DELETE",command=self.deletedata,font=("times new roman",20,"bold"),bg="seashell4",fg="white",width=7)
        btnDelete.grid(row=0,column=2,padx=5,pady=6)

        btnReset=Button(btn_frame,text="RESET",command=self.reset,font=("times new roman",20,"bold"),bg="seashell4",fg="white",width=7)
        btnReset.grid(row=0,column=3,padx=5,pady=6)

        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="      VIEW DETAILS AND SEARCH HISTORY                     ",font=("times new roman",20,"bold"),padx=2)
        Table_Frame.place(x=555,y=60,width=640,height=400)


        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_Frame,column=("floor","roomno","roomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("roomType",text="RoomType")


        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomType",width=100)

        self.room_table.pack(fill=BOTH,expand=1)
        self.fetch_data()


    def add_data(self):
        if self.var_Floor.get()=="" or self.var_RoomNo.get()=="" or self.var_RoomType.get()=="" :
            messagebox.showerror("Error","All fields are to be entered",parent=self.root)
        else:
            try:

                conn=mysql.connector.connect(host="localhost",username="root",password="@@Reet2002",database="demo")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                        self.var_Floor.get(),                                                                                            
                                                                                        self.var_RoomNo.get(),
                                                                                        self.var_RoomType.get(), 
                                                                                                   ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New room added successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning","Something went wrong")


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@@Reet2002",database="demo")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
                self.room_table.delete(*self.room_table.get_children())
                for i in rows:
                        self.room_table.insert("",END,values=i)
                conn.commit()
        conn.close()  

    def update(self):
        if self.var_RoomNo.get()=="":
                messagebox.showerror("Error","Please eneter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="@@Reet2002",database="demo")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(

                                                                                        self.var_Floor.get(),
                                                                                        self.var_RoomType.get(),
                                                                                        self.var_RoomNo.get()
                                                                                                                                                                              

            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update"," Details have been updated successfully",parent=self.root)



    def deletedata(self):
        deletedata=messagebox.askyesno("HMS","Do You want to delete this ?",parent=self.root)
        if deletedata>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="@@Reet2002",database="demo")
            my_cursor=conn.cursor()
            query="delete from details where roomNo=%s"
            value=(self.var_RoomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not deletedata:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_Floor.set(row[0])  
        self.var_RoomNo.set(row[1])
        self.var_RoomType.set(row[2])


    def reset(self):
        
        self.var_RoomNo.set(""),
        self.var_Floor.set(""),
        self.var_RoomType.set("")

if __name__=="__main__":
    root=Tk()
    app=Detailsroom(root)
    root.mainloop()