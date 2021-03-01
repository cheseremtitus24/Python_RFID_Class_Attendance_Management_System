




# for every selection it should overwrite the already existing value
# once the timer is started the field should be converted into being un-editable

import MySQLdb
import time

# todo: implement the use of resource managers

def list_of_units():
    user = 'root'  # your username
    passwd = ''  # your password
    host = 'localhost'  # your host
    db = 'attendance'  # database where your table is stored
    table = 'units'  # table you want to save


    try:
        con = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db)
        cursor = con.cursor()
        # retrieve content from the units.unit_code and save them to a list

        query = "SELECT unit_code FROM %s;" % table
        cursor.execute(query)
        results = cursor.fetchall()
        unit_codes = list()
        for result in results:
            unit_codes.append(result[0])
        print("Retrieved unit_codes from the units table are %s" % unit_codes)
        cursor.close()
        return unit_codes
    except:
        print("Please ensure that the database server is running..")
        quit()




# compare that the content in the unit_codes list matches one of the input strings from the option_menu's input and if so it should # retrieve the
# corresponding unit_id that will be used to set the unit_sessions.unit_id value
def capture_unit_id(unit_code):
    user = 'root'  # your username
    passwd = ''  # your password
    host = 'localhost'  # your host
    db = 'attendance'  # database where your table is stored
    table = 'units'  # table you want to save

    con = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db)
    cursor = con.cursor()

    # retrieve content from the units.unit_code and save them to a list
    units_code = str(unit_code.strip())

    query = "SELECT unit_id FROM units where unit_code like '%s' ;" % units_code
    cursor.execute(query)
    results = cursor.fetchone()
    unit_id = list()
    for result in results:
        unit_id.append(result)
    print("Retrieved unit_id is %s" % unit_id)
    cursor.close()
    return unit_id



def update_unit_sessions_table(unit_id):
    user = 'root'  # your username
    passwd = ''  # your password
    host = 'localhost'  # your host
    db = 'attendance'  # database where your table is stored
    table = 'units'  # table you want to save

    con = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db)
    global cursor
    cursor = con.cursor()

    # retrieve content from the units.unit_code and save them to a list
    units_code = unit_id[0]
    # todo: first check if the current post value already exists
    '''
    if entry_exists:
        do nothing
    else:
        truncate table
        add the new entry value
        then return a value to show success
    '''

    check_unit_id_exist = f"select unit_id from units where unit_id like {units_code}"

    cursor.execute(check_unit_id_exist)

    var = cursor.fetchone()
    # todo: check on this and ensure that it uses select case when exists.
    print("the value of var that is to be checked is ")
    print(var)
    if var[0]:
        print("populating the unit_sessions table with the input unit_id")
        query1 = "TRUNCATE TABLE unit_sessions"
        query2 = "INSERT INTO unit_sessions(unit_id) values('%s')"%units_code
        queries = [query1,query2]
        cursor.execute(query1)
        cursor.execute(query2)
        # cursor.commit()
        return True

    else:
        # print("Account  Exists doing nothing ")
        return False

    cursor.close()