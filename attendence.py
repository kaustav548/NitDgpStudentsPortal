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
import os
import csv
from tkinter import filedialog

myData = []
myfilename = []
class Attendance:
    
    
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
            DATE_Entry.delete(0, END)
            DATE_Entry.insert(0,cal.get_date())
            date_window.destroy()
        #========================variables=========================
        self.var_ID1 = StringVar()
        self.var_ID2 = StringVar()
        self.var_name = StringVar()    
        self.var_DATE = StringVar()
        self.var_time = StringVar()
        self.var_status = StringVar()
        #background image:
        bg = Image.open("NIT_Durgapur_Logo.svg.png")
        bg = bg.resize((500,500),Image.LANCZOS)
        self.photobg = ImageTk.PhotoImage(bg)
        
        bg_img = Label(self.root,image = self.photobg)
        bg_img.place(x=0,y=0,width=1537,height=710)
        
        #title
        title_lbl = Label(bg_img,text= "STUDENT ATTENDENCE PORTAL", font=("times new roman",35,"bold"),bg="white",fg="red" )
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
        
        left_inside_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Student info",font =("times new roman",12,"bold"))
        left_inside_frame.place(x=5,y=5,width=720,height = 450)
        
        Student_Id_1_label = Label(left_inside_frame,text = "Registration number :",font=("times new roman",12,"bold"),bg="white")
        Student_Id_1_label.grid(row = 0, column= 0,padx = 10,pady=10,sticky=W)
        
        Student_Id_1_Entry = ttk.Entry(left_inside_frame,textvariable=self.var_ID1,width=20,font=("times new roman",12,"bold"))
        Student_Id_1_Entry.grid(row = 0, column = 1,padx = 10,pady=10,sticky=W )
        
        Student_Id_2_label = Label(left_inside_frame,text = "Roll number :",font=("times new roman",12,"bold"),bg="white")
        Student_Id_2_label.grid(row = 0, column= 2,padx = 10,pady=10,sticky=W)
        
        Student_Id_2_Entry = ttk.Entry(left_inside_frame,textvariable=self.var_ID2,width=20,font=("times new roman",12,"bold"))
        Student_Id_2_Entry.grid(row = 0, column = 3,padx = 10,pady=10,sticky=W )
        
        Name_label = Label(left_inside_frame,text = "Name :",font=("times new roman",12,"bold"),bg="white")
        Name_label.grid(row = 1, column= 0,padx = 10,pady=10,sticky=W)
        
        Name_Entry = ttk.Entry(left_inside_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        Name_Entry.grid(row = 1, column = 1,padx = 10,pady=10,sticky=W )
        
        DATE_label = Label(left_inside_frame,text = "DATE :",font=("times new roman",12,"bold"),bg="white")
        DATE_label.grid(row = 2, column= 0,padx = 10,pady=10,sticky=W)
        
        DATE_Entry = ttk.Entry(left_inside_frame,textvariable=self.var_DATE,width=20,font=("times new roman",12,"bold"))
        DATE_Entry.grid(row = 2, column = 1,padx = 10,pady=10,sticky=W )
        DATE_Entry.insert(0, "dd/mm/yyyy")
        DATE_Entry.bind("<1>", pick_date)
        
        time_label = Label(left_inside_frame,text = "Time :",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row = 3, column= 0,padx = 10,pady=10,sticky=W)
        
        time_Entry = ttk.Entry(left_inside_frame,textvariable=self.var_time,width=20,font=("times new roman",12,"bold"))
        time_Entry.grid(row = 3, column = 1,padx = 10,pady=10,sticky=W )
        time_Entry.insert(0, "Hr:min:sec")
        
        Status_label = Label(left_inside_frame,text="STATUS :",font=("times new roman",13,"bold"),bg="white")
        Status_label.grid(row = 4,column= 0,padx=10,pady=5,sticky=W)
        
        status_combo = ttk.Combobox(left_inside_frame,textvariable=self.var_status,font=("times new roman",12,"bold"),state="readonly",width= 10)
        status_combo["values"]=("Select","Present", "Absent")
        status_combo.current(0)
        status_combo.grid(row =4,column=1,padx=2,pady=10,sticky=W)
        #Button frame
        btn_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Button",font =("times new roman",12,"bold"))
        btn_frame.place(x=5,y=465,width = 720,height= 150)
        
        importcsv_btn = Button(btn_frame,text="Import_csv",command=self.importCsv,width = 16,font=("times new roman",12,"bold"),bg="green",fg = "white")
        importcsv_btn.grid(row =1,column=0,padx=10,pady=10)
        
        exportcsv_btn = Button(btn_frame,text="Export_csv",command=self.exportCsv,width = 16,font=("times new roman",12,"bold"),bg="green",fg = "white")
        exportcsv_btn.grid(row =1,column=1,padx=10,pady=10)
        
        update_btn = Button(btn_frame,text="Update_data",width = 16,font=("times new roman",12,"bold"),bg="green",fg = "white")
        update_btn.grid(row =2,column=1,padx=10,pady=10)
        
        reset_btn = Button(btn_frame,text="Reset_data",command=self.reset_data,width = 16,font=("times new roman",12,"bold"),bg="green",fg = "white")
        reset_btn.grid(row =2,column=2,padx=10,pady=10)
        
        reset_csv_btn = Button(btn_frame,text="Reset_csv",command=self.reset_csv,width = 16,font=("times new roman",12,"bold"),bg="green",fg = "white")
        reset_csv_btn.grid(row =1,column=2,padx=10,pady=10)
        
        reset_base_csv_btn = Button(btn_frame,text="Reset_base_csv",command=self.reset_base_csv,width = 16,font=("times new roman",12,"bold"),bg="green",fg = "white")
        reset_base_csv_btn.grid(row =2,column=0,padx=10,pady=10)
        
        delete_btn = Button(btn_frame,text="Delete_csv", command=self.delete_csv,width = 16,font=("times new roman",12,"bold"),bg="green",fg = "white")
        delete_btn.grid(row =1,column=3,padx=10,pady=10)
        
        insert_btn = Button(btn_frame,text="insert_data",width = 16,font=("times new roman",12,"bold"),bg="green",fg = "white")
        insert_btn.grid(row =2,column=3,padx=10,pady=10)
        
        #right_frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Box",font =("times new roman",12,"bold"))
        Right_frame.place(x=755,y=10,width = 730,height= 640)
        
        # Table Frame
        Table_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Box",font =("times new roman",12,"bold"))
        Table_frame.place(x=5,y=5,width = 720,height= 610)
        
        scroll_x = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.Attendance_Report_table = ttk.Treeview(Table_frame,column = ("Roll No","Registration No","Name","Time","Date","Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Attendance_Report_table.xview)
        scroll_y.config(command=self.Attendance_Report_table.yview)
        
        self.Attendance_Report_table.heading("Roll No",text="Roll No")
        self.Attendance_Report_table.heading("Registration No",text="Reg No")
        self.Attendance_Report_table.heading("Name",text="Name")
        self.Attendance_Report_table.heading("Time",text="Time")
        self.Attendance_Report_table.heading("Date",text="Date")
        self.Attendance_Report_table.heading("Status",text="Attendence")
        self.Attendance_Report_table["show"]="headings"
        
        self.Attendance_Report_table.column("Roll No",width=100)
        self.Attendance_Report_table.column("Registration No",width=100)
        self.Attendance_Report_table.column("Name",width=100)
        self.Attendance_Report_table.column("Time",width=100)
        self.Attendance_Report_table.column("Date",width=100)
        self.Attendance_Report_table.column("Status",width=100)
        
        self.Attendance_Report_table.pack(fill=BOTH,expand=1)
        self.Attendance_Report_table.bind("<ButtonRelease>",self.get_cursor)
    
    #====================Functions================================
    def  fetch_data(self,rows):
        self.Attendance_Report_table.delete(*self.Attendance_Report_table.get_children())
        for i in rows:
            self.Attendance_Report_table.insert("",END,values=i)
    
    def importCsv(self):
        global myData
        global myfilename
        myData.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title= "Import Csv", filetypes=(("CSV file","*.csv"),("All file","*.*")),parent=self.root)
        myfilename = fln
        with open(fln) as myFile:
            Csv = csv.reader(myFile,delimiter=",")
            for i in Csv:
                myData.append(i)
            self.fetch_data(myData)
            
    def exportCsv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("No Data","No data found to be export",parent = self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title= "Import Csv", filetypes=(("CSV file","*.csv"),("All file","*.*")),parent=self.root)
            with open(fln+".csv",mode='w',newline="") as myFile :
                exp_write = csv.writer(myFile,delimiter=",")
                for i in myData:
                    exp_write.writerow(i)
                messagebox.showinfo("Data export","Your data is exported"+os.path.basename(fln)+"Successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent = self.root)
    
    def get_cursor(self,event=""):
        cursor_row = self.Attendance_Report_table.focus()
        content = self.Attendance_Report_table.item(cursor_row)
        rows = content["values"]
        self.var_ID2.set(rows[0]),
        self.var_ID1.set(rows[1]),
        self.var_name.set(rows[2]),
        self.var_time.set(rows[3]),
        self.var_DATE.set(rows[4]),
        self.var_status.set(rows[5])
        
    def reset_csv(self):
        f = open(myfilename, "w")
        f.truncate()
        f.close()
        
    def reset_base_csv(self):
        f = open("kaustav.csv", "w")
        f.truncate()
        f.close()
    
    def delete_csv(self):
        os.remove(myfilename)
    
    def reset_data(self):
        self.var_ID2.set(""),
        self.var_ID1.set(""),
        self.var_name.set(""),
        self.var_time.set("Hr:min:sec"),
        self.var_DATE.set("dd/mm/yyyy"),
        self.var_status.set("Select")
    

                
        
if __name__ == "__main__":
    root = Tk()
    obj1 = Attendance(root)
    root.mainloop()