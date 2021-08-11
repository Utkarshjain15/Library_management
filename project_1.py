from tkinter import*
from tkinter import messagebox
import mysql.connector;
from PIL import ImageTk,Image
root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")
same=True
n=1.5
background_image = Image.open(r"D:\\A224 IV\\PL\\lib1.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size
newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)
con = mysql.connector.connect(host="localhost" ,user="root" ,password="*********" ,database="____")
if con.is_connected():
    print("Mysql Database connected")
cursor=con.cursor()
def IssueBook():
    root = Tk()
    root.geometry('500x500')
    root.title("IssueBook")
    bookID= IntVar()
    author= StringVar()
    stu_id= StringVar()
    lib_id= IntVar()
    bookname= StringVar()
    issuedate= StringVar()
    id_1=bookID.get()
    ath=author.get()
    stid=stu_id.get()
    lbid=lib_id.get()
    name=bookname.get()
    date=issuedate.get()
        
    try:
        cursor.execute('insert into books (Book_id , Author, Student_ID , library_id , book_name , issue_date) VALUES(?,?,?,?,?,?)',(id_1,ath,stid,lbid,name,date,))
        con.commit()
    except:
        con.rollback()
    label_0 = Label(root, text="Details",width=40,font=("bold", 20))
    label_0.place(x=4,y=23)
    label_1 = Label(root, text="Book ID",width=20,font=("bold", 10))
    label_1.place(x=80,y=110)
    entry_1 = Entry(root,textvar= bookID)
    entry_1.place(x=240,y=110)
    label_2 = Label(root, text="Book Name",width=20,font=("bold", 10))
    label_2.place(x=68,y=140)
    entry_2 = Entry(root,textvar= bookname)
    entry_2.place(x=240,y=140)
    label_3 = Label(root, text="Book author",width=20,font=("bold", 10))
    label_3.place(x=68,y=170)
    entry_3 = Entry(root,textvar= author)
    entry_3.place(x=240,y=170)
    label_4 = Label(root, text="Student ID",width=20,font=("bold", 10))
    label_4.place(x=80,y=200)
    entry_4 = Entry(root,textvar= stu_id)
    entry_4.place(x=240,y=200)
    label_5 = Label(root, text="library ID",width=20,font=("bold", 10))
    label_5.place(x=68,y=230)
    entry_5 = Entry(root,textvar= lib_id)
    entry_5.place(x=240,y=230)
    label_6 = Label(root, text="Todays Date in(dd/mm/yyyy)",width=20,font=("bold", 10))
    label_6.place(x=68,y=260)
    entry_6 = Entry(root,textvar= issuedate)
    entry_6.place(x=240,y=260)
    Button(root, text='Submit',width=10,bg='brown',fg='white',command=root.destroy).place(x=180,y=350)
    print("Data entered successfully")
def View(): 
    bookTable = "books"
    root = Tk()
    root.title("Books List")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font = ('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    Label(labelFrame, text="%-10s%-40s%-30s%-60s"%('BID','Title','Author','Library ID'),
    bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text = "----------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)
    
    try:
        cursor.execute("select Book_ID, book_name, Author, library_ID from books")
        cur = cursor.fetchall()
        for i in cur:
            Label(labelFrame,text="%-10s%-30s%-30s%-60s"%(i[0],i[1],i[2],i[3]) ,bg='black', fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)

def Vendor(): 
    root = Tk()
    root.title("Vendors List")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Vendor List", bg='black', fg='white', font = ('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    Label(labelFrame, text="%-10s%-40s%-30s%-60s"%('Vendor ID','Name','Address','Email ID'),
    bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text = "----------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)
    
    try:
        cursor.execute("select Vendor_ID, Vendor_name, address, email_ID from vendors")
        cur = cursor.fetchall()
        for i in cur:
            Label(labelFrame,text="%-10s%-30s%-30s%-60s"%(i[0],i[1],i[2],i[3]) ,bg='black', fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)

def Student():
    root = Tk()
    root.geometry('500x500')
    root.title("Student Record Entry")
    mobile= IntVar()
    name= StringVar()
    stu_id= StringVar()
    email= StringVar()
    address= StringVar()
    n=name.get()
    m=mobile.get()
    stid=stu_id.get()
    eid=email.get()
    add=address.get()
        
    try:
        cursor.execute('insert into StudentS (student_ID , student_name , Mobile_No , Email_ID , address ) VALUES(?,?,?,?,?)',(stid,n,m,eid,add,))
        con.commit()
    except:
        con.rollback()
    label_0 = Label(root, text="Details",width=40,font=("bold", 20))
    label_0.place(x=4,y=23)
    label_1 = Label(root, text="Student ID",width=20,font=("bold", 10))
    label_1.place(x=80,y=110)
    entry_1 = Entry(root,textvar= stu_id)
    entry_1.place(x=240,y=110)
    label_2 = Label(root, text="Student Name",width=20,font=("bold", 10))
    label_2.place(x=68,y=140)
    entry_2 = Entry(root,textvar= name)
    entry_2.place(x=240,y=140)
    label_3 = Label(root, text="Mobile No",width=20,font=("bold", 10))
    label_3.place(x=68,y=170)
    entry_3 = Entry(root,textvar= mobile)
    entry_3.place(x=240,y=170)
    label_4 = Label(root, text="Email ID",width=20,font=("bold", 10))
    label_4.place(x=80,y=200)
    entry_4 = Entry(root,textvar= email)
    entry_4.place(x=240,y=200)
    label_5 = Label(root, text="Address",width=20,font=("bold", 10))
    label_5.place(x=68,y=230)
    entry_5 = Entry(root,textvar= address)
    entry_5.place(x=240,y=230)
    Button(root, text='Submit',width=10,bg='brown',fg='white',command=root.destroy).place(x=180,y=350)
    print("Data entered successfully")
    
def StudentList(): 
    root = Tk()
    root.title("Student Record")
    root.minsize(width=400,height=400)
    root.geometry("750x600")
    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Student List", bg='black', fg='white', font = ('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.88,relheight=0.5)
    y = 0.25
    Label(labelFrame, text="%-10s%-40s%-30s%-40s%-30s"%('Student ID','Name','Mobile','Email ID','Address'),
    bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text = "--------------------------------------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)
    
    try:
        cursor.execute("select * from StudentS")
        cur = cursor.fetchall()
        for i in cur:
            Label(labelFrame,text="%-10s%-30s%-30s%-40s%-30s"%(i[0],i[1],i[2],i[3],i[4]) ,bg='black', fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n NMIMS Library", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Issue Book ",bg='black', fg='white' , command=IssueBook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Vendors List",bg='black', fg='white',command=Vendor)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="Add Student in record",bg='black', fg='white',command=Student)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text=" View Student List",bg='black', fg='white',command=StudentList)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

root.mainloop()


