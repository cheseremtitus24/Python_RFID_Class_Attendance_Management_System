from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

# This file will be responsible for user registration and the reading of the rfid special UID that will
# be saved in the database

# todo: there should be an admin account that has the permission/ authorization to delete,update the records
# and also a guest user who should be able to create and only update a particular field.
import MySQLdb

root = Tk()
root.title("Python: Simple CRUD Applition")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 500
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)


# ==================================METHODS============================================
def Database():
    # todo: add a table column that will be responsible for saving the rfid UID that matches to Student's admission
    #  number first the user should swipe the UID then all the entry fields will be enabled for reading. furthermore
    #  the read in card should be checked for existence and if it already exists the create tab should be disabled

    global conn, cursor
    conn = MySQLdb.connect("localhost", "root", "", "attendance")
    # open a cursor to the database
    cursor = conn.cursor()
    # conn = sqlite3.connect('pythontut.db')
    # cursor = conn.cursor()
    # cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, firstname "
    #                "TEXT, lastname TEXT, gender TEXT, address TEXT, username TEXT, password TEXT)")


# def Create():
#     if  FIRSTNAME.get() == "" or LASTNAME.get() == "" or GENDER.get() == "" or ADDRESS.get() == "" or USERNAME.get() == "" or PASSWORD.get() == "":
#         txt_result.config(text="Please complete the required field!", fg="red")
#     else:
#         Database()
#         cursor.execute("INSERT INTO `member` (firstname, lastname, gender, address, username, password) VALUES(?, ?, "
#                        "?, ?, ?, ?)", (str(FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), str(ADDRESS.get(
#
#         )), str(USERNAME.get()), str(PASSWORD.get())))
#         tree.delete(*tree.get_children())
#         cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")
#         fetch = cursor.fetchall()
#         for data in fetch:
#             tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
#         conn.commit()
#         FIRSTNAME.set("")
#         LASTNAME.set("")
#         GENDER.set("")
#         ADDRESS.set("")
#         USERNAME.set("")
#         PASSWORD.set("")
#         cursor.close()
#         conn.close()
#         txt_result.config(text="Created a data!", fg="green")

def Read():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM `attendance` ORDER BY `ID` ASC")
    # cursor.execute("SELECT *  FROM students LEFT JOIN attendance ON attendance.attendance_status  = students.attendance_status")
    fetch = cursor.fetchall()
    for data in fetch:
        if data[2] == 1:
            temp = "Present"
        else:
            temp = "Absent"
        tree.insert('', 'end', values=(data[0], data[1], temp, data[3], data[4]))
    cursor.close()
    # getting record of students not yet clocked in
    # cursor.execute("SELECT ID,student_id,attendance_status FROM ")
    conn.close()

    Database()
    # cursor.execute("SELECT * FROM `attendance` ORDER BY `current_timer` ASC")
    # if student.student_id
    # cursor.execute("SELECT *  FROM students LEFT JOIN attendance ON attendance.student_id  != students.student_id")
    cursor.execute("SELECT students.* FROM students WHERE student_id NOT IN (SELECT student_id FROM attendance)")
    fetch = cursor.fetchall()
    for data in fetch:
        from time_helper import time_help as thlp
        tdate = thlp.get_current_date()
        ttime = "----"
        if data[2] == 1:
            temp = "Present"
        else:
            temp = "Absent"
        tree.insert('', 'end', values=(data[0], data[1], temp, tdate, ttime))
    cursor.close()

    # getting record of students not yet clocked in
    # cursor.execute("SELECT ID,student_id,attendance_status FROM ")
    # conn.close()

    txt_result.config(text="Successfully read the data from database", fg="black")


# def Update():
#     #todo:
#     if not tree.selection():
#         txt_result.config(text="Please select an item first", fg="red")
#     else:
#         result = tkMessageBox.askquestion('Python: Simple CRUD Applition',
#                                           'Are you sure you want to update this record?', icon="warning")
#         if result == 'yes':
#             curItem = tree.focus()
#             contents = (tree.item(curItem))
#             selecteditem = contents['values']
#             tree.delete(curItem)
#
#             mem_id = selecteditem[0]
#             Database()
#
#
#             # txt_result.config(text="Successfully deleted the data", fg="black")
#             #clears all the fields in the display window
#             tree.delete(*tree.get_children())
#
#             #todo: autofill the empty fields with old values so that the only changed field updates only that record
#             # check if the entry fields have values else refill with those retrieved from the database
#
#             # implement a custom switch case statement in form of a dictionary each entry will be given a number and
#             # a check for (empty|!empty) and if empty should perform function linked to that key
#
#             #### check if input field 1 is empty and if so retrieve entry value and autofill in the entry field
#             # todo: create a function that retrieves values from the sqlite db
#             def zero():
#                 # check status of the input and if it returns true do nothing else fill that particular field with db values
#                 # todo: create a class that is responsible for retrieving specific db values
#                 # if the field entry is empty do the following
#                 if check_input(FIRSTNAME.get()):
#                     from db_model import retrieve_db_values as rdv
#                     value = rdv.return_uid('pythontut.db','firstname','member',mem_id)
#                     FIRSTNAME.set(value)
#                     # retrieve database values that will set the value of this particula empty field
#                     # todo: this value should be passed two values the db_name, mem_id and the field_entry_name to be changed
#
#
#             def process_default():
#                 pass
#             options = {
#                 0:zero(),
#                 1:"one",
#                 2:"two",
#                 3:"three",
#                 4:"four",
#                 5:"five",
#                 6:"six",
#                 7:"seven",
#                 8: "eight"
#             }
#
#             try:
#
#                 num = 33
#                 print(options[num])
#             except KeyError:
#                 process_default()
#
#             #function to check if the input field is empty
#             def check_input(input_entry):
#                 if input_entry.get() == "":
#                     True
#                 else:
#                     False
#
#
#
#
#
#             if FIRSTNAME.get() == "" or LASTNAME.get() == "" or GENDER.get() == "" or ADDRESS.get() == "" or USERNAME.get() == "" or PASSWORD.get() == "":
#                 txt_result.config(text="Please complete the required field!", fg="red")
#
#
#             cursor.execute(
#                 "UPDATE `member` SET `firstname` = ?, `lastname` = ?, `gender` =?,  `address` = ?,  `username` "
#                 "= ?, `password` = ? WHERE `mem_id` = ?", (str(FIRSTNAME.get()), str(LASTNAME.get()),
#                                                            str(GENDER.get()), str(ADDRESS.get()),
#                                                            str(USERNAME.get()), str(PASSWORD.get()),
#                                                            int(mem_id)))
#             conn.commit()
#             cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")
#             fetch = cursor.fetchall()
#             for data in fetch:
#                 tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
#             cursor.close()
#             conn.close()
#             FIRSTNAME.set("")
#             LASTNAME.set("")
#             GENDER.set("")
#             ADDRESS.set("")
#             USERNAME.set("")
#             PASSWORD.set("")
#             btn_create.config(state=NORMAL)
#             btn_read.config(state=NORMAL)
#             btn_update.config(state=NORMAL)
#             btn_delete.config(state=NORMAL)
#             txt_result.config(text="Successfully updated the data", fg="black")


# def Updater():
#     Database()
#     if GENDER.get() == "":
#         txt_result.config(text="Please select a gender", fg="red")
#     else:
#         #todo: add a field that is non-editable when the update field is unselected and that is used for specifying the mem_id
#
#         tree.delete(*tree.get_children())
#         cursor.execute("UPDATE `member` SET `firstname` = ?, `lastname` = ?, `gender` =?,  `address` = ?,  `username` "
#                        "= ?, `password` = ? WHERE `mem_id` = ?", (str(FIRSTNAME.get()), str(LASTNAME.get()),
#                                                                   str(GENDER.get()), str(ADDRESS.get()),
#                                                                   str(USERNAME.get()), str(PASSWORD.get()),
#                                                                   int(mem_id)))
#         conn.commit()
#         cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")
#         fetch = cursor.fetchall()
#         for data in fetch:
#             tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
#         cursor.close()
#         conn.close()
#         FIRSTNAME.set("")
#         LASTNAME.set("")
#         GENDER.set("")
#         ADDRESS.set("")
#         USERNAME.set("")
#         PASSWORD.set("")
#         btn_create.config(state=NORMAL)
#         btn_read.config(state=NORMAL)
#         btn_update.config(state=NORMAL)
#         btn_delete.config(state=NORMAL)
#         txt_result.config(text="Successfully updated the data", fg="black")


def OnSelected(event):
    global mem_id;
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    mem_id = selecteditem[0]
    FIRSTNAME.set("")
    LASTNAME.set("")
    GENDER.set("")
    ADDRESS.set("")
    USERNAME.set("")
    PASSWORD.set("")
    FIRSTNAME.set(selecteditem[1])
    LASTNAME.set(selecteditem[2])
    ADDRESS.set(selecteditem[4])
    USERNAME.set(selecteditem[5])
    PASSWORD.set(selecteditem[6])
    # btn_create.config(state=DISABLED)
    # btn_read.config(state=DISABLED)
    # btn_update.config(state=NORMAL)
    # btn_delete.config(state=DISABLED)


def Delete():
    if not tree.selection():
        txt_result.config(text="Please select an item first", fg="red")

    else:
        result = tkMessageBox.askquestion('Python: Simple CRUD Applition',
                                          'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            print(selecteditem)
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `attendance` WHERE `ID` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
            txt_result.config(text="Successfully deleted the data", fg="black")


def Exit():
    result = tkMessageBox.askquestion('Python: Simple CRUD Applition', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


# ==================================VARIABLES==========================================
FIRSTNAME = StringVar()
LASTNAME = StringVar()
GENDER = StringVar()
ADDRESS = StringVar()
USERNAME = StringVar()
PASSWORD = StringVar()

# ==================================FRAME==============================================
Top = Frame(root, width=900, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
# Left = Frame(root, width=300, height=500, bd=8, relief="raise")
# Left.pack(side=LEFT)
Right = Frame(root, width=900, height=900, bd=8, relief="raise")
Right.pack(side=RIGHT)
txt_result = Label(Right)
txt_result.pack(side=TOP)
# Button = Button(Right, text="Read_attendance", command=Read).pack(side=LEFT)
Button1 = Button(Right,text="Delete_record", command=Delete).pack(side=RIGHT)
Button2 = Button(Right,text="Read_records", command=Read).pack(side=RIGHT)
Button2 = Button(Right,text="Quit", command=Exit).pack(side=LEFT)

# Buttons = Frame(Left, width=50, height=50, bd=8, relief="raise")
# Buttons.pack(side=BOTTOM)
# ==================================LABEL WIDGET=======================================
txt_title = Label(Top, width=900, font=('arial', 24), text="Python: Simple CRUD Application")
txt_title.pack()
# txt_result = Label(Buttons)
# txt_result.pack(side=TOP)

# ==================================BUTTONS WIDGET=====================================
# btn_create = Button(Buttons, width=10, text="Create", command=Create)
# btn_create.pack(side=LEFT)
# btn_read = Button(Buttons, width=10, text="Read", command=Read )
# btn_read.pack(side=LEFT)
# btn_update = Button(Buttons, width=10, text="Update", command=Update)
# btn_update.pack(side=LEFT)
# btn_delete = Button(Buttons, width=10, text="Delete", command=Delete)
# btn_delete.pack(side=LEFT)
# btn_exit = Button(Buttons, width=10, text="Exit", command=Exit)
# btn_exit.pack(side=LEFT)

# ==================================LIST WIDGET========================================
scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = ttk.Treeview(Right, columns=("MemberID", "Firstname", "Lastname", "Gender", "Address", "Username", "Password"),
                    selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('MemberID', text="MemberID", anchor=W)
tree.heading('Firstname', text="ADM. #", anchor=W)
tree.heading('Lastname', text="Attendance Status", anchor=W)
tree.heading('Gender', text="Date", anchor=W)
tree.heading('Address', text="Clock in", anchor=W)
tree.heading('Username', text="Course", anchor=W)
tree.heading('Password', text="Surname", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=80)
tree.column('#5', stretch=NO, minwidth=0, width=150)
tree.column('#6', stretch=NO, minwidth=0, width=120)
tree.column('#7', stretch=NO, minwidth=0, width=120)
tree.pack()
tree.bind('<Double-Button-1>', OnSelected)

# ==================================INITIALIZATION=====================================
if __name__ == '__main__':
    root.mainloop()
