import MySQLdb


def check_atleast_if_2_attendees():
    # To connect MySQL database
    conn = MySQLdb.connect(
        'localhost',
        'root',
        "",
        'attendance',
    )
    
    mycursor = conn.cursor()
    test2 = "select COUNT(*) from attendance"
    mycursor.execute(test2)

    var = mycursor.fetchone()
    print("Students in attendance are {}".format(var[0]))
    if var[0] < 2:
        print("Minimum Threshold not Reached to Count as a Lecture")
        return False
    elif (var[0] > 2):
        print("Class attendance is OKay ")
        return True

    else:
        print("There was an error maybe check that db server is still running")
        return False



    # To close the connection
    conn.close()


# Driver Code
if __name__ == "__main__":
    print(check_atleast_if_2_attendees())

