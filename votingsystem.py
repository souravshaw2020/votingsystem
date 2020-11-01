from Tkinter import *
import ttk
import tkMessageBox
import sqlite3
import pandas as pd
from pandastable import Table
db=sqlite3.connect('nominee_details.db')
cur=db.cursor()
db1=sqlite3.connect('stud_details.db')
cur1=db1.cursor()
db2=sqlite3.connect('nom_house_record.db')
cur2=db2.cursor()
db3=sqlite3.connect('voter_details.db')
cur3=db3.cursor()
db4=sqlite3.connect('admin_details.db')
cur4=db4.cursor()
global ohc,ohvc,whc,whvc,ghc,ghvc
ohc=0
ohvc=0
whc=0
whvc=0
ghc=0
ghvc=0

try:
    cur2.execute('CREATE TABLE IF NOT EXISTS House_Record_Details(house text primary key,captain integer,vicecaptain integer)')
    cur2.execute('INSERT INTO House_Record_Details(house,captain,vicecaptain)VALUES(?,?,?)',('Orange House',ohc,ohvc))
    db2.commit()
    cur2.execute('INSERT INTO House_Record_Details(house,captain,vicecaptain)VALUES(?,?,?)',('White House',whc,whvc))
    db2.commit()
    cur2.execute('INSERT INTO House_Record_Details(house,captain,vicecaptain)VALUES(?,?,?)',('Green House',ghc,ghvc))
    db2.commit()
except sqlite3.IntegrityError:
    pass



#-----------------------------------------------------------------------------------------------------------------------------------------------------------
class MainWindow(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)
        self.title("eVoting System")#Set the title of the main window
        self.winfo_geometry()
        self.configure(background="#1569C7")
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        container=Frame(self) #This container contains all the pages
        container.pack(fill="both",expand=True)
        container.winfo_geometry()
        container.grid_rowconfigure(0,weight=1)  #Make the cell in grid which cover the entire window
        container.grid_columnconfigure(0,weight=1)  #Make the cell in grid which cover the entire window
        self.frames={}  #Create a dictionary for pages we want to navigate
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        for F in (Login_Page,Admin_Page,White_House,Orange_House,Green_House):  #For each page

            frame=F(parent=container,controller=self) #Create the page for each window
            self.frames[F]=frame  #Store into frames
            frame.grid(row=0,column=0,sticky='nsew')  #Grid it to container
        self.show_frame(Login_Page)  #Let the first page will be Login Page
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def show_frame(self,page_name):
        frame=self.frames[page_name]
        frame.tkraise()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
class Login_Page(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller=controller
        # -----------------------------------------------------------------------------------------------------------------------------------------------------------
        wid=self.winfo_screenwidth()
        self.top = Frame(self,width=1000, height=160, bd=3, bg="#2B3856", relief='raise')
        self.top.pack(side=TOP, fill=BOTH)
        self.middle = Frame(self,width=1000, height=730, bd=0, bg="#1569C7",relief='raise')
        self.middle.pack(side=TOP, fill=BOTH)
        self.bottom = Frame(self,width=1000, height=80, bd=0, bg="#1569C7")
        self.bottom.pack(side=BOTTOM, fill=BOTH)
        self.lb = Label(self.top, font=("Times New Roman", 36, "bold"), width=wid, height=2,
                        text="WELCOME TO ONLINE VOTING PORTAL", bg="#2B3856", fg="#FEFCFF", anchor="center").pack(fill=X)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.login = Frame(self.middle, width=600, height=540, bd=2, relief='sunken')
        self.login.pack(pady=80)
        self.l = Label(self.login, font=("Constania", 18, "bold"), width=35, height=1, text="LOGIN PAGE",bg="#2B3856",
                           fg="#FEFCFF", anchor="w").pack(fill=X)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.logs = Frame(self.login, width=600, height=540, bd=1, relief='flat')
        self.logs.pack(fill=X)
        self.log = Frame(self.logs, width=600, height=540, bd=1, relief='flat')
        self.log.pack(pady=20)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.t1 = Label(self.log, font=("Constania", 14, "bold"), text="Student Login", width=15, height=1,
                            fg="#2B3856", borderwidth=2, anchor="e").grid(row=0, column=0)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.enrollment = StringVar()
        self.studpass = StringVar()
        self.l1 = Label(self.log, font=("Constania", 10, "bold"), text="          Enrollment Number", width=20,
                            height=2, fg="#2B3856", borderwidth=2, anchor="w").grid(row=1, column=0, pady=5)
        self.tb1 = Entry(self.log, font=("Constania", 10, "bold"), width=25, textvariable=self.enrollment)
        self.tb1.grid(row=1, column=1, padx=20)
        self.l2 = Label(self.log, font=("Constania", 10, "bold"), text="          Password", width=20, height=2,
                            fg="#2B3856", borderwidth=2, anchor="w").grid(row=2, column=0, pady=5)
        bullet = u"\u2022"  # specify bullet character
        self.tb2 = Entry(self.log, font=("Constania", 10, "bold"), width=25, show=bullet,
                             textvariable=self.studpass)
        self.tb2.grid(row=2, column=1, padx=20)
        # -----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.b1 = Button(self.log, text="Log in", font=("Constania", 10, "bold"), width=10, borderwidth=2, bd=2,
                             bg="#2B3856", fg="#FEFCFF",command=self.stud_login, anchor="center").grid(row=3, column=0, pady=10)
        # -----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.t2 = Label(self.log, font=("Constania", 18, "bold"), text="OR", width=15, height=1, fg="#FF2400",
                            borderwidth=2, anchor="w").grid(row=4, column=1, pady=5)
        # -----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.t3 = Label(self.log, font=("Constania", 14, "bold"), text="    Admin Login", width=15, height=1,
                            fg="#2B3856", borderwidth=2, anchor="center").grid(row=5, column=0, pady=5)
        # -----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.admin = StringVar()
        self.adminpass = StringVar()
        self.l3 = Label(self.log, font=("Constania", 10, "bold"), text="Admin", width=10, height=2, fg="#2B3856",
                            borderwidth=2, anchor="w").grid(row=6, column=0, pady=5)
        self.tb3 = Entry(self.log, font=("Constania", 10, "bold"), width=25, textvariable=self.admin)
        self.tb3.grid(row=6,column=1, padx=20)
        self.l4 = Label(self.log, font=("Constania", 10, "bold"), text="Password", width=10, height=2, fg="#2B3856",
                            borderwidth=2, anchor="w").grid(row=7, column=0, pady=5)
        self.tb4 = Entry(self.log, font=("Constania", 10, "bold"), width=25, show=bullet,
                             textvariable=self.adminpass)
        self.tb4.grid(row=7, column=1, padx=20)
        # -----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.ad=lambda: controller.show_frame(Admin_Page)
        self.b2 = Button(self.log, text="Sign in", font=("Constania", 10, "bold"), width=10, borderwidth=2, bd=2,
                             bg="#2B3856", fg="#FEFCFF",command=self.admin_login, anchor="center").grid(row=8, column=0, pady=20)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------

    def call_house(self,house):
        c=0
        self.retrieve_lstud_data()
        cur4.execute('SELECT * FROM Admin_Details')
        data=cur4.fetchone()
        cur3.execute('SELECT * FROM Voter_Details')
        voter=cur3.fetchall()
        for row in voter:
            if row[0]==self.s_enr:
                if row[2]!="" and row[3]!="":
                    tkMessageBox.showwarning("Warning!","You've Already Voted!!!")
                    self.admin_clear()
                    self.stud_clear()
                    c=0
                    break
                else:
                    c=1
        if c==1:
            if house == 'Orange House':
                if data[2]==1:
                    Orange_House(parent=None,controller=self.controller)
                    self.oh = lambda: self.controller.show_frame(Orange_House)
                    self.admin_clear()
                    self.stud_clear()
                    return self.oh()
                else:
                    tkMessageBox.showinfo("Information","Can't Vote Right Now!!!\nVoting Hours Is Not Scheduled....")
                    self.admin_clear()
                    self.stud_clear()
            elif house == 'White House':
                if data[2]==1:
                    White_House(parent=None,controller=self.controller)
                    self.wh = lambda: self.controller.show_frame(White_House)
                    self.admin_clear()
                    self.stud_clear()
                    return self.wh()
                else:
                    tkMessageBox.showinfo("Information", "Can't Vote Right Now!!!\nVoting Hours Is Not Scheduled....")
                    self.admin_clear()
                    self.stud_clear()
            else:
                if data[2]==1:
                    Green_House(parent=None,controller=self.controller)
                    self.gh = lambda: self.controller.show_frame(Green_House)
                    self.admin_clear()
                    self.stud_clear()
                    return self.gh()
                else:
                    tkMessageBox.showinfo("Information", "Can't Vote Right Now!!!\nVoting Hours Is Not Scheduled....")
                    self.admin_clear()
                    self.stud_clear()
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
    def retrieve_admin_data(self):
        self.adm_list=[]
        self.a_name=self.admin.get()
        self.adm_list.append(self.a_name)
        self.a_pass=self.adminpass.get()
        self.adm_list.append(self.a_pass)
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
    global p
    p=""
    def enrol(self):
        self.retrieve_lstud_data()
        return p
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def retrieve_lstud_data(self):
        self.s_list=[]
        self.s_enr=self.enrollment.get()
        self.s_list.append(self.s_enr)
        self.s_pass=self.studpass.get()
        self.s_list.append(self.s_pass)
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
    def admin_clear(self):
        self.tb3.delete(0,END)
        self.tb4.delete(0,END)
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
    def stud_clear(self):
        self.tb1.delete(0,END)
        self.tb2.delete(0,END)
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
    def admin_login(self):
        c=0
        try:
            cur4.execute('CREATE TABLE IF NOT EXISTS Admin_Details(username text primary key,password text,status integer)')
            cur4.execute('INSERT INTO Admin_Details(username,password,status)VALUES(?,?,?)',('admin','adminpass',0))
            db4.commit()
        except sqlite3.IntegrityError,sqlite3.OperationalError:
            pass
        self.retrieve_admin_data()
        for i in self.adm_list:
            if i=='':
                c+=1
        if c==0:
            if self.a_name=='admin':
                if self.a_pass=='adminpass':
                    self.ad()
                    self.admin_clear()
                    self.stud_clear()
                else:
                    tkMessageBox.showinfo("Invalid Input!","Incorrect Password")
                    self.admin_clear()
                    self.stud_clear()
            else:
                tkMessageBox.showinfo("Invalid Input","Incorrect Username or Password")
                self.admin_clear()
                self.stud_clear()
        else:
            tkMessageBox.showerror("Error!!!","All Fields Must Be Filled")
            self.admin_clear()
            self.stud_clear()
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
    def stud_login(self):
        global p
        try:
            ob=Admin_Page(parent=None,controller=self.controller)
            data=ob.fetch_stud_data()
            cur2.execute('SELECT * FROM House_Record_Details')
            data1=cur2.fetchall()
            c=0
            k=0
            self.retrieve_lstud_data()
            p=self.s_enr
            for i in self.s_list:
                if i=='':
                    c+=1
            if c==0:
                # -----------------------------------------------------------------------------------------------------------------------------------------------------------
                for row in data:
                    if row[0]==self.s_enr:
                        # -----------------------------------------------------------------------------------------------------------------------------------------------------------
                        if row[2] ==self.s_pass:
                            # -----------------------------------------------------------------------------------------------------------------------------------------------------------
                            try:
                                cur3.execute('CREATE TABLE IF NOT EXISTS Voter_Details(enr_no text primary key,house text,captain text,vcaptain text)')
                                cur3.execute('INSERT INTO Voter_Details(enr_no,house,captain,vcaptain)VALUES(?,?,?,?)',(row[0],row[4],"",""))
                                db3.commit()
                            except sqlite3.IntegrityError,sqlite3.OperationalError:
                                pass
                            for r in data1:
                                if row[4]=='Orange House':
                                    if r[0]=='Orange House':
                                        if r[1]==2 and r[2]==2:
                                            self.call_house(row[4])
                                        else:
                                            tkMessageBox.showinfo("Login Status","Can't Vote Right Now!!!\nNominees Are Not Being Updated...")
                                            self.admin_clear()
                                            self.stud_clear()
                                        break
                                elif row[4]=='White House':
                                    if r[0]=='White House':
                                        if r[1]==2 and r[2]==2:
                                            self.call_house(row[4])
                                        else:
                                            tkMessageBox.showinfo("Login Status","Can't Vote Right Now!!!\nNominees Are Not Being Updated...")
                                            self.admin_clear()
                                            self.stud_clear()
                                        break
                                else:
                                    if r[0]=='Green House':
                                        if r[1]==2 and r[2]==2:
                                            self.call_house(row[4])
                                        else:
                                            tkMessageBox.showinfo("Login Status","Can't Vote Right Now!!!\nNominees Are Not Being Updated...")
                                            self.admin_clear()
                                            self.stud_clear()
                                        break
                            k=1
                            break
                            # -----------------------------------------------------------------------------------------------------------------------------------------------------------
                        # -----------------------------------------------------------------------------------------------------------------------------------------------------------
                        else:
                            tkMessageBox.showinfo("Invalid Input!", "Incorrect Password")
                            self.admin_clear()
                            self.stud_clear()
                            k=1
                            break
                    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
                    else:
                        k=0
                if k==0:
                    tkMessageBox.showinfo("Invalid Input", "Incorrect Username or Password")
                    self.admin_clear()
                    self.stud_clear()
                # -----------------------------------------------------------------------------------------------------------------------------------------------------------
            else:
                tkMessageBox.showerror("Error!!!", "All Fields Must Be Filled")
                self.admin_clear()
                self.stud_clear()
        except sqlite3.OperationalError:
            tkMessageBox.showerror("Error!","Student Database Doesn't Exist, Contact Admin!!!")
            self.admin_clear()
            self.stud_clear()
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
class Admin_Page(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller=controller
        # -----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.tops=Frame(self,width=1000,height=60,bd=5,relief='raise')
        self.tops.pack(side=TOP)
        wid = self.winfo_screenwidth()
        self.lb1=Label(self.tops,font=("Times New Roman",30,"bold"),width=wid,height=2,text="ADMINISTRATOR MANAGEMENT UTILITY",bd=8,bg="#2B3856",fg="#FEFCFF",relief="raise",anchor="center")
        self.lb1.pack(fill=BOTH)
        self.bottom1=Frame(self,width=1000, height=500,bd=2,bg="#2B3856",relief='raise')
        self.bottom1.pack(side=BOTTOM,fill=BOTH)
        # -----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.left=Frame(self.tops,width=1000,height=800,bd=5,bg="#FEFCFF",relief="raise")
        self.left.pack(side=LEFT,fill=BOTH)
        self.right=Frame(self.tops,width=1000,height=800,bd=5,bg="#FEFCFF",relief="raise")
        self.right.pack(side=RIGHT,fill=BOTH)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.left1=Frame(self.left,width=1000,height=700,bd=2,bg="#FEFCFF",relief="raise")
        self.left1.pack(expand=TRUE,fill=BOTH)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.left2=Frame(self.left,width=1000,height=100,bd=2,bg="#FEFCFF",relief="raise")
        self.left2.pack(expand=TRUE,fill=BOTH)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.right1=Frame(self.right,width=1000,height=800,bd=5,bg="#FEFCFF",relief="raise")
        self.right1.pack(expand=TRUE,fill=BOTH)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.n=Frame(self.left1,width=1000,height=50,bd=0,bg="#FEFCFF",relief="raise")
        self.n.pack(expand=TRUE,fill=BOTH)
        self.nom=Label(self.n,font=("Constania",24,"bold"),bg="#2B3856",fg="#FEFCFF",padx=10,borderwidth=5,bd=5,width=25,text="NOMINATION FORM",relief="raise",anchor="w")
        self.nom.pack(fill=X,pady=5)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.fn=StringVar()
        self.ln=StringVar()
        self.nomen=StringVar()
        self.nombat=StringVar()
        self.form=Frame(self.n,width=1000,height=650,bd=0,bg="#FEFCFF",relief="raise")
        self.form.pack(expand=TRUE,fill=BOTH)
        self.nd=Label(self.form,font=("Constania",18,"bold"),text="Nominee Details",width=15,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=0,column=0,padx=10,pady=10,sticky=W)
        self.fnl=Label(self.form,font=("Constania",14,"bold"),text="First Name",width=8,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=1,column=0,padx=10,pady=20,sticky=W)
        self.tfnl=Entry(self.form,font=("Constania",12,"bold"),width=20,bd=2,textvariable=self.fn)
        self.tfnl.grid(row=1,column=1,pady=20,sticky=W)

        self.lnl=Label(self.form,font=("Constania",14,"bold"),text="Last Name",width=10,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=1,column=2,padx=10,pady=20,sticky=W)
        self.tlnl=Entry(self.form,font=("Constania",12,"bold"),width=20,bd=2,textvariable=self.ln)
        self.tlnl.grid(row=1,column=3,pady=20,sticky=W)
        self.en=Label(self.form,font=("Constania",14,"bold"),text="Enrollment Number",width=15,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=2,column=0,padx=10,pady=20,sticky=W)
        self.ten=Entry(self.form,font=("Constania",12,"bold"),width=20,bd=2,textvariable=self.nomen)
        self.ten.grid(row=2,column=1,pady=20,sticky=W)
        self.bat=Label(self.form,font=("Constania",14,"bold"),text="Batch",width=10,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=2,column=2,padx=10,pady=20,sticky=W)
        self.batbox=ttk.Combobox(self.form,font=("Constania",12,"bold"),width=10,textvariable=self.nombat,state='readonly')
        self.batbox['values']=[' ',2021,2020,2019,2018,2017,2016,2015,2014,2013]
        self.batbox.current(0)
        self.batbox.grid(row=2,column=3,padx=2,pady=20,sticky=W)
        self.house=Label(self.form,font=("Constania",14,"bold"),text="House",width=10,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=3,column=0,padx=10,pady=20,sticky=W)

        self.v=StringVar()
        self.v.set("0")
        house1=['Orange House','White House','Green House']
        i=0
        for hc in house1:
            i+=1
            self.h=Radiobutton(self.form,font=("Constania",14,"bold"),text=hc,padx=40,bg="#FEFCFF",fg="#2B3856",variable=self.v,value=hc,relief="flat",anchor="w").grid(row=3,column=i,pady=20,sticky=W)
        self.post=Label(self.form,font=("Constania",14,"bold"),text="Position",width=10,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=4,column=0,padx=10,pady=20,sticky=W)
        position=['Captain','Vice - Captain']
        i=0
        self.v1=StringVar()
        self.v1.set("0")
        for pos in position:
            i+=1
            self.p=Radiobutton(self.form,font=("Constania",14,"bold"),text=pos,padx=40,bg="#FEFCFF",fg="#2B3856",variable=self.v1,value=pos,relief="flat",anchor="w").grid(row=4,column=i,pady=20,sticky=W)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------

        self.up=Button(self.form,text="Update",font=("Constania",16,"bold"),width=15,borderwidth=4,bd=5,bg="#2B3856",fg="#FEFCFF",relief="raise",command=self.nom_update,anchor="center").grid(row=5,column=3,pady=20,sticky=W)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.r=Frame(self.right1,width=1000,height=50,bd=2,bg="#FEFCFF",relief="raise")
        self.r.pack(expand=TRUE,fill=BOTH)
        self.stud= Label(self.r,font=("Constania",24,"bold"),bg="#2B3856",fg="#FEFCFF",padx=10,borderwidth=5,bd=5,width=25,text="UPDATE STUDENT DETAILS",relief="raise",anchor="w").pack(fill=X,pady=5)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.studnm=StringVar()
        self.studln=StringVar()
        self.studenl=StringVar()
        self.studpassd=StringVar()
        self.studbat=StringVar()
        self.studhouse=StringVar()
        self.form1=Frame(self.r,width=1000,height=750,bd=0,bg="#FEFCFF",relief="raise")
        self.form1.pack(expand=TRUE,fill=BOTH)
        self.sd =Label(self.form1,font=("Constania",18,"bold"),text="Student Details",width=15,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=0,column=0,padx=10,pady=10,sticky=W)
        self.sfn=Label(self.form1,font=("Constania",14,"bold"),text="First Name",width=8,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=1,column=0,padx=10,pady=20,sticky=W)
        self.tsfn=Entry(self.form1,font=("Constania",12,"bold"),width=20,bd=2,textvariable=self.studnm)
        self.tsfn.grid(row=1,column=1,pady=20,sticky=W)
        self.sln=Label(self.form1,font=("Constania",14,"bold"),text="Last Name",width=10,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=2,column=0,padx=10,pady=20,sticky=W)
        self.tsln=Entry(self.form1,font=("Constania",12,"bold"),width=20,bd=2,textvariable=self.studln)
        self.tsln.grid(row=2,column=1,pady=20,sticky=W)
        self.sen=Label(self.form1,font=("Constania",14,"bold"),text="Enrollment Number",width=15,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=3,column=0,padx=10,pady=20,sticky=W)
        self.tsen=Entry(self.form1,font=("Constania",12,"bold"),width=20,bd=2,textvariable=self.studenl)
        self.tsen.grid(row=3,column=1,pady=20,sticky=W)
        self.lpas=Label(self.form1,font=("Constania",14,"bold"),text="Password",width=15,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=4,column=0,padx=10,pady=20,sticky=W)
        self.tpas=Entry(self.form1,font=("Constania",12,"bold"),width=20,bd=2,textvariable=self.studpassd)
        self.tpas.grid(row=4,column=1,pady=20,sticky=W)
        self.sbat=Label(self.form1,font=("Constania",14,"bold"),text="Batch",width=10,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=5,column=0,padx=10,pady=20,sticky=W)
        self.sbatbox=ttk.Combobox(self.form1,font=("Constania",10,"bold"),width=10,textvariable=self.studbat,state='readonly')
        self.sbatbox['values']=[' ',2021,2020,2019,2018,2017,2016,2015,2014,2013]
        self.sbatbox.current(0)
        self.sbatbox.grid(row=5,column=1,padx=2,pady=20,sticky=W)
        self.slhouse=Label(self.form1,font=("Constania",12,"bold"),text="House",width=10,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=6,column=0,padx=10,pady=20,sticky=W)
        self.shouse=ttk.Combobox(self.form1,font=("Constania",10,"bold"),width=15,textvariable=self.studhouse,state='readonly')
        self.shouse['values']=[' ','Orange House','White House','Green House']
        self.shouse.current(0)
        self.shouse.grid(row=6,column=1,padx=2,pady=20,sticky=W)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.sup=Button(self.form1,text="Update",font=("Constania",16,"bold"),width=15,borderwidth=4,bd=5,bg="#2B3856",fg="#FEFCFF",relief="raise",command=self.stud_update,anchor="center").grid(row=7,column=1,padx=35,pady=20,sticky=E)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.vsd=Button(self.left2,text="View Student Details",font=("Constania",16,"bold"),width=20,borderwidth=4,bd=5,bg="#2B3856",fg="#FEFCFF",command=self.stud_details,relief="raise",anchor="center").grid(row=1,column=1,padx=20,pady=40,sticky=E)
        self.vnd=Button(self.left2,text="View Nominee Details",font=("Constania",16,"bold"),width=20,borderwidth=4,bd=5,bg="#2B3856",fg="#FEFCFF",command=self.nom_details,relief="raise",anchor="center").grid(row=1,column=2,padx=20,pady=40,sticky=E)
        self.vr=Button(self.left2,text="View Results",font=("Constania",16,"bold"),width=20,borderwidth=4,bd=5,bg="#2B3856",fg="#FEFCFF",command=self.result,relief="raise",anchor="center").grid(row=1,column=3,padx=20,pady=40,sticky=E)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.bot=Frame(self.bottom1,width=900,height=500,bd=2,bg="#2B3856",relief='raise')
        self.bot.pack(side=LEFT,expand=TRUE,fill=BOTH)
        self.bot1=Frame(self.bottom1,width=50,height=500,bd=2,bg="#2B3856",relief='raise')
        self.bot1.pack(side=RIGHT,expand=TRUE,fill=BOTH)

        self.sv=Button(self.bot,text="Start Vote",font=("Constania",16,"bold"),width=10,borderwidth=5,bd=5,bg="#4863A0",fg="#FEFCFF",command=self.start_vote,relief="raise",anchor="center").grid(row=0,column=0,padx=50,pady=30,sticky=E)
        self.stv=Button(self.bot,text="Stop Vote",font=("Constania",16,"bold"),width=10,borderwidth=5,bd=5,bg="#4863A0",fg="#FEFCFF",command=self.stop_vote,relief="raise",anchor="center").grid(row=0,column=1,padx=50,pady=30,sticky=E)
        self.lg=Button(self.bot1,text="Logout",font=("Constania",18,"bold"),width=8,borderwidth=5,bd=5,bg="#4863A0",fg="#FEFCFF",relief="raise",command=self.logout,anchor="center").pack(side=RIGHT,padx=50)
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def nom_details(self):
        try:
            cur.execute('Select * FROM Nominee_Details')
            nom_d = cur.fetchall()
            val=list(nom_d)
            show=pd.DataFrame(val,columns=['ENROLLMENT NUMBER','NAME','BATCH','HOUSE','POSITION'])
            nom=Tk()
            self.title=nom.title("Nominees Database")
            nom.geometry("1000x800")
            nom.configure(background="#FEFCFF")
            frame = Frame(nom,width=nom.winfo_screenwidth(),height=nom.winfo_screenheight(),bg="#FEFCFF",bd=5,relief='raise')
            frame.pack(side=TOP,fill=BOTH,expand=TRUE)
            table=Table(frame,dataframe=show)
            table.show()
            nom.mainloop()
        except sqlite3.DatabaseError:
            tkMessageBox.showwarning("Status","Please Update The Nominees Details!!!")
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def stud_details(self):
        try:
            cur1.execute('Select * FROM Student_Details')
            st_det=cur1.fetchall()
            val=list(st_det)
            show=pd.DataFrame(val, columns=['ENROLLMENT NUMBER','NAME','PASSWORD','BATCH','HOUSE'])
            stud=Tk()
            self.title=stud.title("Student Database")
            stud.geometry("1000x800")
            stud.configure(background="#FEFCFF")
            frame=Frame(stud,width=stud.winfo_screenwidth(),height=stud.winfo_screenheight(),bg="#FEFCFF",bd=5,relief='raise')
            frame.pack(side=TOP, fill=BOTH, expand=TRUE)
            table = Table(frame,dataframe=show)
            table.show()
            stud.mainloop()
        except sqlite3.DatabaseError:
            tkMessageBox.showwarning("Status","Please Update The Student Details!!!")
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def logout(self):
        z1 = lambda: self.controller.show_frame(Login_Page)
        self.nom_clear()
        self.stud_clear()
        return z1()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def start_vote(self):
        try:
            cur2.execute('SELECT * FROM House_Record_Details')
            data=cur2.fetchall()
        except sqlite3.DatabaseError:
            tkMessageBox.showwarning("Status","Please Update The Nominees!!!")
        c=0
        for row in data:
            if row[0]=='Orange House' and row[1]==2 and row[2]==2:
                c+=1
            elif row[0]=='White House' and row[1]==2 and row[2]==2:
                c+=1
            elif row[0]=='Green House' and row[1]==2 and row[2]==2:
                c+=1
        if c==3:
            cur4.execute('UPDATE Admin_Details SET status=? WHERE username=?',(1,'admin'))
            db4.commit()
            tkMessageBox.showinfo("Status","Voting Scheduled Successfully...")
            self.nom_clear()
            self.stud_clear()
        else:
            tkMessageBox.showwarning("Status","Please Update The Nominees Details...")
            self.nom_clear()
            self.stud_clear()

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    global q
    q=0
    def stop_vote(self):
        global q
        cur4.execute('SELECT * FROM Admin_Details')
        data=cur4.fetchone()
        if data[2]==0:
            tkMessageBox.showwarning("Status","Please, Press The Start Button To Schedule It...")
            self.nom_clear()
            self.stud_clear()
        else:
            result=tkMessageBox.askyesno("Stop!!!","Would You Like To Stop It ?")
            self.nom_clear()
            self.stud_clear()
            if result==False:
                pass
            else:
                tkMessageBox.showinfo("Status","Voting System Is Closed!!!")
                q=1
                cur4.execute('UPDATE Admin_Details SET status=? WHERE username=?', (0, 'admin'))
                db4.commit()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def clear_record(self):
        cur.execute('DROP TABLE Nominee_Details')
        db.commit()
        cur1.execute('DROP TABLE Student_Details')
        db1.commit()
        cur2.execute('DROP TABLE House_Record_Details')
        db2.commit()
        cur3.execute('DROP TABLE Voter_Details')
        db3.commit()
        self.resultt.destroy()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def calculation(self):
        self.tot_wh=0
        self.tot_gh=0
        self.tot_oh=0
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.numc1_wh=0
        self.numc2_wh=0
        self.numvc1_wh=0
        self.numvc2_wh=0
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.numc1_gh=0
        self.numc2_gh=0
        self.numvc1_gh=0
        self.numvc2_gh=0
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.numc1_oh=0
        self.numc2_oh=0
        self.numvc1_oh=0
        self.numvc2_oh=0
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------

        cur3.execute('Select * FROM Voter_Details')
        self.v_det=cur3.fetchall()
        cur.execute('Select * FROM Nominee_Details')
        self.nom_det=cur.fetchall()
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        for row in self.v_det:
            if row[1]=='White House':
                self.tot_wh+=1
            elif row[1]=='Orange House':
                self.tot_oh+=1
            elif row[1]=='Green House':
                self.tot_gh+=1
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.whcp=[]
        self.whvcp=[]
        self.ghcp=[]
        self.ghvcp=[]
        self.ohcp=[]
        self.ohvcp=[]
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        for row in self.nom_det:
            if row[3]=='White House' and row[4]=='Captain':
                self.whcp.append(row[1])
            elif row[3]=='White House' and row[4]=='Vice - Captain':
                self.whvcp.append(row[1])
            elif row[3]=='Orange House' and row[4]=='Captain':
                self.ohcp.append(row[1])
            elif row[3]=='Orange House' and row[4]=='Vice - Captain':
                self.ohvcp.append(row[1])
            elif row[3]=='Green House' and row[4]=='Captain':
                self.ghcp.append(row[1])
            elif row[3]=='Green House' and row[4]=='Vice - Captain':
                self.ghvcp.append(row[1])
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        for row in self.v_det:
            if row[1]=='White House' and row[2]==self.whcp[0]:
                self.numc1_wh+=1
            if row[1]=='White House' and row[2]==self.whcp[1]:
                self.numc2_wh+=1
            if row[1]=='White House' and row[3]==self.whvcp[0]:
                self.numvc1_wh+=1
            if row[1]=='White House' and row[3]==self.whvcp[1]:
                self.numvc2_wh+=1
            #-----------------------------------------------------------------------------------------------------------------------------------------------------------
            if row[1]=='Orange House' and row[2]==self.ohcp[0]:
                self.numc1_oh+=1
            if row[1]=='Orange House' and row[2]==self.ohcp[1]:
                self.numc2_oh+=1
            if row[1]=='Orange House' and row[3]==self.ohvcp[0]:
                self.numvc1_oh+=1
            if row[1]=='Orange House' and row[3]==self.ohvcp[1]:
                self.numvc2_oh+=1
            #-----------------------------------------------------------------------------------------------------------------------------------------------------------
            if row[1]=='Green House' and row[2]==self.ghcp[0]:
                self.numc1_gh+=1
            if row[1]=='Green House' and row[2]==self.ghcp[1]:
                self.numc2_gh+=1
            if row[1]=='Green House' and row[3]==self.ghvcp[0]:
                self.numvc1_gh+=1
            if row[1]=='Green House' and row[3]==self.ghvcp[1]:
                self.numvc2_gh+=1
            #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        try:
            self.pc1_wh=round(((self.numc1_wh*100)/self.tot_wh),2)
            self.pc2_wh=round(((self.numc2_wh*100)/self.tot_wh),2)
            self.pvc1_wh=round(((self.numvc1_wh*100)/self.tot_wh),2)
            self.pvc2_wh=round(((self.numvc2_wh*100)/self.tot_wh),2)
        except ZeroDivisionError:
            self.pc1_wh=0
            self.pc2_wh=0
            self.pvc1_wh=0
            self.pvc2_wh=0
            #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        try:
            self.pc1_gh=round(((self.numc1_gh*100)/self.tot_gh),2)
            self.pc2_gh=round(((self.numc2_gh*100)/self.tot_gh),2)
            self.pvc1_gh=round(((self.numvc1_gh*100)/self.tot_gh),2)
            self.pvc2_gh=round(((self.numvc2_gh*100)/self.tot_gh),2)
        except ZeroDivisionError:
            self.pc1_gh = 0
            self.pc2_gh = 0
            self.pvc1_gh = 0
            self.pvc2_gh = 0
            #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        try:
            self.pc1_oh=round(((self.numc1_oh*100)/self.tot_oh),2)
            self.pc2_oh=round(((self.numc2_oh*100)/self.tot_oh),2)
            self.pvc1_oh=round(((self.numvc1_oh*100)/self.tot_oh),2)
            self.pvc2_oh=round(((self.numvc2_oh*100)/self.tot_oh),2)
        except ZeroDivisionError:
            self.pc1_oh = 0
            self.pc2_oh = 0
            self.pvc1_oh = 0
            self.pvc2_oh = 0
            #-----------------------------------------------------------------------------------------------------------------------------------------------------------

    def result(self):
        global q
        if q==0:
            tkMessageBox.showinfo("Result Status","Result Not Yet Declared!!!")
        else:
            self.calculation()
            # -----------------------------------------------------------------------------------------------------------------------------------------------------------
            self.resultt = Tk()
            self.title = self.resultt.title("Result")
            self.resultt.geometry("1500x800")
            self.resultt.configure(background="#1569C7")
            top=Frame(self.resultt,width=1000, height=40, bd=5, relief='raise')
            top.pack(side=TOP, fill=BOTH)
            # -----------------------------------------------------------------------------------------------------------------------------------------------------------
            ltop=Frame(top, width=800, height=100, bd=0, bg="#2B3856", relief='raise')
            ltop.pack(side=LEFT, fill=BOTH, expand=TRUE)
            rtop=Frame(top, width=200, height=100, bd=0, bg="#2B3856", relief='raise')
            rtop.pack(side=RIGHT, fill=BOTH, expand=TRUE)
            lttop= Label(ltop, font=("Times New Roman", 30, "bold"), height=2, padx=10, text="VOTING RESULTS", bd=0,bg="#2B3856", fg="#FEFCFF", relief="raise", anchor="w")
            lttop.pack(fill=BOTH)
            rttop=Button(rtop, text="Quit", font=("Constania", 16, "bold"), width=6, padx=20, borderwidth=5, bd=5,bg="#4863A0", fg="#FEFCFF",command=self.resultt.destroy, relief="raise", anchor="center")
            rttop.pack(side=RIGHT, padx=20)
            rt1top=Button(rtop, text="Clear Records", font=("Constania", 16, "bold"), width=10, padx=20, borderwidth=5,bd=5, bg="#4863A0", fg="#FEFCFF",command=self.clear_record, relief="raise", anchor="center")
            rt1top.pack(side=RIGHT, padx=20)
            # -----------------------------------------------------------------------------------------------------------------------------------------------------------
            bottom = Frame(self.resultt,width=1000, height=15, bd=5, bg="#2B3856", relief='raise')
            bottom.pack(side=BOTTOM, fill=BOTH)
            # -----------------------------------------------------------------------------------------------------------------------------------------------------------
            mid = Frame(self.resultt,width=1000, height=660, bd=5, bg="#FEFCFF", relief="raise")
            mid.pack(side=TOP, fill=BOTH, expand=TRUE)
            # -----------------------------------------------------------------------------------------------------------------------------------------------------------
            ohh = Frame(mid, width=1000, height=220, bd=5, bg="#FEFCFF", relief="raise")
            ohh.pack(fill=BOTH, expand=TRUE)
            # -----------------------------------------------------------------------------------------------------------------------------------------------------------
            whh = Frame(mid, width=1000, height=220, bd=5, bg="#FEFCFF", relief="raise")
            whh.pack(fill=BOTH, expand=TRUE)
            # -----------------------------------------------------------------------------------------------------------------------------------------------------------
            ghh = Frame(mid, width=1000, height=220, bd=5, bg="#FEFCFF", relief="raise")
            ghh.pack(fill=BOTH, expand=TRUE)
            # -----------------------------------------------------------------------------------------------------------------------------------------------------------
            o=Frame(ohh, width=1000, height=20, bd=0, bg="#FEFCFF", relief="raise")
            o.pack(fill=BOTH, expand=TRUE)
            ohhh=Label(o, font=("Constania", 18, "bold"), text="ORANGE HOUSE", width=25, height=1, fg="#FEFCFF",bg="#2B3856", anchor="w")
            ohhh.pack(fill=X)
            oc=Frame(o, width=1000, height=200, bd=0, bg="#FEFCFF", relief="raise")
            oc.pack(fill=BOTH, expand=TRUE)
            oh2 = Label(oc, font=("Constania", 16, "bold"), text="Total Number of Voters    --- ", width=30, height=1,fg="#2B3856", bg="#FEFCFF", anchor="w")
            oh2.grid(row=0, column=0, padx=10, pady=5, sticky=W)
            oh3 = Label(oc, font=("Constania", 16, "bold"), text=self.tot_oh, width=20, height=1, fg="#2B3856", bg="#FEFCFF",anchor="w")
            oh3.grid(row=0, column=1, pady=5, sticky=W)
            ocap=Label(oc, font=("Constania", 14, "bold"), text="CAPTAIN", width=20, height=1, fg="#2B3856",bg="#FEFCFF", anchor="w")
            ocap.grid(row=1,column=0,padx=10,pady=5,sticky=W)
            oh4 = Label(oc, font=("Constania", 12, "bold"), text=self.ohcp[0], width=20, height=1, fg="#2B3856",bg="#FEFCFF", anchor="w")
            oh4.grid(row=2, column=0, padx=10, pady=5, sticky=W)
            oh5 = Label(oc, font=("Constania", 12, "bold"), text=str(self.pc1_oh)+" %", width=10, height=1, fg="#2B3856", bg="#FEFCFF",anchor="w")
            oh5.grid(row=2, column=1, pady=5, sticky=W)
            oh6 = Label(oc, font=("Constania", 12, "bold"), text=self.ohcp[1], width=20, height=1, fg="#2B3856",bg="#FEFCFF", anchor="w")
            oh6.grid(row=3, column=0, padx=10, pady=5, sticky=W)
            oh7 = Label(oc, font=("Constania", 12, "bold"), text=str(self.pc2_oh)+" %", width=20, height=1, fg="#2B3856", bg="#FEFCFF",anchor="w")
            oh7.grid(row=3, column=1, pady=5, sticky=W)
            ovcap = Label(oc, font=("Constania", 14, "bold"), text="VICE - CAPTAIN", width=20, height=1, fg="#2B3856",bg="#FEFCFF", anchor="w")
            ovcap.grid(row=1, column=2, padx=10, pady=5, sticky=W)
            oh8 = Label(oc, font=("Constania", 12, "bold"), text=self.ohvcp[0], width=20, height=1, fg="#2B3856",bg="#FEFCFF", anchor="w")
            oh8.grid(row=2, column=2, padx=10, pady=5, sticky=W)
            oh9 = Label(oc, font=("Constania", 12, "bold"), text=str(self.pvc1_oh)+" %", width=20, height=1, fg="#2B3856", bg="#FEFCFF",anchor="w")
            oh9.grid(row=2, column=3, pady=5, sticky=W)
            oh10 = Label(oc, font=("Constania", 12, "bold"), text=self.ohvcp[1], width=20, height=1, fg="#2B3856",bg="#FEFCFF", anchor="w")
            oh10.grid(row=3, column=2, padx=10, pady=5, sticky=W)
            oh11 = Label(oc, font=("Constania", 12, "bold"), text=str(self.pvc2_oh)+" %", width=20, height=1, fg="#2B3856", bg="#FEFCFF",anchor="w")
            oh11.grid(row=3, column=3, pady=5, sticky=W)
            # -----------------------------------------------------------------------------------------------------------------------------------------------------------
            w = Frame(whh, width=1000, height=20, bd=0, bg="#FEFCFF", relief="raise")
            w.pack(fill=BOTH, expand=TRUE)
            whhh = Label(w, font=("Constania", 18, "bold"), text="WHITE HOUSE", width=25, height=1, fg="#FEFCFF",bg="#2B3856", anchor="w")
            whhh.pack(fill=X)
            wc = Frame(w, width=1000, height=200, bd=0, bg="#FEFCFF", relief="raise")
            wc.pack(fill=BOTH, expand=TRUE)
            wh2 = Label(wc, font=("Constania", 16, "bold"), text="Total Number of Voters    --- ", width=30, height=1,fg="#2B3856", bg="#FEFCFF", anchor="w")
            wh2.grid(row=0, column=0, padx=10, pady=5, sticky=W)
            wh3 = Label(wc, font=("Constania", 16, "bold"), text=self.tot_wh, width=20, height=1, fg="#2B3856", bg="#FEFCFF",anchor="w")
            wh3.grid(row=0, column=1, pady=5, sticky=W)
            wcap = Label(wc, font=("Constania", 14, "bold"), text="CAPTAIN", width=20, height=1, fg="#2B3856",bg="#FEFCFF", anchor="w")
            wcap.grid(row=1, column=0, padx=10, pady=5, sticky=W)
            wh4 = Label(wc, font=("Constania", 12, "bold"), text=self.whcp[0], width=20, height=1, fg="#2B3856",bg="#FEFCFF", anchor="w")
            wh4.grid(row=2, column=0, padx=10, pady=5, sticky=W)
            wh5 = Label(wc, font=("Constania", 12, "bold"), text=str(self.pc1_wh)+" %", width=20, height=1, fg="#2B3856", bg="#FEFCFF",anchor="w")
            wh5.grid(row=2, column=1, pady=5, sticky=W)
            wh6 = Label(wc, font=("Constania", 12, "bold"), text=self.whcp[1], width=20, height=1, fg="#2B3856",bg="#FEFCFF", anchor="w")
            wh6.grid(row=3, column=0, padx=10, pady=5, sticky=W)
            wh7 = Label(wc, font=("Constania", 12, "bold"), text=str(self.pc2_wh)+" %", width=20, height=1, fg="#2B3856", bg="#FEFCFF",anchor="w")
            wh7.grid(row=3, column=1, pady=5, sticky=W)
            wvcap = Label(wc, font=("Constania", 14, "bold"), text="VICE - CAPTAIN", width=20, height=1, fg="#2B3856",bg="#FEFCFF", anchor="w")
            wvcap.grid(row=1, column=2, padx=10, pady=5, sticky=W)
            wh8 = Label(wc, font=("Constania", 12, "bold"), text=self.whvcp[0], width=20, height=1, fg="#2B3856",bg="#FEFCFF", anchor="w")
            wh8.grid(row=2, column=2, padx=10, pady=5, sticky=W)
            wh9 = Label(wc, font=("Constania", 12, "bold"), text=str(self.pvc1_wh)+" %", width=20, height=1, fg="#2B3856", bg="#FEFCFF",anchor="w")
            wh9.grid(row=2, column=3, pady=5, sticky=W)
            wh10 = Label(wc, font=("Constania", 12, "bold"), text=self.whvcp[1], width=20, height=1, fg="#2B3856",bg="#FEFCFF", anchor="w")
            wh10.grid(row=3, column=2, padx=10, pady=5, sticky=W)
            wh11 = Label(wc, font=("Constania", 12, "bold"), text=str(self.pvc2_wh)+" %", width=20, height=1, fg="#2B3856", bg="#FEFCFF",anchor="w")
            wh11.grid(row=3, column=3, pady=5, sticky=W)
            # -----------------------------------------------------------------------------------------------------------------------------------------------------------
            g = Frame(ghh, width=1000, height=20, bd=0, bg="#FEFCFF", relief="raise")
            g.pack(fill=BOTH, expand=TRUE)
            ghhh = Label(g, font=("Constania", 18, "bold"), text="GREEN HOUSE", width=25, height=1, fg="#FEFCFF",bg="#2B3856", anchor="w")
            ghhh.pack(fill=X)
            gc = Frame(g, width=1000, height=200, bd=0, bg="#FEFCFF", relief="raise")
            gc.pack(fill=BOTH, expand=TRUE)
            gh2 = Label(gc, font=("Constania", 16, "bold"), text="Total Number of Voters    --- ", width=30, height=1,fg="#2B3856", bg="#FEFCFF", anchor="w")
            gh2.grid(row=0, column=0, padx=10, pady=5, sticky=W)
            gh3 = Label(gc, font=("Constania", 16, "bold"), text=self.tot_gh, width=20, height=1, fg="#2B3856", bg="#FEFCFF",anchor="w")
            gh3.grid(row=0, column=1, pady=5, sticky=W)
            gcap = Label(gc, font=("Constania", 14, "bold"), text="CAPTAIN", width=20, height=1, fg="#2B3856",bg="#FEFCFF", anchor="w")
            gcap.grid(row=1, column=0, padx=10, pady=5, sticky=W)
            gh4 = Label(gc, font=("Constania", 12, "bold"), text=self.ghcp[0], width=20, height=1, fg="#2B3856",bg="#FEFCFF", anchor="w")
            gh4.grid(row=2, column=0, padx=10, pady=5, sticky=W)
            gh5 = Label(gc, font=("Constania", 12, "bold"), text=str(self.pc1_gh)+" %", width=10, height=1, fg="#2B3856", bg="#FEFCFF",anchor="w")
            gh5.grid(row=2, column=1, pady=5, sticky=W)
            gh6 = Label(gc, font=("Constania", 12, "bold"), text=self.ghcp[1], width=20, height=1, fg="#2B3856",bg="#FEFCFF", anchor="w")
            gh6.grid(row=3, column=0, padx=10, pady=5, sticky=W)
            gh7 = Label(gc, font=("Constania", 12, "bold"), text=str(self.pc2_gh)+" %", width=20, height=1, fg="#2B3856", bg="#FEFCFF",anchor="w")
            gh7.grid(row=3, column=1, pady=5, sticky=W)
            gvcap = Label(gc, font=("Constania", 14, "bold"), text="VICE - CAPTAIN", width=20, height=1, fg="#2B3856",bg="#FEFCFF", anchor="w")
            gvcap.grid(row=1, column=2, padx=10, pady=5, sticky=W)
            gh8 = Label(gc, font=("Constania", 12, "bold"), text=self.ghvcp[0], width=20, height=1, fg="#2B3856",bg="#FEFCFF", anchor="w")
            gh8.grid(row=2, column=2, padx=10, pady=5, sticky=W)
            gh9 = Label(gc, font=("Constania", 12, "bold"), text=str(self.pvc1_gh)+" %", width=20, height=1, fg="#2B3856", bg="#FEFCFF",anchor="w")
            gh9.grid(row=2, column=3, pady=5, sticky=W)
            gh10 = Label(gc, font=("Constania", 12, "bold"), text=self.ghvcp[1], width=20, height=1, fg="#2B3856",bg="#FEFCFF", anchor="w")
            gh10.grid(row=3, column=2, padx=10, pady=5, sticky=W)
            gh11 = Label(gc, font=("Constania", 12, "bold"), text=str(self.pvc2_gh)+" %", width=20, height=1, fg="#2B3856", bg="#FEFCFF",anchor="w")
            gh11.grid(row=3, column=3, pady=5, sticky=W)
            # -----------------------------------------------------------------------------------------------------------------------------------------------------------
            self.resultt.mainloop()
        # -----------------------------------------------------------------------------------------------------------------------------------------------------------

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def retrieve_nom_data(self):
        self.nom_list=[]
        self.nom_fname=self.fn.get()
        self.nom_list.append(self.nom_fname)
        self.nom_lname=self.ln.get()
        self.nom_list.append(self.nom_lname)
        self.nom_name=self.nom_fname+" "+self.nom_lname
        self.nom_enr=self.nomen.get()
        self.nom_enr=self.nom_enr.upper()
        self.nom_list.append(self.nom_enr)
        self.nom_batch=self.nombat.get()
        self.nom_list.append(self.nom_batch)
        self.nom_house=self.v.get()
        self.nom_list.append(self.nom_house)
        self.nom_pos=self.v1.get()
        self.nom_list.append(self.nom_pos)


    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def retrieve_stud_data(self):
        self.stud_list=[]
        self.stud_fname=self.studnm.get()
        self.stud_list.append(self.stud_fname)
        self.stud_lname=self.studln.get()
        self.stud_list.append(self.stud_lname)
        self.stud_name=self.stud_fname+" "+self.stud_lname
        self.stud_enr=self.studenl.get()
        self.stud_enr=self.stud_enr.upper()
        self.stud_list.append(self.stud_enr)
        self.stud_pass=self.studpassd.get()
        self.stud_list.append(self.stud_pass)
        self.stud_batch=self.studbat.get()
        self.stud_list.append(self.stud_batch)
        self.stud_house=self.studhouse.get()
        self.stud_list.append(self.stud_house)
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def nom_entry(self):
        cur.execute('CREATE TABLE IF NOT EXISTS Nominee_Details(enr_no text primary key,name text,batch text,house text,position text)')
        cur.execute('INSERT INTO Nominee_Details(enr_no,name,batch,house,position)VALUES(?,?,?,?,?)',(self.nom_enr,self.nom_name,self.nom_batch,self.nom_house,self.nom_pos))
        db.commit()

        tkMessageBox.showinfo("Done!", "Updated Successfully")
    def  nom_data_entry(self):
        self.retrieve_nom_data()
        cur2.execute('SELECT * FROM House_Record_Details')
        self.house_record=cur2.fetchall()
        c=0
        for i in self.nom_list:
            if i=='' or i=='0' or i==' ':
                c+=1
        if c==0:
            for row in self.house_record:
                if row[0]=='Orange House':
                    if self.nom_house==row[0] and self.nom_pos=='Captain':
                        if row[1]<2:
                            self.nom_entry()
                            cur2.execute('UPDATE House_Record_Details SET captain=? WHERE house=?',(row[1]+1,row[0]))
                            db2.commit()
                        else:
                            tkMessageBox.showwarning("Warning!","Atleast Two Members Can Be Nominated as Captain for Orange House")
                            self.nom_clear()
                            self.stud_clear()
                    elif self.nom_house==row[0] and self.nom_pos=='Vice - Captain':
                        if row[2]<2:
                            self.nom_entry()
                            cur2.execute('UPDATE House_Record_Details SET vicecaptain=? WHERE house=?',(row[2]+1,row[0]))
                            db2.commit()
                        else:
                            tkMessageBox.showwarning("Warning!","Atleast Two Members Can Be Nominated as Vice - Captain for Orange House")
                            self.nom_clear()
                            self.stud_clear()
                elif row[0]=='White House':
                    if self.nom_house==row[0] and self.nom_pos=='Captain':
                        if row[1]<2:
                            self.nom_entry()
                            cur2.execute('UPDATE House_Record_Details SET captain=? WHERE house=?',(row[1]+1,row[0]))
                            db2.commit()
                        else:
                            tkMessageBox.showwarning("Warning!","Atleast Two Members Can Be Nominated as Captain for White House")
                            self.nom_clear()
                            self.stud_clear()
                    elif self.nom_house==row[0] and self.nom_pos=='Vice - Captain':
                        if row[2]<2:
                            self.nom_entry()
                            cur2.execute('UPDATE House_Record_Details SET vicecaptain=? WHERE house=?',(row[2]+1,row[0]))
                            db2.commit()
                        else:
                            tkMessageBox.showwarning("Warning!","Atleast Two Members Can Be Nominated as Vice - Captain for White House")
                            self.nom_clear()
                            self.stud_clear()
                elif row[0]=='Green House':
                    if self.nom_house==row[0] and self.nom_pos=='Captain':
                        if row[1]<2:
                            self.nom_entry()
                            cur2.execute('UPDATE House_Record_Details SET captain=? WHERE house=?',(row[1]+1,row[0]))
                            db2.commit()
                        else:
                            tkMessageBox.showwarning("Warning!","Atleast Two Members Can Be Nominated as Captain for Green House")
                            self.nom_clear()
                            self.stud_clear()
                    elif self.nom_house==row[0] and self.nom_pos=='Vice - Captain':
                        if row[2]<2:
                            self.nom_entry()
                            cur2.execute('UPDATE House_Record_Details SET vicecaptain=? WHERE house=?',(row[2]+1,row[0]))
                            db2.commit()
                        else:
                            tkMessageBox.showwarning("Warning!","Atleast Two Members Can Be Nominated as Vice - Captain for Green House")
                            self.nom_clear()
                            self.stud_clear()
        else:
            tkMessageBox.showerror("Error!!!","All Fields Must Be Filled")
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------

    def fetch_nom_data(self):
        cur.execute('SELECT * FROM Nominee_Details')
        self.nom_data = cur.fetchall()
        return self.nom_data
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def stud_data_entry(self):
        self.retrieve_stud_data()
        c=0
        for i in self.stud_list:
            if i=='' or i==' ':
                c+=1
        if c==0:
            cur1.execute('CREATE TABLE IF NOT EXISTS Student_Details(enr_no text primary key,name text,password text,batch text,house text)')
            cur1.execute('INSERT INTO Student_Details(enr_no,name,password,batch,house)VALUES(?,?,?,?,?)',(self.stud_enr,self.stud_name,self.stud_pass,self.stud_batch,self.stud_house))
            db1.commit()
            tkMessageBox.showinfo("Done!","Updated Successfully")
        else:
            tkMessageBox.showerror("Error!!!", "All Fields Must Be Filled")
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------

    def fetch_stud_data(self):
        cur1.execute('SELECT * FROM Student_Details')
        self.stud_data=cur1.fetchall()
        return self.stud_data
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------

    def nom_clear(self):
        self.tfnl.delete(0,END)
        self.tlnl.delete(0,END)
        self.ten.delete(0,END)
        self.batbox.current(0)
        self.v.set("0")
        self.v1.set("0")
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------

    def stud_clear(self):
        self.tsfn.delete(0,END)
        self.tsln.delete(0, END)
        self.tsen.delete(0, END)
        self.tpas.delete(0,END)
        self.sbatbox.current(0)
        self.shouse.current(0)
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------

    def nom_update(self):
        try:
            self.nom_data_entry()
            self.nom_clear()
            self.stud_clear()
        except sqlite3.IntegrityError:
            tkMessageBox.showwarning("Warning!","Enrollment ID Already Exist")
            self.nom_clear()
            self.stud_clear()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------

    def stud_update(self):
        try:
            self.stud_data_entry()
            self.stud_clear()
            self.nom_clear()
        except sqlite3.IntegrityError:
            tkMessageBox.showwarning("Warning!","Enrollment ID Already Exist")
            self.stud_clear()
            self.nom_clear()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
class White_House(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller=controller
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.top=Frame(self,width=1000,height=120,bd=5,bg="#2B3856",relief='raise')
        self.top.pack(side=TOP,fill=BOTH)
        self.ltop=Frame(self.top,width=800,height=100,bd=0,bg="#2B3856",relief='raise')
        self.ltop.pack(side=LEFT,fill=BOTH,expand=TRUE)
        self.rtop=Frame(self.top,width=200,height=100,bd=0,bg="#2B3856",relief='raise')
        self.rtop.pack(side=RIGHT,fill=BOTH,expand=TRUE)
        self.wlb=Label(self.ltop,font=("Times New Roman",30,"bold"),height=2,padx=10,text="WHITE HOUSE NOMINEES",bd=0,bg="#2B3856",fg="#FEFCFF",relief="raise",anchor="w").pack(fill=BOTH)

        self.wlg=Button(self.rtop,text="Logout",font=("Constania",16,"bold"),width=6,padx=20,borderwidth=5,bd=5,bg="#4863A0",fg="#FEFCFF",command=self.logout,relief="raise",anchor="center").pack(side=RIGHT,padx=20)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.bottom=Frame(self,width=1000,height=100,bd=5,bg="#2B3856",relief="raise")
        self.bottom.pack(side=BOTTOM,fill=BOTH)
        self.mid=Frame(self,width=1000,height=500,bd=5,bg="#FEFCFF",relief="raise")
        self.mid.pack(side=TOP,fill=BOTH,expand=TRUE)
        self.mid1=Frame(self.mid,width=1000,height=250,bd=5,bg="#FEFCFF",relief="raise")
        self.mid1.pack(expand=TRUE,fill=BOTH)
        self.mid2=Frame(self.mid,width=1000,height=250,bd=5,bg="#FEFCFF",relief="raise")
        self.mid2.pack(expand=TRUE,fill=BOTH)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.cap=Frame(self.mid1,width=1000,height=50,bd=0,bg="#FEFCFF",relief="raise")
        self.cap.pack(expand=TRUE,fill=BOTH)
        self.lcap=Label(self.cap,font=("Constania",24,"bold"),bg="#2B3856",fg="#FEFCFF",padx=10,borderwidth=5,bd=5,width=25,text="CAPTAIN NOMINEES",relief="raise",anchor="w").pack(fill=X,pady=2)
        self.fcap=Frame(self.cap,width=1000,height=250,bd=0,bg="#FEFCFF",relief="raise")
        self.fcap.pack(expand=TRUE,fill=BOTH)
        self.hcl=Label(self.fcap,font=("Constania",18,"bold"),text="Choose Your House Captain",width=25,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=0,column=0,padx=10,pady=10,sticky=W)
        self.v1=StringVar()
        self.v1.set("0")
        # -----------------------------------------------------------------------------------------------------------------------------------------------------------
        n=self.call_house_record()
        self.cn=[]
        self.vcn=[]
        self.cb=[]
        self.vcb=[]
        for row in n:
            if row[0] == 'White House':
                if row[1] == 2 and row[2] == 2:
                    self.show_nominee()
                    self.cn = self.cname
                    self.vcn = self.vcname
                    self.cb = self.cbatch
                    self.vcb = self.vcbatch
                    self.cb1="BATCH - "+self.cb[0]
                    self.cb2="BATCH - "+self.cb[1]
                    self.vcb1="BATCH - "+self.vcb[0]
                    self.vcb2="BATCH - "+self.vcb[1]
                    c=0
                break
            else:
                c=1
        if c==1:
            self.cn.append("Nominee 1")
            self.cn.append("Nominee 2")
            self.cb.append("BATCH 1")
            self.cb.append("BATCH 2")
            self.cb1=self.cb[0]
            self.cb2=self.cb[1]
            self.vcn.append("Nominee 1")
            self.vcn.append("Nominee 2")
            self.vcb.append("BATCH 1")
            self.vcb.append("BATCH 2")
            self.vcb1=self.vcb[0]
            self.vcb2=self.vcb[1]
        # -----------------------------------------------------------------------------------------------------------------------------------------------------------

        i=0
        for nm in self.cn:
            self.rc=Radiobutton(self.fcap,font=("Constania",18,"bold"),text=nm,padx=40,bg="#FEFCFF",fg="#2B3856",variable=self.v1,value=nm,relief="flat",anchor="w")
            self.rc.grid(row=2,column=i,pady=20,sticky=W)
            i+=2
        self.cbat=Label(self.fcap,font=("Constania",16,"bold"),text=self.cb1,padx=65,width=25,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=3,column=0,sticky=W)
        self.cbat1=Label(self.fcap,font=("Constania",16,"bold"),text=self.cb2,padx=65,width=10,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=3,column=2,sticky=W)

        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.vcap=Frame(self.mid2,width=1000,height=50,bd=0,bg="#FEFCFF",relief="raise")
        self.vcap.pack(expand=TRUE,fill=BOTH)
        self.lvcap=Label(self.vcap,font=("Constania",24,"bold"),bg="#2B3856",fg="#FEFCFF",padx=10,borderwidth=5,bd=5,width=35,text="VICE-CAPTAIN NOMINEES",relief="raise",anchor="w").pack(fill=X,pady=2)
        self.fvcap=Frame(self.vcap,width=1000,height=250,bd=0,bg="#FEFCFF",relief="raise")
        self.fvcap.pack(expand=TRUE,fill=BOTH)
        self.hvcl=Label(self.fvcap,font=("Constania",18,"bold"),text="Choose Your House Vice-Captain",width=25,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.v2=StringVar()
        self.v2.set("0")
        # -----------------------------------------------------------------------------------------------------------------------------------------------------------
        i=0
        for nm1 in self.vcn:
            self.rvc=Radiobutton(self.fvcap,font=("Constania",18,"bold"),text=nm1,padx=40,bg="#FEFCFF",fg="#2B3856",variable=self.v2,value=nm1,relief="flat",anchor="w").grid(row=2,column=i,pady=20,sticky=W)
            i+=2
        self.vcbat=Label(self.fvcap,font=("Constania",16,"bold"),text=self.vcb1,padx=65,width=25,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=3,column=0,sticky=W)
        self.vcbat1=Label(self.fvcap,font=("Constania",16,"bold"),text=self.vcb2,padx=65,width=10,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=3,column=2,sticky=W)

        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.bot1=Frame(self.bottom,width=50,height=100,bd=0,bg="#2B3856",relief='raise')
        self.bot1.pack(expand=TRUE,side=RIGHT)
        self.cp=Button(self.bot1,text="Proceed",font=("Constania",16,"bold"),width=20,borderwidth=5,bd=5,bg="#4863A0",fg="#FEFCFF",command=self.w_vote,relief="raise",anchor="center").grid(row=0,column=0,padx=30,pady=30,sticky=E)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def logout(self):
        self.z2 = lambda: self.controller.show_frame(Login_Page)
        self.clear()
        return self.z2()

    def call_nom_record(self):
        cur.execute('SELECT * FROM Nominee_Details')
        self.data=cur.fetchall()
        return self.data
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def call_house_record(self):
        cur2.execute('SELECT * FROM House_Record_Details')
        self.data1=cur2.fetchall()
        return self.data1
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def retrieve(self):
        self.v_list=[]
        self.ccap=self.v1.get()
        self.cvcap=self.v2.get()
        self.v_list.append(self.ccap)
        self.v_list.append(self.cvcap)
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def w_vote(self):
        self.retrieve()
        ob=Login_Page(parent=None,controller=self.controller)
        p=ob.enrol()
        c=0
        for i in self.v_list:
            if i=='0':
                c+=1
        if c==0:
            cur3.execute('UPDATE Voter_Details SET captain=? WHERE enr_no=?',(self.v_list[0],p))
            db3.commit()
            cur3.execute('UPDATE Voter_Details SET vcaptain=? WHERE enr_no=?', (self.v_list[1],p))
            db3.commit()
            tkMessageBox.showinfo("Status","Thanks For Voting...")
            self.logout()
        else:
            tkMessageBox.showerror("Error!","Inappropriate Selection!!!")
            self.clear()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def clear(self):
        self.v1.set("0")
        self.v2.set("0")
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def show_nominee(self):
        self.cname=[]
        self.cbatch=[]
        self.vcname=[]
        self.vcbatch=[]
        data=self.call_nom_record()
        data1=self.call_house_record()
        for row in data:
            if row[3]=='White House':
                for r in data1:
                    if r[0]=='White House':
                        if r[1]==2 and r[2]==2:
                            if row[4]=='Vice - Captain':
                                self.vcname.append(row[1])
                                self.vcbatch.append(row[2])
                            elif row[4]=='Captain':
                                self.cname.append(row[1])
                                self.cbatch.append(row[2])
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
class Orange_House(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller=controller
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.top=Frame(self,width=1000,height=120,bd=5,bg="#2B3856",relief='raise')
        self.top.pack(side=TOP,fill=BOTH)
        self.ltop=Frame(self.top,width=800,height=100,bd=0,bg="#2B3856",relief='raise')
        self.ltop.pack(side=LEFT,fill=BOTH,expand=TRUE)
        self.rtop=Frame(self.top,width=200,height=100,bd=0,bg="#2B3856",relief='raise')
        self.rtop.pack(side=RIGHT,fill=BOTH,expand=TRUE)
        self.olb=Label(self.ltop,font=("Times New Roman",30,"bold"),height=2,padx=10,text="Orange HOUSE NOMINEES",bd=0,bg="#2B3856",fg="#FEFCFF",relief="raise",anchor="w").pack(fill=BOTH)
        self.olg=Button(self.rtop,text="Logout",font=("Constania",16,"bold"),width=6,padx=20,borderwidth=5,bd=5,bg="#4863A0",fg="#FEFCFF",command=self.logout,relief="raise",anchor="center").pack(side=RIGHT,padx=20)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.bottom=Frame(self,width=1000,height=100,bd=5,bg="#2B3856",relief="raise")
        self.bottom.pack(side=BOTTOM,fill=BOTH)
        self.mid=Frame(self,width=1000,height=500,bd=5,bg="#FEFCFF",relief="raise")
        self.mid.pack(side=TOP,fill=BOTH,expand=TRUE)
        self.mid1=Frame(self.mid,width=1000,height=250,bd=5,bg="#FEFCFF",relief="raise")
        self.mid1.pack(expand=TRUE,fill=BOTH)
        self.mid2=Frame(self.mid,width=1000,height=250,bd=5,bg="#FEFCFF",relief="raise")
        self.mid2.pack(expand=TRUE,fill=BOTH)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.cap=Frame(self.mid1,width=1000,height=50,bd=0,bg="#FEFCFF",relief="raise")
        self.cap.pack(expand=TRUE,fill=BOTH)
        self.lcap=Label(self.cap,font=("Constania",24,"bold"),bg="#2B3856",fg="#FEFCFF",padx=10,borderwidth=5,bd=5,width=25,text="CAPTAIN NOMINEES",relief="raise",anchor="w").pack(fill=X,pady=2)
        self.fcap=Frame(self.cap,width=1000,height=250,bd=0,bg="#FEFCFF",relief="raise")
        self.fcap.pack(expand=TRUE,fill=BOTH)
        self.hcl=Label(self.fcap,font=("Constania",18,"bold"),text="Choose Your House Captain",width=25,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=0,column=0,padx=10,pady=10,sticky=W)
        self.v1=StringVar()
        self.v1.set("0")
        # -----------------------------------------------------------------------------------------------------------------------------------------------------------
        n = self.call_house_record()
        c=1
        self.cn=[]
        self.vcn=[]
        self.cb=[]
        self.vcb=[]
        for row in n:
            if row[0] == 'Orange House':
                if row[1] == 2 and row[2] == 2:
                    self.show_nominee()
                    self.cn = self.cname
                    self.vcn = self.vcname
                    self.cb = self.cbatch
                    self.vcb = self.vcbatch
                    self.cb1 = "BATCH - " + self.cb[0]
                    self.cb2 = "BATCH - " + self.cb[1]
                    self.vcb1 = "BATCH - " + self.vcb[0]
                    self.vcb2 = "BATCH - " + self.vcb[1]
                    c=0
                break
            else:
                c=1
        if c==1:
            self.cn.append("Nominee 1")
            self.cn.append("Nominee 2")
            self.cb.append("BATCH 1")
            self.cb.append("BATCH 2")
            self.cb1=self.cb[0]
            self.cb2=self.cb[1]
            self.vcn.append("Nominee 1")
            self.vcn.append("Nominee 2")
            self.vcb.append("BATCH 1")
            self.vcb.append("BATCH 2")
            self.vcb1=self.vcb[0]
            self.vcb2=self.vcb[1]
        # -----------------------------------------------------------------------------------------------------------------------------------------------------------
        i=0
        for nm in self.cn:
            self.rc=Radiobutton(self.fcap,font=("Constania",18,"bold"),text=nm,padx=40,bg="#FEFCFF",fg="#2B3856",variable=self.v1,value=nm,relief="flat",anchor="w").grid(row=2,column=i,pady=20,sticky=W)
            i+=2
        self.cbat=Label(self.fcap,font=("Constania",16,"bold"),text=self.cb1,padx=65,width=25,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=3,column=0,sticky=W)
        self.cbat1=Label(self.fcap,font=("Constania",16,"bold"),text=self.cb2,padx=65,width=10,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=3,column=2,sticky=W)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.vcap=Frame(self.mid2,width=1000,height=50,bd=0,bg="#FEFCFF",relief="raise")
        self.vcap.pack(expand=TRUE,fill=BOTH)
        self.lvcap=Label(self.vcap,font=("Constania",24,"bold"),bg="#2B3856",fg="#FEFCFF",padx=10,borderwidth=5,bd=5,width=35,text="VICE-CAPTAIN NOMINEES",relief="raise",anchor="w").pack(fill=X,pady=2)
        self.fvcap=Frame(self.vcap,width=1000,height=250,bd=0,bg="#FEFCFF",relief="raise")
        self.fvcap.pack(expand=TRUE,fill=BOTH)
        self.hvcl=Label(self.fvcap,font=("Constania",18,"bold"),text="Choose Your House Vice-Captain",width=25,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.v2=StringVar()
        self.v2.set("0")
        i=0
        for nm1 in self.vcn:
            self.rvc=Radiobutton(self.fvcap,font=("Constania",18,"bold"),text=nm1,padx=40,bg="#FEFCFF",fg="#2B3856",variable=self.v2,value=nm1,relief="flat",anchor="w").grid(row=2,column=i,pady=20,sticky=W)
            i+=2
        self.vcbat=Label(self.fvcap,font=("Constania",16,"bold"),text=self.vcb1,padx=65,width=25,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=3,column=0,sticky=W)
        self.vcbat1=Label(self.fvcap,font=("Constania",16,"bold"),text=self.vcb2,padx=65,width=10,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=3,column=2,sticky=W)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.bot1=Frame(self.bottom,width=50,height=100,bd=0,bg="#2B3856",relief='raise')
        self.bot1.pack(expand=TRUE,side=RIGHT)
        self.cp=Button(self.bot1,text="Proceed",font=("Constania",16,"bold"),width=20,borderwidth=5,bd=5,bg="#4863A0",fg="#FEFCFF",command=self.o_vote,relief="raise",anchor="center").grid(row=0,column=0,padx=30,pady=30,sticky=E)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def logout(self):
        self.z3 = lambda: self.controller.show_frame(Login_Page)
        self.clear()
        return self.z3()
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
    def call_nom_record(self):
        cur.execute('SELECT * FROM Nominee_Details')
        self.data = cur.fetchall()
        return self.data

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
    def call_house_record(self):
        cur2.execute('SELECT * FROM House_Record_Details')
        self.data1 = cur2.fetchall()
        return self.data1

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
    def retrieve(self):
        self.v_list = []
        self.ccap = self.v1.get()
        self.cvcap = self.v2.get()
        self.v_list.append(self.ccap)
        self.v_list.append(self.cvcap)
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
    def o_vote(self):
        self.retrieve()
        ob=Login_Page(parent=None,controller=self.controller)
        p=ob.enrol()
        c=0
        for i in self.v_list:
            if i=='0':
                c+=1
        if c==0:
            cur3.execute('UPDATE Voter_Details SET captain=? WHERE enr_no=?',(self.v_list[0],p))
            db3.commit()
            cur3.execute('UPDATE Voter_Details SET vcaptain=? WHERE enr_no=?', (self.v_list[1],p))
            db3.commit()
            tkMessageBox.showinfo("Status","Thanks For Voting...")
            self.logout()
        else:
            tkMessageBox.showerror("Error!","Inappropriate Selection!!!")
            self.clear()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def clear(self):
        self.v1.set("0")
        self.v2.set("0")
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def show_nominee(self):
        self.cname = []
        self.cbatch = []
        self.vcname = []
        self.vcbatch = []
        data = self.call_nom_record()
        data1 = self.call_house_record()
        for row in data:
            if row[3] == 'Orange House':
                for r in data1:
                    if r[0] == 'Orange House':
                        if r[1] == 2 and r[2] == 2:
                            if row[4] == 'Vice - Captain':
                                self.vcname.append(row[1])
                                self.vcbatch.append(row[2])
                            elif row[4] == 'Captain':
                                self.cname.append(row[1])
                                self.cbatch.append(row[2])
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
class Green_House(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller=controller
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.top=Frame(self,width=1000,height=120,bd=5,bg="#2B3856",relief='raise')
        self.top.pack(side=TOP,fill=BOTH)
        self.ltop=Frame(self.top,width=800,height=100,bd=0,bg="#2B3856",relief='raise')
        self.ltop.pack(side=LEFT,fill=BOTH,expand=TRUE)
        self.rtop=Frame(self.top,width=200,height=100,bd=0,bg="#2B3856",relief='raise')
        self.rtop.pack(side=RIGHT,fill=BOTH,expand=TRUE)
        self.glb=Label(self.ltop,font=("Times New Roman",30,"bold"),height=2,padx=10,text="GREEN HOUSE NOMINEES",bd=0,bg="#2B3856",fg="#FEFCFF",relief="raise",anchor="w").pack(fill=BOTH)
        self.glg=Button(self.rtop,text="Logout",font=("Constania",16,"bold"),width=6,padx=20,borderwidth=5,bd=5,bg="#4863A0",fg="#FEFCFF",command=self.logout,relief="raise",anchor="center").pack(side=RIGHT,padx=20)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.bottom=Frame(self,width=1000,height=100,bd=5,bg="#2B3856",relief="raise")
        self.bottom.pack(side=BOTTOM,fill=BOTH)
        self.mid=Frame(self,width=1000,height=500,bd=5,bg="#FEFCFF",relief="raise")
        self.mid.pack(side=TOP,fill=BOTH,expand=TRUE)
        self.mid1=Frame(self.mid,width=1000,height=250,bd=5,bg="#FEFCFF",relief="raise")
        self.mid1.pack(expand=TRUE,fill=BOTH)
        self.mid2=Frame(self.mid,width=1000,height=250,bd=5,bg="#FEFCFF",relief="raise")
        self.mid2.pack(expand=TRUE,fill=BOTH)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.cap=Frame(self.mid1,width=1000,height=50,bd=0,bg="#FEFCFF",relief="raise")
        self.cap.pack(expand=TRUE,fill=BOTH)
        self.lcap=Label(self.cap,font=("Constania",24,"bold"),bg="#2B3856",fg="#FEFCFF",padx=10,borderwidth=5,bd=5,width=25,text="CAPTAIN NOMINEES",relief="raise",anchor="w").pack(fill=X,pady=2)
        self.fcap=Frame(self.cap,width=1000,height=250,bd=0,bg="#FEFCFF",relief="raise")
        self.fcap.pack(expand=TRUE,fill=BOTH)
        self.hcl=Label(self.fcap,font=("Constania",18,"bold"),text="Choose Your House Captain",width=25,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=0,column=0,padx=10,pady=10,sticky=W)
        self.v1=StringVar()
        self.v1.set("0")
        # -----------------------------------------------------------------------------------------------------------------------------------------------------------
        n = self.call_house_record()
        c = 1
        self.cn = []
        self.vcn = []
        self.cb = []
        self.vcb = []
        for row in n:
            if row[0] == 'Green House':
                if row[1] == 2 and row[2] == 2:
                    self.show_nominee()
                    self.cn = self.cname
                    self.vcn = self.vcname
                    self.cb = self.cbatch
                    self.vcb = self.vcbatch
                    self.cb1 = "BATCH - " + self.cb[0]
                    self.cb2 = "BATCH - " + self.cb[1]
                    self.vcb1 = "BATCH - " + self.vcb[0]
                    self.vcb2 = "BATCH - " + self.vcb[1]
                    c = 0
                break
            else:
                c=1
        if c == 1:
            self.cn.append("Nominee 1")
            self.cn.append("Nominee 2")
            self.cb.append("BATCH 1")
            self.cb.append("BATCH 2")
            self.cb1 = self.cb[0]
            self.cb2 = self.cb[1]
            self.vcn.append("Nominee 1")
            self.vcn.append("Nominee 2")
            self.vcb.append("BATCH 1")
            self.vcb.append("BATCH 2")
            self.vcb1 = self.vcb[0]
            self.vcb2 = self.vcb[1]
        # -----------------------------------------------------------------------------------------------------------------------------------------------------------
        i=0
        for nm in self.cn:
            self.rc=Radiobutton(self.fcap,font=("Constania",18,"bold"),text=nm,padx=40,bg="#FEFCFF",fg="#2B3856",variable=self.v1,value=nm,relief="flat",anchor="w").grid(row=2,column=i,pady=20,sticky=W)
            i+=2
        self.cbat=Label(self.fcap,font=("Constania",16,"bold"),text=self.cb1,padx=65,width=25,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=3,column=0,sticky=W)
        self.cbat1=Label(self.fcap,font=("Constania",16,"bold"),text=self.cb2,padx=65,width=10,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=3,column=2,sticky=W)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.vcap=Frame(self.mid2,width=1000,height=50,bd=0,bg="#FEFCFF",relief="raise")
        self.vcap.pack(expand=TRUE,fill=BOTH)
        self.lvcap=Label(self.vcap,font=("Constania",24,"bold"),bg="#2B3856",fg="#FEFCFF",padx=10,borderwidth=5,bd=5,width=35,text="VICE-CAPTAIN NOMINEES",relief="raise",anchor="w").pack(fill=X,pady=2)
        self.fvcap=Frame(self.vcap,width=1000,height=250,bd=0,bg="#FEFCFF",relief="raise")
        self.fvcap.pack(expand=TRUE,fill=BOTH)
        self.hvcl=Label(self.fvcap,font=("Constania",18,"bold"),text="Choose Your House Vice-Captain",width=25,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.v2=StringVar()
        self.v2.set("0")
        i=0
        for nm1 in self.vcn:
            self.rvc=Radiobutton(self.fvcap,font=("Constania",18,"bold"),text=nm1,padx=40,bg="#FEFCFF",fg="#2B3856",variable=self.v2,value=nm1,relief="flat",anchor="w").grid(row=2,column=i,pady=20,sticky=W)
            i+=2
        self.vcbat=Label(self.fvcap,font=("Constania",16,"bold"),text=self.vcb1,padx=65,width=25,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=3,column=0,sticky=W)
        self.vcbat1=Label(self.fvcap,font=("Constania",16,"bold"),text=self.vcb2,padx=65,width=10,height=1,fg="#2B3856",bg="#FEFCFF",anchor="w").grid(row=3,column=2,sticky=W)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.bot1=Frame(self.bottom,width=50,height=100,bd=0,bg="#2B3856",relief='raise')
        self.bot1.pack(expand=TRUE,side=RIGHT)
        self.cp=Button(self.bot1,text="Proceed",font=("Constania",16,"bold"),width=20,borderwidth=5,bd=5,bg="#4863A0",fg="#FEFCFF",command=self.g_vote,relief="raise",anchor="center").grid(row=0,column=0,padx=30,pady=30,sticky=E)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def logout(self):
        self.z4 = lambda: self.controller.show_frame(Login_Page)
        self.clear()
        return self.z4()
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
    def call_nom_record(self):
        cur.execute('SELECT * FROM Nominee_Details')
        self.data = cur.fetchall()
        return self.data

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
    def call_house_record(self):
        cur2.execute('SELECT * FROM House_Record_Details')
        self.data1 = cur2.fetchall()
        return self.data1
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def retrieve(self):
        self.v_list = []
        self.ccap = self.v1.get()
        self.cvcap = self.v2.get()
        self.v_list.append(self.ccap)
        self.v_list.append(self.cvcap)
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def g_vote(self):
        self.retrieve()
        ob=Login_Page(parent=None,controller=self.controller)
        p=ob.enrol()
        c=0
        for i in self.v_list:
            if i=='0':
                c+=1
        if c==0:
            cur3.execute('UPDATE Voter_Details SET captain=? WHERE enr_no=?',(self.v_list[0],p))
            db3.commit()
            cur3.execute('UPDATE Voter_Details SET vcaptain=? WHERE enr_no=?', (self.v_list[1],p))
            db3.commit()
            tkMessageBox.showinfo("Status","Thanks For Voting...")
            self.logout()
        else:
            tkMessageBox.showerror("Error!","Inappropriate Selection!!!")
            self.clear()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def clear(self):
        self.v1.set("0")
        self.v2.set("0")
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
    def show_nominee(self):
        self.cname = []
        self.cbatch = []
        self.vcname = []
        self.vcbatch = []
        data = self.call_nom_record()
        data1 = self.call_house_record()
        for row in data:
            if row[3] == 'Green House':
                for r in data1:
                    if r[0] == 'Green House':
                        if r[1] == 2 and r[2] == 2:
                            if row[4] == 'Vice - Captain':
                                self.vcname.append(row[1])
                                self.vcbatch.append(row[2])
                            elif row[4] == 'Captain':
                                self.cname.append(row[1])
                                self.cbatch.append(row[2])
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__=='__main__':
    window=MainWindow()
    window.mainloop()

