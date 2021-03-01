import MySQLdb


def check_student_id_exist(stud_id):
    db_conn = MySQLdb.connect("localhost", "root", "", "attendance")
    # open a cursor to the database
    cursor = db_conn.cursor()
    # finding and connecting to a comport automatically

    mycursor = db_conn.cursor()

    #
    # Account_number = nfc_check_exist()
    # print("from within Status output = " + str(Account_number))

    # uid_check = f"SELECT CASE WHEN EXISTS(select  account_number from accounts where account_number = {Account_number} ) THEN CAST(1 as BIT) ELSE CAST(0 as BIT) END "
    #print(f"gotten memb id is {member_id[0]}")
    test2 = f"select stud_id from student_class_attendance where stud_id like '%s'" % stud_id

    mycursor.execute(test2)


    var = mycursor.fetchone()
    # print(var)
    print(f"The results from querying the student_class_attendance for {stud_id} are {var}")
    if var:
        print(f"Student id {stud_id} Exists in the student_class_attendance table!")
        return True



    else:
        print(f"Student id {stud_id} does not exists in the student_class_attendance table")
        return False

# print(check_student_id_exist('J17-5562-2015'))