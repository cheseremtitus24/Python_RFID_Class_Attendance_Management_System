import MySQLdb
import serial
from MySQLdb.cursors import Cursor
from serial.tools import list_ports
import time

from db_models import init_student_id_attendance_table, check_mem_id_exist as mem_check


def read_in_rfid_values():
    # connection to the attendance database
    try:
        dbConn = MySQLdb.connect("localhost", "root", "", "attendance")
    except:
        print("Start the database server init")
        quit()
    # finding and connecting to a comport automatically

    try:

        cdc = next(list_ports.grep("CH340"))
        print("Device was found ")
        # below line returns the comport number to connect to e.g [com5]
        device = cdc.device  # this will have to be changed to the serial port you are using
        print("Trying...", device)
        # PN532 card provides readable output when it operates at a baudrate of 115200

        arduino = serial.Serial(device, baudrate=115200, timeout=1)
    except:
        print("No device Found, Please Connect an RFID Device")
        quit()
    global data, unit_id

    # Main Program loop for reading the serial output
    while True:
        global restart
        restart = False
        # This variable is used to reset the value read in through rfid serial output

        if restart:
            data = None

        # Serially read data is stored to the local variable data
        data = arduino.readline().decode('ascii')
        print(data)
        # print(len(data.split()))

        if len(data.split()) > 0:
            # print("length above zero importing memcheck ")

            time.sleep(1)

            val = mem_check.check_mem_id_exist(data.split())

            if val:
                print(f"Success read in , ready to continue")
                # the read in id exists in the database now time to fill in the attendance form
                # step1: get the student_id

                # get unit id
                # connection to the attendance database
                try:
                    dbConnect = MySQLdb.connect("localhost", "root", "", "attendance")
                    db_cursor = dbConnect.cursor()
                    query = "SELECT unit_id from unit_sessions"
                    db_cursor.execute(query)
                    resultt = db_cursor.fetchone()
                    unit_id = int(resultt[0])
                    print(f"Retrieved Unit_id from the sessions table is {unit_id}")
                except:
                    print("Failed to read unit_id from unit_sessions table becoz you need first start the timer")
                    quit()
                # finding and connecting to a comport automatically

                from db_models import get_std_id as gsid

                stud_id = gsid.return_uid(data.split())

                # checking whether user is in the student_class_attendance if not add his entry to this table
                status = init_student_id_attendance_table.check_student_id_exist(stud_id)
                if not (status):
                    # the student_id entry is missing from the student_class_attendance tbl thefore lets create that entry
                    dbConnect = MySQLdb.connect("localhost", "root", "", "attendance")
                    db_cursor = dbConnect.cursor()
                    query = "INSERT into student_class_attendance(stud_id) VALUES ('%s')" % stud_id
                    db_cursor.execute(query)
                    # db_cursor.commit()
                    print(f"successfully inserted {stud_id} in the student_class_attendance table please check")

                # step2: change the attendance status to 1
                # step3: get current date
                from time_helper import time_help as th

                curr_date = th.get_current_date()
                curr_time = th.get_current_time()
                # pieces = data.split(" ")
                # print(pieces)
                try:
                    dbobject = MySQLdb.connect("localhost", "root", "", "attendance")
                    cursorss = dbobject.cursor()
                    # time.sleep(2)
                    # check if same student_id already exists if so skip this [continue]

                    exists = mem_check.check_student_id_exist(stud_id.split())
                    print(f"Does {stud_id} exist in the attendance table {exists}")
                    # time.sleep(2)
                    # if it does not exist continue prog execution printing something first
                    if exists:
                        print("The Student is already in Attending!!!!!!!! Skip ahead")
                        restart = True
                        continue
                        # continue
                    else:
                        # todo: query a temporary db such as the attendance one for holding the unit that is being taught
                        status_update = 1

                        qqquery = f"INSERT INTO `attendance` (`ID`, `student_id`, `attendance_status`, `unit_id`, `current_dater`, `current_timer`) VALUES (NULL, '{stud_id}', '{status_update}', '{unit_id}', '{curr_date}', '{curr_time}')"
                        # qquery = """INSERT INTO attendance (student_id,attendance_status,unit_id ,current_dater,
                        # current_timer) VALUES (%s,%s,%s,%s)""",(stud_id, str(status_update),str(unit_id), curr_date, curr_time)
                        status = cursorss.execute(qqquery)
                        time.sleep(1)
                        dbConn.commit()
                        # in the unit_id extract the final int at end of the string
                        # time.sleep(1)

                        # todo:update the student_class_attendance unit_1 with value read in from the attendance table and then use
                        '''
                        extract integer number at end of the unit
                        '''
                        dbConnect1 = MySQLdb.connect("localhost", "root", "", "attendance")
                        db_cursor1 = dbConnect1.cursor()
                        query1 = f"UPDATE `student_class_attendance` SET `unit_{unit_id}` = '{unit_id}' WHERE `student_class_attendance`.`stud_id` like '{stud_id}'"
                        # query1 = (
                        #     """INSERT INTO student_class_attendance (unit_%s) VALUES (%s) WHERE stud_id like '%s'""",
                        #     (unit_id, unit_id, stud_id))
                        check = db_cursor1.execute(query1)
                        dbConnect1.commit()
                        # if check:
                        #     print("Successfully inserted unit_. into the student class attendance")
                        # else:
                        #     print("update  into the student class attendance for a particular student failed")
                        # db_cursor1.commit()

                        if status:
                            print("data insertin success")
                            restart = True
                            continue

                        cursorss.close()
                except MySQLdb.IntegrityError:
                    print("failed to insert data")
                finally:
                    cursorss.close()





            else:
                print("card swiped is invalid/Expired")
                # break
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


if __name__ == '__main__':
    read_in_rfid_values()
