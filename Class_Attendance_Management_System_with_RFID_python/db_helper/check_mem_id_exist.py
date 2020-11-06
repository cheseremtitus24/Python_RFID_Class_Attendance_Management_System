import MySQLdb


def check_mem_id_exist(member_id):
    db_conn = MySQLdb.connect("localhost", "root", "", "attendance")
    # open a cursor to the database
    cursor = db_conn.cursor()
    # finding and connecting to a comport automatically

    mycursor = db_conn.cursor()

    #
    # Account_number = nfc_check_exist()
    # print("from within Status output = " + str(Account_number))

    # uid_check = f"SELECT CASE WHEN EXISTS(select  account_number from accounts where account_number = {Account_number} ) THEN CAST(1 as BIT) ELSE CAST(0 as BIT) END "
    print(f"gotten memb id is {member_id[0]}")
    test2 = f"select member_id from students where member_id = '{member_id[0]}'"

    mycursor.execute(test2)


    var = mycursor.fetchone()
    # print(var)
    if var==None:
        print("Account Not Exists!")
        return False

    else:
        print("Account  Exists")
        return True
# check_mem_id_exist(2519180581)

def check_student_id_exist(member_id):
    db_conn = MySQLdb.connect("localhost", "root", "", "attendance")
    # open a cursor to the database
    cursor = db_conn.cursor()
    # finding and connecting to a comport automatically

    mycursor = db_conn.cursor()

    #
    # Account_number = nfc_check_exist()
    # print("from within Status output = " + str(Account_number))

    # uid_check = f"SELECT CASE WHEN EXISTS(select  account_number from accounts where account_number = {Account_number} ) THEN CAST(1 as BIT) ELSE CAST(0 as BIT) END "
    print(f"gotten memb id is {member_id[0]}")
    test2 = f"select student_id from attendance where student_id = '{member_id[0]}'"

    mycursor.execute(test2)


    var = mycursor.fetchone()
    # print(var)
    if var==None:
        print("Account Not Exists!")
        return False

    else:
        print("Account  Exists")
        return True