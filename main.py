from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
import time
from time import strftime
from student import Student
from attendence import Attendance
import os
import cv2
import numpy as np
from tkinter import messagebox
import mysql.connector
        
class face_recognisation_System:
    
    
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
            
        
        #background image:
        bg = Image.open("NIT_Durgapur_Logo.svg.png")
        bg = bg.resize((500,500),Image.LANCZOS)
        self.photobg = ImageTk.PhotoImage(bg)
        
        bg_img = Label(self.root,image = self.photobg)
        bg_img.place(x=0,y=0,width=1537,height=710)
        
        #title
        title_lbl = Label(bg_img,text= "ATTENDENCE SYSTEM", font=("times new roman",35,"bold"),bg="white",fg="red" )
        title_lbl.place(x=300,y=0,width=930,height=45)
        
        lbl = Label(root, font=("times new roman",35,"bold"),bg="white",fg="blue")
        lbl.place(x=1230,y=0,width=300,height=45)
        time()
        
        lbld = Label(root, font=("times new roman",35,"bold"),bg="white",fg="blue")
        lbld.place(x=0,y=0,width=300,height=45)
        date()
        
        #Student details input:
        stuimg = Image.open("NIT_Durgapur_Logo.svg.png")
        stuimg = stuimg.resize((150,150),Image.LANCZOS)
        self.photostuimg = ImageTk.PhotoImage(stuimg)
        #student details
        b1 = Button(bg_img,image=self.photostuimg,command=self.student_details,cursor="hand2")
        b1.place(x=300,y=50,width =150,height=150)
        
        b1_1 = Button(bg_img,text="Student details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue")
        b1_1.place(x=300,y=200,width =150,height=30)
        
        #Dataset photo
        b2 = Button(bg_img,image=self.photostuimg,command=self.open_img,cursor="hand2")
        b2.place(x=200,y=250,width =150,height=150)
        
        b2_1 = Button(bg_img,text="DataSet Photos",command=self.open_img,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue")
        b2_1.place(x=200,y=400,width =150,height=30)
        
        #Training
        b2 = Button(bg_img,image=self.photostuimg,command=self.train_classifier,cursor="hand2")
        b2.place(x=300,y=450,width =150,height=150)
        
        b2_1 = Button(bg_img,text="Training",command=self.train_classifier,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue")
        b2_1.place(x=300,y=600,width =150,height=30)
        
        # Developer
        b2 = Button(bg_img,image=self.photostuimg,cursor="hand2")
        b2.place(x=1080,y=450,width =150,height=150)
        
        b2_1 = Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue")
        b2_1.place(x=1080,y=600,width =150,height=30)
        
        # Attendance
        b2 = Button(bg_img,image=self.photostuimg,command=self.Attendance,cursor="hand2")
        b2.place(x=1180,y=250,width =150,height=150)
        
        b2_1 = Button(bg_img,text="Attendance",command=self.Attendance,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue")
        b2_1.place(x=1180,y=400,width =150,height=30)
        
        # face_recognition
        b2 = Button(bg_img,image=self.photostuimg,command=self.face_recog,cursor="hand2")
        b2.place(x=1080,y=50,width =150,height=150)
        
        b2_1 = Button(bg_img,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue")
        b2_1.place(x=1080,y=200,width =150,height=30)
        
    #========================Function========================================
    
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def open_img(self):
        os.startfile("data")
        
    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces = []
        ids = []
        
        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img,'uint8')
            id = str(os.path.split(image)[1].split('.')[1])
            id = int(id.replace("CH",""))
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids = np.array(ids)
        
        #==================Train the classifier and save=================
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset completed")
    
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord = []
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))
                id = str(id)
                nid = id[:2]+"CH"+id[2:]
                conn = mysql.connector.connect(host="localhost",port="3305",username="root",password="Blank548#@+nit.dgp",database="face_recognition")
                my_cursor = conn.cursor()
                
                my_cursor.execute("select NAME from student_details where ROLLNO = %s",(nid,))
                i = my_cursor.fetchone()
                i = "+".join(i)
                
                my_cursor.execute("select ROLLNO from student_details where ROLLNO = %s",(nid,))
                s = my_cursor.fetchone()
                s = "+".join(s)
                
                my_cursor.execute("select REGNO from student_details where ROLLNO = %s",(nid,))
                t = my_cursor.fetchone()
                t = "+".join(t)
                if confidence>77:
                    cv2.putText(img,f'Roll : {s}',(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f'RegNo : {t}',(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f'Name : {i}',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,s,t)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f'Unknown',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord = [x,y,w,h]
            return coord
        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.read("classifier.xml")
        # (0) for defaiult (1) for connected camera (url) for cctv camera
        video_cap = cv2.VideoCapture(0)
        
        while True :
            ret,img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Face Recognition",img)
            
            if cv2.waitKey(1)==13 :
                break
        video_cap.release()
        cv2.destroyAllWindows()
    
    #=========================attendence================================
    def mark_attendence(self,i,s,t):
        with open("kaustav.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list=[]
            H = datetime.now().strftime("%H")
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if ((s not in name_list) and (t not in name_list) and (i not in name_list) and (H not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString =now.strftime("%H:%M:%S")
                f.writelines(f"\n{s},{t},{i},{dtString},{d1},Present")
                
    def Attendance(self):
        self.new_window = Toplevel(self.root)
        self.app=Attendance(self.new_window)
                    
                    
                
        

        
if __name__ == "__main__":
    root = Tk()
    obj1 = face_recognisation_System(root)
    root.mainloop()