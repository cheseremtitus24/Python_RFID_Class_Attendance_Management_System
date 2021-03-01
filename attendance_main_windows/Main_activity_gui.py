import time
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

# This file will be responsible for user registration and the reading of the rfid special UID that will
# be saved in the database

# todo: there should be an admin account that has the permission/ authorization to delete,update the records
# and also a guest user who should be able to create and only update a particular field.
# todo: create an option to generate a pdf of the atttending students
from tkinter import messagebox

# todo: On selection of an option from the options menu the unit_sessions table should be populated by a unit_id and
#  on time_out this table should have its content truncated todo: When the options menu is selected then the timer is
#   started the units.sessions_counters should be incremented by one only if a value is set in the unit_sessions table


#tod: change the run_gui_program such that the options menu populates the unit_sessions table and not the time_counter_function that updates this table

# global the_unit
def run_gui_program():
    import MySQLdb

    root = Tk()
    root.title("Python: Simple CRUD Application")

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
            # print(data)
            if data[2] == 1:
                temp = "Present"
                query = f"SELECT surname from attendance.students where student_id ='{data[1]}'"
                cursor.execute(query)
                Surname = cursor.fetchall()

                UnitCode = "Sco"
                # Surname = "Hello"
            else:
                temp = "Absent"



            tree.insert('', 'end', values=(data[0], data[1], temp, data[4], data[5],UnitCode,Surname))
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
        root.after(2000, Read)

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
            result = tkMessageBox.askquestion('Python: Simple CRUD Applition',
                                              'Are you sure you want to delete this record?', icon="warning")
            if result == 'yes':
                curItem = tree.focus()
                contents = (tree.item(curItem))
                selecteditem = contents['values']
                # print(selecteditem)
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
    # todo: make a query to the units table and display the unit name and when it is selected then the start button is pressed retrieve the unit.unit_id and save to unit_sessions
    # connection to the attendance database
    # global the_unit
    # the_unit = None
    def fill_307(filler):
        # the selected compare function should be a list of items contained in the db
        from db_models.set_unit_sessions_unit_code import list_of_units as lou
        list_of_units = lou()

        if filler in list_of_units:
            #retrieve the available unit_id
            from db_models.set_unit_sessions_unit_code import capture_unit_id as cuid
            unit_id = cuid(filler)
            #finally check if a similar value of id exists in the unit_sessions.unit_id and if not first truncate the
            # table and add an entry value else do nothing
            from db_models.set_unit_sessions_unit_code import update_unit_sessions_table as uust
            status = uust(unit_id)
            # todo: Truncate the content in the tqble unit_sessions
            db_conn = MySQLdb.connect("localhost", "root", "", "attendance")

            # open a cursor to the database
            # finding and connecting to a comport automatically

            mycursor = db_conn.cursor()
            test2 = "TRUNCATE table attendance"
            # todo: ensure that when an options menu option is selected it updates the unit_sessions table and then auto_increments the
            # number of units.sessions_counter

            mycursor.execute(test2)





    def fill_309(filler):
        # the selected compare function should be a list of items contained in the db
        from db_models.set_unit_sessions_unit_code import list_of_units as lou
        list_of_units = lou()

        if filler in list_of_units:
            # retrieve the available unit_id
            from db_models.set_unit_sessions_unit_code import capture_unit_id as cuid
            unit_id = cuid(filler)
            # finally check if a similar value of id exists in the unit_sessions.unit_id and if not first truncate the
            # table and add an entry value else do nothing
            from db_models.set_unit_sessions_unit_code import update_unit_sessions_table as uust
            status = uust(unit_id)
            # todo: Truncate the content in the tqble unit_sessions
            db_conn = MySQLdb.connect("localhost", "root", "", "attendance")

            # open a cursor to the database
            # finding and connecting to a comport automatically

            mycursor = db_conn.cursor()
            test2 = "TRUNCATE table attendance"
            # todo: ensure that when an options menu option is selected it updates the unit_sessions table and then auto_increments the
            # number of units.sessions_counter

            mycursor.execute(test2)

    def option_handle( selected):
        # above specific case is simply print(selected) but
        # todo: revisit this function such that it will be retrieving values automatically from the db
        unit_code_1 = "sco-307"
        unit_code_2 = "sco-309"
        if selected == unit_code_1:
            fill_307("sco-307")
        elif selected == unit_code_2:
            fill_309("sco-309")

        # if you specifically want to call methods that has exactly
        # the same name as options
        # eval(selected + "()")
    var = StringVar(Top)
    var.set("Select a unit of study")
    global menu
    menu = OptionMenu(Top,var,'sco-307','sco-309',command=option_handle).place(x=7, y=1)
    # print(var)
    
    #todo: When the counter button is pressed and it is still counting down then you should set the optionmenu to be uneditable
    



    # ==================================LABEL WIDGET=======================================
    txt_title = Label(Top, width=90, font=('arial', 12), text="Start Timer To Initiate Class Session")
    txt_title.place(x=30,y=0)

     #==================================================== Time Counter ===========================
    # Declaration of variables
    hour = StringVar()
    minute = StringVar()
    second = StringVar()

    # setting the default value as 0
    hour.set("00")
    minute.set("00")
    second.set("00")

    # Use of Entry class to take input from the user
    hourEntry = Entry(Top, width=3, font=("Arial", 18, ""),
                      textvariable=hour)
    hourEntry.place(x=242, y=20)

    minuteEntry = Entry(Top, width=3, font=("Arial", 18, ""),
                        textvariable=minute)
    minuteEntry.place(x=302, y=20)

    secondEntry = Entry(Top, width=3, font=("Arial", 18, ""),
                        textvariable=second)
    secondEntry.place(x=362, y=20)


    # global controller
    # controller = False

    def submit():
        #todo: update since the unit_sessions table has already been populated with data by the Option menu select function
        #todo here is to ensure that when this button is pressed the option menu select should be made immutable/uneditable.
        # root.menu.configure(state="disabled")
        # root.menu.configure()
        # todo: Truncate the content in the tqble unit_sessions

        try:
            # the input provided by the user is
            # stored in here :temp
            temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
        except:
            print("Please input the right value")
        while temp > -1:
            #todo: We need to autocall the Read() function so that It can auto-update the attendance window
            root.after(2000, Read)

            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins, secs = divmod(temp, 60)

            # Converting the input entered in mins or secs to hours,
            # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
            # 50min: 0sec)
            hours = 0
            if mins > 60:
                # divmod(firstvalue = temp//60, secondvalue
                # = temp%60)
                hours, mins = divmod(mins, 60)

            # using format () method to store the value up to
            # two decimal places
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            # updating the GUI window after decrementing the
            # temp value every time
            root.update()
            time.sleep(1)

            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if (temp == 0):
                #re-enable to menu OptionMenu once time has expired
                # menu.configure(state="enabled")
                '''
                step1 : increment the sessions counter only when there's an attendance recorded in the db
                #search for an sql query that will count the number of entries in the db and return true if there's atleast two entries.
                # When it returns true we should now increment the class sessions counter
                
                #calling a subroutine to check if session attendance is above 2 student attendees.
                '''
                
                from db_models.confirm_session_is_attended import  check_atleast_if_2_attendees as confirm_session_attend
                status = confirm_session_attend()
                if status: # It is now ok to proceed in updating the sessions counter
                    from db_models.get_current_session_unit_id import get_session_unit_id as update_session
                    unit_id = update_session()
                    from db_models.Increment_attendance_count.increment_sessions_counter import update_attendance_counter as ics
                    ics(unit_id)
                    # time.sleep(1)

                    # Getting a list of present students
                    from db_models.get_students_present import get_present_students as get_student_list
                    students_present = get_student_list()
                    # todo: update the %age student_class_attendance of each studentstudents
                    from db_models.Increment_attendance_count import calculate_attendance_percentage as cap
                    from db_models.Increment_attendance_count import attendance_count_update as acp

                    for student in students_present:
                        acp.update_attendance_counter(student, unit_id)
                        time.sleep(0.2)
                        cap.update_attendance_percentage(student, unit_id)
                        time.sleep(0.2)

                    # time.sleep(1)

                    # update the units_session_counter to facilitate final student unit %age class attendance
                    # time.sleep(0.2)
                    # todo: generate then save pdf to user defined local through a pop up save to path window
                    from db_reporting.Excel_gen import gen_table_report as gtr
                    # todo generate a more refined report with properly defined titled columns
                    gtr
                    time.sleep(0.8)
                    from db_reporting.Excel_gen import gen_percentage_attendance as gpa
                    gpa

                    # todo: Truncate the content in the tqble unit_sessions
                    db_conn = MySQLdb.connect("localhost", "root", "", "attendance")

                    # open a cursor to the database
                    # finding and connecting to a comport automatically

                    mycursor = db_conn.cursor()
                    test2 = "TRUNCATE table unit_sessions"
                    # todo: ensure that when an options menu option is selected it updates the unit_sessions table and then auto_increments the
                    # number of units.sessions_counter

                    mycursor.execute(test2)
                    mycursor.close()
                    messagebox.showinfo("Time Countdown",
                                        "Time's up! Please locate the excel attendance form for this class session")

                    # todo: update the unit_sessions counter by one for the select unit
                    from db_models.Increment_attendance_count import increment_sessions_counter as ics

                
                else:
                    messagebox.showerror("Attendance Error","Students in Attending have not met the minimum Threshold")
                    

                
                
                #todo:
                

            # after every one sec the value of temp will be decremented
            
            # by one
            temp -= 1
        # return controller

    # button widget
    btn = Button(Top, text='Set Time Countdown', bd='5',
                 command=submit)
    btn.place(x=420, y=20)

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
