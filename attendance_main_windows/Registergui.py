import MySQLdb
import serial
from MySQLdb.cursors import Cursor
from serial.tools import list_ports
import time

def read_in_rfid_values():

    #connection to the attendance database
    try:
        dbConn = MySQLdb.connect("localhost", "root", "", "attendance")
    except:
        print("Start the database server first")
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
    global data

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
        try:
            cursor: Cursor = dbConn.cursor()
            status = cursor.execute(

            cursor.execute( """INSERT INTO attendance (student_id )VALUES (%s)""")
          #  dbConn.commit()
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









if __name__ == '__main__':
    read_in_rfid_values()

