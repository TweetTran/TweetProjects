# notes: tinker .pack() arranges widgets in vertical or horizontal manner. 
# .grid() place widget in table like structure 
# data name 'detail' is set up differently from the other data due to it lengthly text, therefore the text are place in the 'TEXT' format instead of 'ENTRY' format 
# the 'TEXT' format do not have .get() it required the use of .get("1.0", "end-1c") for retrieval
# get_children() is a function in tkinter that get all the childrens on the parent item ((children are row)) 
# to update the executable application using "pyinstaller --onefile job_tracker.py"
# pip install pyinstaller using "pyinstaller job_tracker.py --onefile" in the cmd 
# the file need to be in an enviroement to be convert to exe

from tkinter import *
from tkinter import ttk
import sqlite3

# Initialized/configured database
# data = [
#     [1, "jn test1", "cn test1", "1/1/1", "ru test1"], 
#     [2,'jn test2', "cn test2", "1/2/3", "ru test2"], 
#     [3, 'jn test3', "cn test3", "1/2/3", "ru test3"]
# ]

# Create database 
conn = sqlite3.connect('application_tracker.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS applications (
          id int,
          job_name text, 
          company_name text, 
          applied_date text, 
          resume_used text, 
          detail text)
          """)

# for record in data:
#     c.execute("INSERT INTO applications VALUES (:id, :job_name, :company_name, :applied_date, :resume_used, :detail)", 
#     {
#         'id': record[0] ,
#         'job_name': record[1],
#         'company_name': record[2],
#         'applied_date': record[3],
#         'resume_used': record[4], 
#         'detail': record[5],
#     })
conn.commit()
conn.close()

def query_database():
    conn = sqlite3.connect('application_tracker.db')
    c = conn.cursor()
    c.execute("SELECT * FROM applications")
    records = c.fetchall()

    # Insert data into Treeview
    global count
    count = 0
    for i in records:
        tree.insert(parent = "", index = "end", iid = count, text = '', values= (i[0], i[1], i[2], i[3], i[4], i[5]))
        print (i)
        count += 1

    conn.commit()
    conn.close()
# # Insert data into Treeview
# global count
# count = 0
# for i in data:
#     tree.insert(parent = "", index = "end", iid = count, text = '', values= (i[0], i[1], i[2], i[3],i[4], i[5]))
#     count += 1



root = Tk()
info_notebook = ttk.Notebook(root)
info_notebook.pack(pady = 15)


# Application name 
root.title("Job Application Tracker")

# Gui style 
style = ttk.Style()

# Gui theme
style.theme_use('default')

# Select highlight 
style.map('Treeview', 
          background = [('selected', "#D3D3D3")]) 

# Initialize treeframe 
job_frame = Frame(info_notebook)
job_frame.pack()
info_notebook.add(job_frame, text = "Applied Jobs")

tree_frame = Frame(job_frame, width = 250, height = 250)
tree_frame.pack(fill = "both", expand = 1)

# Initialize scrollbar
scroll = Scrollbar(tree_frame)
scroll.pack(side = RIGHT, fill = Y)

# Initialize treeview 
tree = ttk.Treeview(tree_frame, yscrollcommand=scroll.set, selectmode="extended", show="headings")
tree.pack()

# Configure scrollbar 
scroll.config(command=tree.yview)

# Define column names
columns = ("ID","Job Name", "Company Name", "Applied Date", "Resume Used", "Details")

# Initalized columns 
tree["columns"] = columns

# Format columns 
for col in tree["columns"]:
    tree.column(col, anchor = W, width = 200)
    tree.heading(col, text = col, anchor = W)


# Add record to database 
data_frame = LabelFrame(job_frame, text = "Data")
data_frame.pack(fill = "x", expand= "yes", padx = 20)

# Format inputs

jobName_label =Label(data_frame, text = "Job Name")
jobName_label.grid(row = 0, column = 0, padx = 10, pady = 5)

jobName_entry = Entry(data_frame)
jobName_entry.grid(row = 0, column = 1, padx = 10, pady = 5)

companyName_label = Label(data_frame, text = "Company Name")
companyName_label.grid(row = 0, column = 2, padx = 15, pady = 5)

companyName_entry = Entry(data_frame)
companyName_entry.grid(row = 0, column = 3, padx = 10, pady = 5)

appliedDate_label = Label(data_frame, text = "Applied Date")
appliedDate_label.grid(row = 0, column = 4, padx = 15, pady = 5)

appliedDate_entry = Entry(data_frame)
appliedDate_entry.grid(row = 0, column = 5, padx = 10, pady = 5)
 
resumeUse_label = Label(data_frame, text = "Resume Used")
resumeUse_label.grid(row = 0, column = 6, padx = 20, pady = 5)

resumeUse_entry = Entry(data_frame)
resumeUse_entry.grid(row = 0, column = 7, padx = 10, pady = 5)

id_entry = Entry(data_frame)

# Different Frame (Connect One Scrollbar to TextBoxes )
data_frame2 = LabelFrame(job_frame, text="Detail")
data_frame2.pack(fill="x", expand="yes", padx=10)
# text_scroll = Scrollbar(data_frame2)
# text_scroll.pack(side = RIGHT, fill =Y)
detail_entry = Text(data_frame2, width=100, height=10) 
detail_entry.grid(row=0, column=0, padx=10, pady=10)


# Add functionality to buttons 
def select_record(e):
    id_entry.delete(0,END)
    jobName_entry.delete(0, END)
    companyName_entry.delete(0, END)
    appliedDate_entry.delete(0, END)
    resumeUse_entry.delete(0, END)
    detail_entry.delete(1.0, END)

    # Retrieve record 
    selected = tree.focus()
    values = tree.item(selected, 'values')

    # Display the record: 0 is position
    id_entry.insert(0,values[0])
    jobName_entry.insert(0, values[1])
    companyName_entry.insert(0, values[2])
    appliedDate_entry.insert(0, values[3])
    resumeUse_entry.insert(0, values[4])
    detail_entry.insert(1.0, values[5])

def clear_entry():
    id_entry.delete(0,END)
    jobName_entry.delete(0, END)
    companyName_entry.delete(0, END)
    appliedDate_entry.delete(0, END)
    resumeUse_entry.delete(0, END)
    detail_entry.delete(1.0, END)

def add_entry():

    conn = sqlite3.connect('application_tracker.db')
    c = conn.cursor()

    # Generate new id 
    # COALESCE in SQL use to return the first non null value   
    c.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM applications")
    new_id = c.fetchone()[0]

    c.execute(" INSERT INTO applications VALUES (:id, :job_name, :company_name, :applied_date, :resume_used, :detail)", 
    {
        'id': new_id,
        'job_name':jobName_entry.get(),
        'company_name': companyName_entry.get(), 
        'applied_date': appliedDate_entry.get(), 
        'resume_used': resumeUse_entry.get(), 
        'detail': detail_entry.get("1.0", "end-1c"),
    }
              )

    conn.commit()
    conn.close()

    clear_entry()

    # Reload the tree
    tree.delete(*tree.get_children())
    query_database()

def update_entry():
    selected = tree.focus()
    tree.item(selected, text = "", values = (id_entry.get(), jobName_entry.get(), companyName_entry.get(), appliedDate_entry.get(), resumeUse_entry.get(), detail_entry.get("1.0", "end-1c")))

    conn = sqlite3.connect('application_tracker.db')
    c = conn.cursor()
    c.execute("""UPDATE applications SET
              job_name = :job,
              company_name = :company,
              applied_date = :date,
              resume_used = :resume,
              detail= :detail

              WHERE oid = :oid""",
              {
                  'job':jobName_entry.get(),
                  'company': companyName_entry.get(), 
                  'date' : appliedDate_entry.get(), 
                  'resume': resumeUse_entry.get(), 
                  'detail': detail_entry.get("1.0", "end-1c"),
                  'oid': id_entry.get(),
              }
              )

    conn.commit()
    conn.close()

    clear_entry()

def remove_anEntry():
    target = tree.selection()[0]
    tree.delete(target)

    conn = sqlite3.connect('application_tracker.db')
    c = conn.cursor()
    c.execute("DELETE from applications WHERE id= "+ id_entry.get())

    conn.commit()
    conn.close()

    # Clear out all entry
    clear_entry()

def remove_manyEntry():
    target = tree.selection()
    for number in target:
        tree.delete(number)

def search_entry():
    search_job = jobName_entry.get()
    search_company = companyName_entry.get()   

    for record in tree.get_children():
        tree.delete(record)

    conn = sqlite3.connect('application_tracker.db')
    c = conn.cursor()
    if search_job and search_company:
        c.execute("SELECT * FROM applications WHERE job_name like ? AND company_name like ?", (search_job, search_company,))
    elif search_job:
        c.execute("SELECT * FROM applications WHERE job_name like ?", (search_job,))
    elif search_company:
        c.execute("SELECT * FROM applications WHERE company_name like ?", (search_company,))
    else: 
        pass
    records = c.fetchall()
     
    # Insert data into Treeview
    global count
    count = 0
    for i in records:
        tree.insert(parent = "", index = "end", iid = count, text = '', values= (i[0], i[1], i[2], i[3], i[4], i[5]))
        print (i)
        count += 1

    conn.commit()
    conn.close()

def reset_view():
    for record in tree.get_children():
        tree.delete(record)
    
    query_database()
    

# Add buttons layout
button_frame =LabelFrame(job_frame, text= "Options")
button_frame.pack(fill = "x", expand = "yes", padx = 20)

search_button = Button(button_frame, text = "Search", command = search_entry)
search_button.grid(row = 0, column = 0, padx = 10, pady = 10)

add_button = Button(button_frame, text = "Add",command= add_entry)
add_button.grid(row = 0, column = 1, padx = 10, pady = 10)

update_button = Button(button_frame, text = "Update", comman = update_entry)
update_button.grid(row = 0, column = 2, padx = 10, pady = 10)

delete_button = Button(button_frame, text = "Delete", command = remove_anEntry)
delete_button.grid(row = 0, column = 3, padx = 10, pady = 10)

clear_entry_button = Button(button_frame, text = "Clear", command = clear_entry)
clear_entry_button.grid(row = 0, column = 4, padx = 10, pady = 10)

reset_view_button = Button(button_frame, text = "Reset", command = reset_view)
reset_view_button.grid(row = 0, column = 5, padx = 10, pady = 10)

# Selection binding
tree.bind("<ButtonRelease-1>", select_record)

query_database()


#### 2ND TAB ###
company_frame = Frame(info_notebook, width = 250, height = 250)
company_frame.pack(fill = "both", expand = 1)
info_notebook.add(company_frame, text = "Company")

view_frame = Frame(company_frame, width = 250, height = 250)
view_frame.pack(fill = "both", expand = 1)

# Initialize scrollbar
view_scroll = Scrollbar(view_frame)
view_scroll.pack(side = RIGHT, fill = Y)

# Initialize treeview 
view = ttk.Treeview(view_frame, yscrollcommand=scroll.set, selectmode="extended", show="headings")
view.pack()

# Configure scrollbar 
scroll.config(command=view.yview)

# Define column names
columns_name = ("ID", "Company Name", "About", "Opening", "Questions")

# Initalized columns 
view["columns"] = columns_name

# Format columns 
for i in view["columns"]:
    view.column(i, anchor = W, width = 250)
    view.heading(i, text = i, anchor = W)
          
root.mainloop()
