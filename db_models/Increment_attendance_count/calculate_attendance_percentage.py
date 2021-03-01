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
table = 'attendance'  # table you want to save

con = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db)
cursor = con.cursor()

# We will need to select for each and every student and for this we will go about it as follows

query = "SELECT student_id, attendance_status, unit_id FROM %s;" % table
cursor.execute(query)
results = cursor.fetchall()
present_students = list()
unit_id = None
for result in results:
    if result[2] == True:
        present_students.append(result[0])
        unit_id = result[1]
# print("The students who are in attendance are %s" % present_students)
cursor.close()


# increment the attendance counter by 1 for each and every student that attended the class

# todo: use a map function to update the student attendance count

def update_attendance_percentage(student_id, unit_id):
    user = 'root'  # your username
    passwd = ''  # your password
    host = 'localhost'  # your host
    db = 'attendance'  # database where your table is stored
    table = 'student_class_attendance'  # table you want to save

    conn = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db)
    cursor1 = conn.cursor()

    # query the student_class_attendance to get the previous value count of the previous unit attendance for the particular student
    # todo : select the total number of unit_sessions reported to then save as a denominator value from the units.sessions_counter and match the unit_id

    # query1 = ")",unit_id
    cursor1.execute(f"SELECT sessions_counter from  units where  unit_id like {unit_id}")
    result1 = cursor1.fetchone()
    denominator = result1[0]
    print(f"The sessions attended for unit_{unit_id} are {denominator}")
    if result1:
        conn5 = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db)
        cursor5 = conn5.cursor()
        # query5 = "SELECT unit_{unit_id}_percentage_attendance from  student_class_attendance where stud_id like {student_id} and unit_{unit_id} like '{unit_id}'"

        #get the unit attendance count for each student in the present_students list

        cursor5.execute(f"select unit_{unit_id}_attendance_count from student_class_attendance where stud_id like '{student_id}'")
        result5 = cursor5.fetchone()
        previous = result5[0]
        print(f"current attendance count for {student_id} reads {previous}")

        numerator = previous
        # print(denominator)
        # print(numerator)
        # percentage = 40
        try:
            percentage = numerator / denominator * 100
            con3 = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db)
            cursor3 = con3.cursor()

            query = f"UPDATE `student_class_attendance` SET `unit_{unit_id}_percentage_attendance`={percentage} WHERE stud_id='{student_id}'"
            cursor3.execute(query)

        except:
            pass



    else:
        print("student id does not exist in the target students. table")




# update_attendance_percentage('J17-5562-2015', '1')
