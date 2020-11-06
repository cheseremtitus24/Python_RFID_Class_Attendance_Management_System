import MySQLdb
import serial
from MySQLdb.cursors import Cursor
from serial.tools import list_ports

import time

dbConn = MySQLdb.connect("localhost", "root", "", "attendance")
# open a cursor to the database
# cursor = dbConn.cursor()
# finding and connecting to a comport automatically

cdc = next(list_ports.grep("CH340"))
print("Device was found ")
# global ser
# ser = serial.Serial(f'{cdc.device}', baudrate=115200, timeout=1)
time.sleep(2)

device = cdc.device  # this will have to be changed to the serial port you are using
try:
    print("Trying...", device)
    arduino = serial.Serial(device, baudrate=115200, timeout=1)
except:
    print("Failed to connect on", device)
    global data
    global restart
    # restart = True
while True:
    global restart
    restart = False
    if restart:
        data = None

    data = arduino.readline().decode('ascii')
    print(data)
    # print(len(data.split()))

    if len(data.split()) > 0:
        # print("length above zero importing memcheck ")
        from db_helper import check_mem_id_exist  as mem_check

        time.sleep(1)

        val = mem_check.check_mem_id_exist(data.split())
        # time.sleep(2)

        # if the account number exists do the following else sleep for five seconds display smthn

        # time.sleep(1)

        if val:
            print(f"Success read in , ready to continue")
            # the read in id exists in the database now time to fill in the attendance form
            # step1: get the student_id
            from db_helper import get_std_id as gsid

            stud_id = gsid.return_uid(data.split())
            # step2: change the attendance status to 1
            # step3: get current date
            from time_helper import time_help as th

            curr_date = th.get_current_date()
            curr_time = th.get_current_time()
            # pieces = data.split(" ")
            # print(pieces)
            try:
                cursor: Cursor = dbConn.cursor()
                # time.sleep(2)
                #check if same student_id already exists if so skip this [continue]

                exists = mem_check.check_student_id_exist(stud_id.split())
                print(f"Does {stud_id} exist in the attendance table {exists}")
                # time.sleep(2)
                #if it does not exist continue prog execution printing something first
                if exists:
                    print("The Student has already in Attending!!!!!!!! Skip ahead")
                    restart = True
                    continue
                    # continue
                else:
                    status = cursor.execute("""INSERT INTO attendance (student_id,attendance_status,current_dater,current_timer) VALUES (%s,%s,%s,%s)""",(stud_id, 1, curr_date, curr_time))
                    time.sleep(1)
                    dbConn.commit()
                    # time.sleep(1)
                    if status:
                        print("data insertin success")
                        restart = True
                        continue

                    cursor.close()
            except MySQLdb.IntegrityError:
                print("failed to insert data")
            finally:
                cursor.close()
                    
                    


                
        else:
            print("card swiped is invalid")
            break
            # time.sleep(5)

    # todo: create two tables one being the main table when an rfid card is scanned it retrieves the adm. no and
    #  goes ahead to fill in the attendance with the necessary information that is displayed on a web page in
    #  real time
    #
    # step 0: check if the member_id exists if not do nothing show invalid somewhere [think of it later]

    # step 1: according to the member_id retrieve the student_id
    # step 2: check if contents to be inserted already exist in the new table
    # step 3: insert values of student_id, attendance_status, current_dater,current_timer
    # step 4: display values in the db in a web page for interpreting the data then generate automatically after 3 hours
    # step 5: restrict the program from reposting same data to with same UID to the db

