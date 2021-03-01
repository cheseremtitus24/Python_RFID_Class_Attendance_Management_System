import MySQLdb


def update_attendance_counter(student_id, unit_id):
    user = 'root'  # your username
    passwd = ''  # your password
    host = 'localhost'  # your host
    db = 'attendance'  # database where your table is stored
    table = 'attendance'  # table you want to save
    # todo: before incrementing the unit_1/2_attendance count we must check if an entry exists in the attendance table by using the where clause for the
    # student_id
    con = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db)
    cursor = con.cursor()

    # We will save all the student_ids which have the attendance flag as true and save them to a list object called present_students

    query = "SELECT student_id, attendance_status, unit_id FROM %s;" % table
    cursor.execute(query)
    results = cursor.fetchall()
    present_students = list()

    for result in results:
        if result[2] == True:
            present_students.append(result[0])
            unit_id = result[1]
    # print("The students who are in attendance are %s" % present_students)
    cursor.close()
    user = 'root'  # your username
    passwd = ''  # your password
    host = 'localhost'  # your host
    db = 'attendance'  # database where your table is stored
    table = 'student_class_attendance'

    conn = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db)
    cursor1 = conn.cursor()

    # TODO:

    # query the student_class_attendance to get the previous value count of the previous unit attendance for the particular student
    # print(type(student_id))
    queryy = f"SELECT `unit_{unit_id}_attendance_count` FROM `student_class_attendance` WHERE `stud_id` = '{student_id}'"
    cursor1.execute(queryy)
    result1 = cursor1.fetchone()
    print(result1)
    if result1:
        previous = int(result1[0])
        print("Previous Count attendance is %s" % previous)

        current = previous + 1

        con = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db)
        cursor = con.cursor()
        if student_id in present_students:
            query = f"UPDATE `attendance`.`student_class_attendance` SET `unit_{unit_id}_attendance_count` = {current} WHERE stud_id like '{student_id}'"
            cursor.execute(query)

            conn2 = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db)
            cursor2 = conn2.cursor()

            query2 = f"SELECT `unit_{unit_id}_attendance_count` FROM `student_class_attendance` WHERE `stud_id` = '{student_id}'"
            cursor2.execute(query2)
            result2 = cursor2.fetchone()
            updated = int(result2[0])
            print("Updated attendance reads %s" % updated)
    else:
        print("student id does not exist in the target students. table")


# update_attendance_counter("J17-0000-2014", '1')
