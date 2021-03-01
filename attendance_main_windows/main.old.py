from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox


# This file will be responsible for user registration and the reading of the rfid special UID that will
# be saved in the database

# todo: there should be an admin account that has the permission/ authorization to delete,update the records
# and also a guest user who should be able to create and only update a particular field.
# todo: create an option to generate a pdf of the atttending students
def run_gui_program():
    import MySQLdb

    root = Tk()
    root.title("Class Attendance Window")
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

    def Read():
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `attendance` ORDER BY `ID` ASC")
        # cursor.execute("SELECT *  FROM students LEFT JOIN attendance ON attendance.attendance_status  = students.attendance_status")
        fetch = cursor.fetchall()
        for data in fetch:
            print(data)
            if data[2] == 1:
                temp = "Present"
                query = f"SELECT surname from attendance.students where student_id ='{data[1]}'"
                cursor.execute(query)
                Surname = cursor.fetchall()

                UnitCode = "Sco"
                # Surname = "Hello"
            else:
                temp = "Absent"

            tree.insert('', 'end', values=(data[0], data[1], temp, data[3], data[4], UnitCode, Surname))
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
            ttime = "N/A"
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

    def Delete():
        if not tree.selection():
            txt_result.config(text="Please select an item first", fg="red")

        else:
            result = tkMessageBox.askquestion('Class Attendance Window',
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
        result = tkMessageBox.askquestion('Python: Simple CRUD Applition', 'Are you sure you want to exit?',
                                          icon="warning")
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
    Button1 = Button(Right, text="Delete_record", command=Delete).pack(side=RIGHT)
    Button2 = Button(Right, text="Read_records", command=Read).pack(side=RIGHT)
    Button2 = Button(Right, text="Quit", command=Exit).pack(side=LEFT)

    # Buttons = Frame(Left, width=50, height=50, bd=8, relief="raise")
    # Buttons.pack(side=BOTTOM)
    # ==================================LABEL WIDGET=======================================
    txt_title = Label(Top, width=900, font=('arial', 24), text="Python: Simple CRUD Application")
    txt_title.pack()
    # todo: create an Options Menu to select the Unit that is being sat for
    # todo: create an sql query to retrieve details from units.unit_name table to populate the OptionMenu values
    '''
    step 2: Creating an sql query for units.Unit_name retrieval and save to a local var
    '''
    try:
        db_conn = MySQLdb.connect("localhost", "root", "", "attendance")
        # open a cursor to the database
        cursor = db_conn.cursor()
        # finding and connecting to a comport automatically

        mycursor = db_conn.cursor()

        #
        # Account_number = nfc_check_exist()
        # print("from within Status output = " + str(Account_number))

        # uid_check = f"SELECT CASE WHEN EXISTS(select  account_number from accounts where account_number = {Account_number} ) THEN CAST(1 as BIT) ELSE CAST(0 as BIT) END "
        # print(f"gotten memb id is {member_id[0]}")
        test2 = f"select unit_name from units "

        mycursor.execute(test2)
        units = mycursor.fetchall()
        print(f"Retrieved Units are as follows {units}")
    except:
        print("Please check that your database server is running and username and password are root,'' respectively")
    finally:
        mycursor.close()

    # todo: on the same top view frame create a command button that will start  a 3 hour count_down timer.

    '''
    step3: Creating a section for a count_down timer
    step3.1: developing the countdown clock in tkinter

    '''

    # todo: Create a gui countdown timer in tkinter and a command button that when the time expires the program produces an excel sheet containing the class attendance.
    '''
    step3.2: develop a subroutine to generate an excel sheet from the data in a db
    '''

    # todo: Furthermore, this button should alter the contents of the attendance.attendance_count for the students who attended the class.{increments by 1}
    # todo: Finally there should be a final gui that will be used in the generation of the final student attendance along with their class attendance agregate for
    # each and every unit that they ever registered for.
    # sample output for each student will be Adm_code Unit_code1 Percentage_attendance
    #                                  Unit_code2 Percentage_attendance

    # ==================================LIST WIDGET========================================
    scrollbary = Scrollbar(Right, orient=VERTICAL)
    scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
    tree = ttk.Treeview(Right,
                        columns=("MemberID", "Firstname", "Lastname", "Gender", "Address", "Username", "Password"),
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
    tree.heading('Username', text="UnitCode", anchor=W)
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
    root.mainloop()


# ==================================INITIALIZATION=====================================
if __name__ == '__main__':
    run_gui_program()
