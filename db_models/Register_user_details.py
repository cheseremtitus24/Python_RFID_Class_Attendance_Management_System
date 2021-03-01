import MySQLdb

# todo: First scan the RFID once it is accepted enable the rest of the input fields for editing and saving of content
from db_models.check_mem_id_exist import check_mem_id_exist


def insert_data_to_db(student_id,surname,member_id,phone_number,email):
    # connection to the attendance database todo: First confirm whether the member_id exists and if so return a value
    #  that signifies an invalid card is swipe and suggest to user that they should try another card
    if not(check_mem_id_exist(member_id)):

        try:
            db_conn = MySQLdb.connect("localhost", "root", "", "attendance")
            # open a cursor to the database
            cursor = db_conn.cursor()
            # finding and connecting to a comport automatically

            mycursor = db_conn.cursor()
            # TODO: test2 = f"select case when exists ( select * from [accounts] where 'account_number' = {
            #  account_number}) then cast (1 as bit) else cast (0 as BIT) end"
            test1 = f"INSERT into students ( student_id, surname, member_id,phone_number,email) VALUES ('{student_id}','{surname}','{member_id}','{phone_number}','{email}') "
            mycursor.execute(test1)
        except:
            print("Start the database server first")
            quit()
        # finding and connecting to a comport automatically
        #status 0 shows that data was successfully inserted to the database
        return 1
    else:
        print("The RFID card is  Already in Use. Please try swiping a different card...")
        #status 1 shows there was an error and the user must be informed of the failure
        return 0
