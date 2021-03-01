def get_current_time():
    from datetime import datetime

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    # print("Current Time =", current_time)
    return current_time
def get_current_date():
    import datetime
    from datetime import datetime
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d')

    # Current_Date_Formatted = datetime.datetime.today().strftime('%d-%b-%Y')
    # print('Current Date: ' + str(Current_Date_Formatted))
    # return str(Current_Date_Formatted)
    return formatted_date
# print(get_current_date())