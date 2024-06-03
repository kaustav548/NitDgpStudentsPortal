from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
import time
from time import strftime
from tkcalendar import*
from tkinter import messagebox
import mysql.connector
import cv2 



class Student:
    
    
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("National Institute of Technology Attendence System:")
        
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)
            
        def date():
            datezx = datetime.today().date()
            lbld.config(text = datezx)
            lbld.after(1000, date)
            
        def pick_date(event):
            global cal,date_window
            
            
            date_window = Toplevel()
            date_window.grab_set()
            date_window.title("Choose Date of Birth")
            date_window.geometry('250x220+590+370')
            cal = Calendar(date_window,selectmode = "day" , date_pattern = "mm/dd/y" )
            cal.place(x=0,y=0)
            
            submit_btn = Button(date_window,text="Submit",command = grab_date)
            submit_btn.place(x = 80,y=190)
        
        def grab_date():
            DOB_Entry.delete(0, END)
            DOB_Entry.insert(0,cal.get_date())
            date_window.destroy()
        #========================variables=========================
        self.var_dep = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_ID1 = StringVar()
        self.var_ID2 = StringVar()
        self.var_name = StringVar()
        self.var_div = StringVar()
        self.var_DOB = StringVar()
        self.var_sex = StringVar()
        self.var_mail1 = StringVar()
        self.var_mail2 = StringVar()
        self.var_p1 = StringVar()
        self.var_p2 = StringVar()
        self.var_choise = StringVar()
        self.var_result = StringVar()
        
        
        #background image:
        bg = Image.open("NIT_Durgapur_Logo.svg.png")
        bg = bg.resize((500,500),Image.LANCZOS)
        self.photobg = ImageTk.PhotoImage(bg)
        
        bg_img = Label(self.root,image = self.photobg)
        bg_img.place(x=0,y=0,width=1537,height=710)
        
        #title
        title_lbl = Label(bg_img,text= "STUDENT MANAGEMENT SYSTEM", font=("times new roman",35,"bold"),bg="white",fg="red" )
        title_lbl.place(x=300,y=0,width=930,height=45)
        
        lbl = Label(root, font=("times new roman",35,"bold"),bg="white",fg="blue")
        lbl.place(x=1230,y=0,width=300,height=45)
        time()
        
        lbld = Label(root, font=("times new roman",35,"bold"),bg="white",fg="blue")
        lbld.place(x=0,y=0,width=300,height=45)
        date()
        
        main_frame = LabelFrame(bg_img,bd=2,bg="blue")
        main_frame.place(x=11,y=50,width=1500,height = 659)
        
        #LabelFrame
        #left_frame
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font =("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width = 730,height= 640)
        
        #current cource:
        current_cource_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current cource",font =("times new roman",12,"bold"))
        current_cource_frame.place(x=5,y=5,width = 720,height= 150)
        
        dep_label = Label(current_cource_frame,text = "Cource",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row = 0, column= 0,padx = 10)
        
        dep_combo = ttk.Combobox(current_cource_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width= 17)
        dep_combo["values"]=("Select cource","B.tech","B.tech + M.tech (D D )","M.tech","Phd")
        dep_combo.current(0)
        dep_combo.grid(row =0,column=1,padx=2,pady=10,sticky=W)
        
        #year
        year_label = Label(current_cource_frame,text = "Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row = 0, column= 5,padx = 10)
        
        year_combo = ttk.Combobox(current_cource_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width= 17)
        year_combo["values"]=("Select year","2023-2024","2022-2023","2021-2022","2020-2021","2019-2020")
        year_combo.current(0)
        year_combo.grid(row =0,column=6,padx=2,pady=10,sticky=W)
        
        # Semister
        Semister_label = Label(current_cource_frame,text = "Semister",font=("times new roman",12,"bold"),bg="white")
        Semister_label.grid(row = 1, column= 0,padx = 10)
        
        Semister_combo = ttk.Combobox(current_cource_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly",width= 17)
        Semister_combo["values"]=("Select Semister","01","02","03","04","05","06","07","08","09","10")
        Semister_combo.current(0)
        Semister_combo.grid(row =1,column=1,padx=2,pady=10,sticky=W)
        
        #class studdent information panel:
        class_student_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class student infotrmation",font =("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=160,width = 720,height= 300)
        
        Student_Id_1_label = Label(class_student_frame,text = "Registration number :",font=("times new roman",12,"bold"),bg="white")
        Student_Id_1_label.grid(row = 0, column= 0,padx = 10,pady=10,sticky=W)
        
        Student_Id_1_Entry = ttk.Entry(class_student_frame,textvariable=self.var_ID1,width=20,font=("times new roman",12,"bold"))
        Student_Id_1_Entry.grid(row = 0, column = 1,padx = 10,pady=10,sticky=W )
        
        Student_Id_2_label = Label(class_student_frame,text = "Roll number :",font=("times new roman",12,"bold"),bg="white")
        Student_Id_2_label.grid(row = 0, column= 2,padx = 10,pady=10,sticky=W)
        
        Student_Id_2_Entry = ttk.Entry(class_student_frame,textvariable=self.var_ID2,width=20,font=("times new roman",12,"bold"))
        Student_Id_2_Entry.grid(row = 0, column = 3,padx = 10,pady=10,sticky=W )
        
        Name_label = Label(class_student_frame,text = "Name :",font=("times new roman",12,"bold"),bg="white")
        Name_label.grid(row = 1, column= 0,padx = 10,pady=10,sticky=W)
        
        Name_Entry = ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        Name_Entry.grid(row = 1, column = 1,padx = 10,pady=10,sticky=W )
        
        Division_label = Label(class_student_frame,text = "Division :",font=("times new roman",12,"bold"),bg="white")
        Division_label.grid(row = 1, column= 2,padx = 10,pady=10,sticky=W)
        
        Division_Entry = ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        Division_Entry.grid(row = 1, column = 3,padx = 10,pady=10,sticky=W )
        
        DOB_label = Label(class_student_frame,text = "DOB:",font=("times new roman",12,"bold"),bg="white")
        DOB_label.grid(row = 2, column= 0,padx = 10,pady=10,sticky=W)
        
        DOB_Entry = ttk.Entry(class_student_frame,textvariable=self.var_DOB,width=20,font=("times new roman",12,"bold"))
        DOB_Entry.grid(row = 2, column = 1,padx = 10,pady=10,sticky=W )
        DOB_Entry.insert(0, "dd/mm/yyyy")
        DOB_Entry.bind("<1>", pick_date)
        
        Gender_label = Label(class_student_frame,text = "Gender:",font=("times new roman",12,"bold"),bg="white")
        Gender_label.grid(row = 2, column= 2,padx = 10,pady=10,sticky=W)
        
        Gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_sex,font=("times new roman",12,"bold"),state="readonly",width= 17)
        Gender_combo["values"]=("Choose Gender","Male","Female","Others")
        Gender_combo.current(0)
        Gender_combo.grid(row =2,column=3,padx=2,pady=10,sticky=W)
        
        Email_Id_1_label = Label(class_student_frame,text = "Work Email :",font=("times new roman",12,"bold"),bg="white")
        Email_Id_1_label.grid(row = 3, column= 0,padx = 10,pady=10,sticky=W)
        
        Email_Id_1_Entry = ttk.Entry(class_student_frame,textvariable=self.var_mail1,width=20,font=("times new roman",12,"bold"))
        Email_Id_1_Entry.grid(row = 3, column = 1,padx = 10,pady=10,sticky=W )
        
        Email_Id_2_label = Label(class_student_frame,text = "Personal Email :",font=("times new roman",12,"bold"),bg="white")
        Email_Id_2_label.grid(row = 3, column= 2,padx = 10,pady=10,sticky=W)
        
        Email_Id_2_Entry = ttk.Entry(class_student_frame,textvariable=self.var_mail2,width=20,font=("times new roman",12,"bold"))
        Email_Id_2_Entry.grid(row = 3, column = 3,padx = 10,pady=10,sticky=W )
        
        Phone_1_label = Label(class_student_frame,text = "Phone 1 :",font=("times new roman",12,"bold"),bg="white")
        Phone_1_label.grid(row = 4, column= 0,padx = 10,pady=10,sticky=W)
        
        Phone_1_Entry = ttk.Entry(class_student_frame,textvariable=self.var_p1,width=20,font=("times new roman",12,"bold"))
        Phone_1_Entry.grid(row = 4, column = 1,padx = 10,pady=10,sticky=W )
        
        Phone_2_label = Label(class_student_frame,text = "Phone 2 :",font=("times new roman",12,"bold"),bg="white")
        Phone_2_label.grid(row = 4, column= 2,padx = 10,pady=10,sticky=W)
        
        Phone_2_Entry = ttk.Entry(class_student_frame,textvariable=self.var_p2,width=20,font=("times new roman",12,"bold"))
        Phone_2_Entry.grid(row = 4, column = 3,padx = 10,pady=10,sticky=W )
        
        #Radio Button
        self.var_Radio1= StringVar()
        Radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_Radio1,text="Take photo sample", value="YES")
        Radiobtn1.grid(row = 6, column = 0)
        
        Radiobtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_Radio1,text="No photo sample", value="NO")
        Radiobtn2.grid(row = 6, column = 1)
        
        #Button frame
        btn_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Button",font =("times new roman",12,"bold"))
        btn_frame.place(x=5,y=465,width = 720,height= 150)
        
        Take_btn = Button(btn_frame,text="Take Photo Sample",command=self.generate_dataset,width = 16,font=("times new roman",12,"bold"),bg="green",fg = "white")
        Take_btn.grid(row =0,column=1,padx=10,pady=10)
        
        Update_P_btn = Button(btn_frame,text="Update photo Sample",command=self.generate_dataset,width = 16,font=("times new roman",12,"bold"),bg="green",fg = "white")
        Update_P_btn.grid(row =0,column=2,padx=10)
        
        save_btn = Button(btn_frame,text="Save",command=self.add_data,width = 16,font=("times new roman",12,"bold"),bg="green",fg = "white")
        save_btn.grid(row =1,column=0,padx=10,pady=10)
        
        update_btn = Button(btn_frame,text="Update",command=self.update_data,width = 16,font=("times new roman",12,"bold"),bg="green",fg = "white")
        update_btn.grid(row =1,column=1,padx=10,pady=10)
        
        delete_btn = Button(btn_frame,text="Delete",command=self.Delete_data,width = 16,font=("times new roman",12,"bold"),bg="green",fg = "white")
        delete_btn.grid(row =1,column=2,padx=10,pady=10)
        
        reset_btn = Button(btn_frame,text="Reset",command=self.Reset_data,width = 16,font=("times new roman",12,"bold"),bg="green",fg = "white")
        reset_btn.grid(row =1,column=3,padx=10,pady=10)
        
        #right_frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font =("times new roman",12,"bold"))
        Right_frame.place(x=755,y=10,width = 730,height= 640)
        
        img_right = Image.open("NIT_Durgapur_Logo.svg.png")
        img_right = img_right.resize((130,130),Image.LANCZOS)
        self.photo_img_right = ImageTk.PhotoImage(img_right)
        
        f_img = Label(Right_frame,image = self.photo_img_right)
        f_img.place(x=0,y=0,width=720,height=130)
        
        Serch_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Data set",font =("times new roman",12,"bold"))
        Serch_frame.place(x=5,y=140,width = 720,height= 70)
        
        Serch_label = Label(Serch_frame,text="Search By :",font=("times new roman",13,"bold"),bg="white")
        Serch_label.grid(row = 0,column= 0,padx=10,pady=5,sticky=W)
        
        serch_combo = ttk.Combobox(Serch_frame,textvariable=self.var_choise,font=("times new roman",12,"bold"),state="readonly",width= 10)
        serch_combo["values"]=("Select","Registration No", "Roll No","Name")
        serch_combo.current(0)
        serch_combo.grid(row =0,column=1,padx=2,pady=10,sticky=W)
        
        Serch_Entry = ttk.Entry(Serch_frame,textvariable=self.var_result,width=18,font=("times new roman",12,"bold"))
        Serch_Entry.grid(row = 0, column = 2,padx = 10,pady=10,sticky=W )
        
        Serch_btn = Button(Serch_frame,text="Search",command=self.SerchResults,width = 15,font=("times new roman",12,"bold"),bg="green",fg = "white")
        Serch_btn.grid(row =0,column=3,padx=10,pady=10)
        
        showAll_btn = Button(Serch_frame,text="Show All",command=self.Fletch_data,width = 15,font=("times new roman",12,"bold"),bg="green",fg = "white")
        showAll_btn.grid(row =0,column=4,padx=10,pady=10)
        
        # Table Frame
        Table_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font =("times new roman",12,"bold"))
        Table_frame.place(x=5,y=215,width = 730,height= 350)
        
        scroll_x = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.Student_table = ttk.Treeview(Table_frame,column = ("Roll No","Registration No","Name","Cource","Year","Semister","Division","DOB","Gender","WorkMail","Email","Phone1","Phone2","Photos"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        
        self.Student_table.heading("Roll No",text="Roll No")
        self.Student_table.heading("Registration No",text="Reg No")
        self.Student_table.heading("Name",text="Name")
        self.Student_table.heading("Cource",text="Cource")
        self.Student_table.heading("Year",text="Year")
        self.Student_table.heading("Semister",text="Semister")
        self.Student_table.heading("Division",text="Division")
        self.Student_table.heading("DOB",text="DOB")
        self.Student_table.heading("Gender",text="Gender")
        self.Student_table.heading("WorkMail",text="Workmail")
        self.Student_table.heading("Email",text="Email")
        self.Student_table.heading("Phone1",text="Phone1")
        self.Student_table.heading("Phone2",text="Phone2")
        self.Student_table.heading("Photos",text="Photos")
        self.Student_table["show"]="headings"
        
        self.Student_table.column("Roll No",width=100)
        self.Student_table.column("Registration No",width=100)
        self.Student_table.column("Name",width=100)
        self.Student_table.column("Cource",width=100)
        self.Student_table.column("Year",width=100)
        self.Student_table.column("Semister",width=100)
        self.Student_table.column("Division",width=100)
        self.Student_table.column("DOB",width=100)
        self.Student_table.column("Gender",width=100)
        self.Student_table.column("WorkMail",width=100)
        self.Student_table.column("Email",width=100)
        self.Student_table.column("Phone1",width=100)
        self.Student_table.column("Phone2",width=100)
        self.Student_table.column("Photos",width=100)
        
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease>",self.get_cursor)
        self.Fletch_data()
        
    # ========================Function=========================    
    
    def add_data(self):
        if self.var_dep.get()=="Select cource" or self.var_name.get()=="" or self.var_ID1.get() == "" or self.var_ID2.get() == "" or self.var_mail1.get() =="" or self.var_p1.get() =="":
            messagebox.showerror("ERROR!","All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",port="3305",username="root",password="Blank548#@+nit.dgp",database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                          
                    self.var_ID2.get(),
                    self.var_ID1.get(),
                    self.var_name.get(),
                    self.var_dep.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_div.get(),
                    self.var_DOB.get(),
                    self.var_sex.get(),
                    self.var_mail1.get(),
                    self.var_mail2.get(),
                    self.var_p1.get(),
                    self.var_p2.get(), 
                    self.var_Radio1.get()
                                                                                        ))
                
                conn.commit()
                self.Fletch_data()
                conn.close()
                messagebox.showinfo("Successfull","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent = self.root)
                
    #========================Fletch data========================
    def Fletch_data(self):
        conn = mysql.connector.connect(host="localhost",port="3305",username="root",password="Blank548#@+nit.dgp",database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from Student_details")
        data = my_cursor.fetchall()
        
        if len(data) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for i in data:
                self.Student_table.insert("",END,values=i)
            conn.commit()
            conn.close()
    
    def SerchResults(self):
        conn = mysql.connector.connect(host="localhost",port="3305",username="root",password="Blank548#@+nit.dgp",database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from Student_details")
        data = my_cursor.fetchall()
        
        if len(data) != 0:
            if self.var_choise.get() == "Registration No":
                self.Student_table.delete(*self.Student_table.get_children())
                for i in data:
                    if i[1] == self.var_result.get():
                        self.Student_table.insert("",END,values=i)
                conn.commit()
                conn.close()
            if self.var_choise.get() ==  "Roll No":
                self.Student_table.delete(*self.Student_table.get_children())
                for i in data:
                    if i[0] == self.var_result.get():
                        self.Student_table.insert("",END,values=i)
                conn.commit()
                conn.close()
            if self.var_choise.get() == "Name":
                self.Student_table.delete(*self.Student_table.get_children())
                for i in data:
                    if i[2] == self.var_result.get():
                        self.Student_table.insert("",END,values=i)
                conn.commit()
                conn.close()
    #==========================get cursor=============================
    def get_cursor(self,event=""):
        cursor_focus = self.Student_table.focus()
        content=self.Student_table.item(cursor_focus)
        data = content["values"]
        
        self.var_ID2.set(data[0]),
        self.var_ID1.set(data[1]),
        self.var_name.set(data[2]),
        self.var_dep.set(data[3]),
        self.var_year.set(data[4]),
        self.var_sem.set(data[5]),
        self.var_div.set(data[6]),
        self.var_DOB.set(data[7]),
        self.var_sex.set(data[8]),
        self.var_mail1.set(data[9]),
        self.var_mail2.set(data[10]),
        self.var_p1.set(data[11]),
        self.var_p2.set(data[12]),
        self.var_Radio1.set(data[13])
        
    # update function
    def update_data(self):
        if self.var_dep.get()=="Select cource" or self.var_name.get()=="" or self.var_ID1.get() == "" or self.var_ID2.get() == "" or self.var_mail1.get() =="" or self.var_p1.get() =="":
            messagebox.showerror("ERROR!","All fields are required",parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to update?",parent=self.root)
                if Update >0:
                    conn = mysql.connector.connect(host="localhost",port="3305",username="root",password="Blank548#@+nit.dgp",database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student_details set REGNO = %s,NAME =%s,COURCE = %s,YEAR =%s,SEM =%s , DIVISION =%s, DOB =%s , SEX =%s, WORKMAIL =%s,EMAIL =%s,PHONE1=%s,PHONE2=%s,PHOTOS =%s where ROLLNO =%s",(
                        self.var_ID1.get(),
                        self.var_name.get(),
                        self.var_dep.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_div.get(),
                        self.var_DOB.get(),
                        self.var_sex.get(),
                        self.var_mail1.get(),
                        self.var_mail2.get(),
                        self.var_p1.get(),
                        self.var_p2.get(), 
                        self.var_Radio1.get(),
                        self.var_ID2.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.Fletch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To{str(es)}",parent=self.root)
    #delete data
    def Delete_data(self):
        if self.var_ID2.get()=="":
            messagebox.showerror("Error","Roll No Required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete","Do you want to DELETE entry?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",port="3305",username="root",password="Blank548#@+nit.dgp",database="face_recognition")
                    my_cursor = conn.cursor()
                    sql = "delete from student_details where ROLLNO = %s"
                    val=(self.var_ID2.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.Fletch_data()
                conn.close()
                messagebox.showinfo("Delete","successfully deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To{str(es)}",parent=self.root)
    
    #reset function
    def Reset_data(self):
        self.var_ID2.set(""),
        self.var_ID1.set(""),
        self.var_name.set(""),
        self.var_dep.set("Select cource"),
        self.var_year.set("Select year"),
        self.var_sem.set("Select Semister"),
        self.var_div.set(""),
        self.var_DOB.set("dd/mm/yyyy"),
        self.var_sex.set("Choose Gender"),
        self.var_mail1.set(""),
        self.var_mail2.set(""),
        self.var_p1.set(""),
        self.var_p2.set(""),
        self.var_Radio1.set("")
        
    # ===============================Generate Data Set Take Photo Samples===================================
    def generate_dataset (self):
        if self.var_dep.get()=="Select cource" or self.var_name.get()=="" or self.var_ID1.get() == "" or self.var_ID2.get() == "" or self.var_mail1.get() =="" or self.var_p1.get() =="":
            messagebox.showerror("ERROR!","All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",port="3305",username="root",password="Blank548#@+nit.dgp",database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student_details")
                my_result = my_cursor.fetchall()
                my_cursor.execute("update student_details set REGNO = %s,NAME =%s,COURCE = %s,YEAR =%s,SEM =%s , DIVISION =%s, DOB =%s , SEX =%s, WORKMAIL =%s,EMAIL =%s,PHONE1=%s,PHONE2=%s,PHOTOS =%s where ROLLNO =%s",(
                        self.var_ID1.get(),
                        self.var_name.get(),
                        self.var_dep.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_div.get(),
                        self.var_DOB.get(),
                        self.var_sex.get(),
                        self.var_mail1.get(),
                        self.var_mail2.get(),
                        self.var_p1.get(),
                        self.var_p2.get(), 
                        self.var_Radio1.get(),
                        self.var_ID2.get()
                    ))
                id_P = self.var_ID2.get()
                
                conn.commit()
                self.Fletch_data()
                self.Reset_data()
                conn.close()
                
                #=============Load predifined data=================
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def Face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    face = face_classifier.detectMultiScale(gray,1.3,5) #scaling factor = 1.3 ; Minimum neighbour = 5;
                    
                    for (x,y,w,h) in face:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                # (0) = own camera (url) for other .
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,My_frame = cap.read()
                    if Face_cropped(My_frame) is not None :
                        img_id+=1
                        face = cv2.resize(Face_cropped(My_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id_P)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("croped face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("result","generating data set")
                
            except Exception as es:
                messagebox.showerror("Error",f"Due To{str(es)}",parent=self.root)
                        
                
                    
                    
                
                    
                
        
            
            
if __name__ == "__main__":
    root = Tk()
    obj1 = Student(root)
    root.mainloop()