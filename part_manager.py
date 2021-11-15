from tkinter import *
from tkinter import messagebox
from db import Database
db =Database('store.db')
from typing import Collection
def populate_list():
    parts_list.delete(0,END)
    for row in db.fetch():
        parts_list.insert(END,str(row[0])+" "+str(row[1]))
        
def select_item(event):
    try:
        global selected_item  
        index=parts_list.curselection()[0]
        selected_item=parts_list.get(index)
        part_entry.delete(0,END)
        part_entry.insert(END,selected_item[2:])
    except IndexError:
        pass

    
    # print(selected_item)
    # print("select")
def remove_item():
    db.remove(selected_item[0])
    # print(selected_item[0])
    clear_text()
    populate_list()

def add_item():
    if part_text.get()=='':
        messagebox.showerror("Required Fields","Please Fill The Field")
        return
    db.insert(part_text.get())
    parts_list.delete(0,END)
    parts_list.insert(END,(part_text.get()))
    populate_list()
def update_item():
    db.update(selected_item[0],part_text.get())
    populate_list()
    # print("update")
def clear_text():
    part_entry.delete(0,END)
  
app =Tk()

part_text=StringVar()
part_label=Label(app,text="Task Name",font=('bold',14),pady=20,padx=15)
part_label.grid(row=0,column=0,sticky=W)


part_entry=Entry(app,textvariable=part_text,width=30)
part_entry.grid(row=0,column=1)



parts_list=Listbox(app,height=20,width=60,bg="#03FAE9", font=('Helvetica',12))
parts_list.grid(row=3,column=0,columnspan=3,rowspan=6,pady=20, padx=20)
# create Scrollbar
scrollbar=Scrollbar(app)
scrollbar.grid(row=3,column=3)
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)


parts_list.bind('<<ListboxSelect>>',select_item)


add_btn=Button(app,text="Add Task",width=12,command=add_item,bg="#65F208")
add_btn.grid(row=2,column=0,padx=20)

remove_btn=Button(app,text="Remove Task",width=12,command=remove_item,bg="#F24808")
remove_btn.grid(row=2,column=1)

update_btn=Button(app,text="Update Task",width=12,command=update_item,bg="#E808F2")
update_btn.grid(row=2,column=2)

clear_btn=Button(app,text="Clear Task",width=12,command=clear_text,bg="#F3FA03")
clear_btn.grid(row=2,column=3,padx=25)

app.title('ToDo')
app.geometry('1000x800')
populate_list()
app.mainloop()