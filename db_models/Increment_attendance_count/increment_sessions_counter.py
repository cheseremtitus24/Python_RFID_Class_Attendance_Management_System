import MySQLdb
import time

'''
def cdn_parser_enclose(url): 
    """Say hello to a person.
    Args:
        name: the url of the webpage as string
    Returns:
        A number.
"""
print(greeting[language]+" "+name)
return 4
'''
# todo: update the unit_attendance %age by querying the units.sessions_counter table and compute the percentage that is saved as a string


# todo: query the current status of each student in the attendance.attendance table then save to a variable
# todo: query the attendance.student table where student_id and update the attendance_count by adding the  attendance.attendance.attendance_status +
# attendance.students.attendance_count

user = 'root'  # your username
passwd = ''  # your password
host = 'localhost'  # your host
db = 'attendance'  # database where your table is stored
table = 'unit_sessions'  # table you want to save

con = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db)
cursor = con.cursor()

# We will need to select for each and every student and for this we will go about it as follows
'''
step 1: select the contents of all student_id and attendance_status save them to a list
step 2: remove the students who are absent and append to a list the student ids of those who are present
step 3:::: 
'''

query = "SELECT unit_id FROM %s;" % table
cursor.execute(query)
results = cursor.fetchone()
this_unit = results[0]
cursor.close()


# increment the attendance counter by 1 for each and every student that attended the class

# todo: use a map function to update the student attendance count

def update_attendance_counter(unit_id):
    user = 'root'  # your username
    passwd = ''  # your password
    host = 'localhost'  # your host
    db = 'attendance'  # database where your table is stored
    table = 'units'  # table you want to save

    conn = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db)
    cursor1 = conn.cursor()

    # query the units table to get the previous value count of the previous unit attendance
    print("Attempting to update the Students sessions Counter for this Session")

    query1 = (
            """SELECT sessions_counter from  units where unit_id like %s """ % unit_id)
    cursor1.execute(query1)
    result1 = cursor1.fetchone()
    print(result1)
    if result1:
        previous = int(result1[0])
        print("Previous Sessions Counter attendance is %s" % previous)

        current = previous + 1

        con = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db)
        cursor = con.cursor()

        query = "UPDATE `attendance`.`units` SET `sessions_counter` = {update} WHERE unit_id like '{unit_id}';".format(
            update=current, unit_id=unit_id)
        status = cursor.execute(query)
        if status:
            print("Sessions Attendance has been update from {previous} to {update}".format(previous=previous,update=current))
        else:
            print("The update possibly failed")
        conn2 = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db)
        cursor2 = conn2.cursor()

        query2 = (
                "SELECT sessions_counter from  units where unit_id like %s " % unit_id)
        cursor2.execute(query2)
        result2 = cursor2.fetchone()
        print(result2)

        updated = int(result2[0])
        print("Updated attendance reads %s" % updated)
    else:
        print("student id does not exist in the target students. table")

# update_attendance_counter(str(this_unit))
# map(update_attendance_counter,present_students)

# This entire file should be a function that updAtes the attendance_count and returns the ids that have
# successfully been updated

# We need a function that will serve to notify the user on the incumbent update
# Failed table updates should also be reflected
