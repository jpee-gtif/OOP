from tkinter import*

import sqlite3

root=Tk()
root.title("My Project")
root.geometry("500x500")

#database
conn=sqlite3.connect('my_project.db')
c=conn.cursor()


def submit():
    conn=sqlite3.connect('C:/Users/STUDENTS/Documents/my_project.db')
    c=conn.cursor()

    c.execute("INSERT INTO student_info VALUES(:f_name,:l_name,:age,:address,:email)",
              {
                  'f_name': f_name.get(),
                  'l_name':l_name.get(),
                  'age':age.get(),
                  'address':address.get(),
                  'email':email.get(),
                  })
    
    conn.commit()
    conn.close()

    f_name.delete(0,END)
    l_name.delete(0,END)
    age.delete(0,END)
    address.delete(0,END)
    email.delete(0,END)

def query():
    conn=sqlite3.connect('C:/Users/STUDENTS/Documents/my_project.db')
    c=conn.cursor()
    c.execute("SELECT *,oid FROM student_info")
    records=c.fetchall()

    print_records=' '
    for record in records:
        print_records +=str(record[0])+" "+str(record[1])+" "+str(record[2])+" "+str(record[3])+" "+str(record[4])+" "+"\t"+str(record[5])+"/n"
        query_label=Label(root,text=print_records)
        query_label.grid(row=30,column=0,columnspan=2)

    conn.commit
    conn.close()



'''
c.execute ("""CREATE TABLE "students_info"(
          "f_name" TEXT,
          "l_name" TEXT,
          "age" INTEGER,
          "address" TEXT,
          "email" TEXT,
)""")
'''

#clear the text boxes

f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)
l_name=Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20)
age=Entry(root,width=30)
age.grid(row=2,column=1,padx=20)
address=Entry(root,width=30)
address.grid(row=3,column=1,padx=20)
email=Entry(root,width=30)
email.grid(row=4,column=1,padx=20)


#create textbox label
f_name_label=Label(root,text="First Name")
f_name_label.grid(row=0,column=0)
l_name_label=Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)
age_label_label=Label(root,text= "Age")
age_label_label.grid(row=2,column=0)
address_label_label=Label(root,text= "Address")
address_label_label.grid(row=3,column=0)
email_label_label=Label(root,text= "Email")
email_label_label.grid(row=4,column=0)


#create submit button

submit_btn=Button(root,text="Add Record to Database",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

query_btn=Button(root,text="Show Records",command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)
            
root.mainloop()