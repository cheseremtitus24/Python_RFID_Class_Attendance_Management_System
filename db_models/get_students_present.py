import MySQLdb
def get_present_students():

    user = 'root' # your username
    passwd = '' # your password
    host = 'localhost' # your host
    db = 'attendance' # database where your table is stored
    table = 'attendance' # table you want to save

    con = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db)
    cursor = con.cursor()

    # We will need to select for each and every student and for this we will go about it as follows
    '''
    step 1: select the contents of all student_id and attendance_status save them to a list
    step 2: remove the students who are absent and append to a list the student ids of those who are present
    step 3:::: 
    '''

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
    return present_students
# get_present_students()