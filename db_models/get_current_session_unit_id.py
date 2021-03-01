import MySQLdb


def get_session_unit_id():
    db_conn = MySQLdb.connect("localhost", "root", "", "attendance")
    # open a cursor to the database
    cursor = db_conn.cursor()
    # finding and connecting to a comport automatically

    mycursor = db_conn.cursor()
    # test2 = f"select case when exists ( select * from [accounts] where 'account_number' = {account_number}) then cast (1 as bit) else cast (0 as BIT) end"
    test1 = "select unit_id from unit_sessions "
    # print(f"Received member id from the read in is {account_number}")
    mycursor.execute(test1)
    var = mycursor.fetchone()
    # print(var)
    if var[0]:
        # print(f"The student_id retrieved successfuly as {var}!")
        return var[0]

    else:
        # print("Student_id retrieval failed ")
        # print(var[0])
        return None
    con_obj.close()

# print(r