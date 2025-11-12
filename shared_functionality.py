from tkinter import messagebox
import mysql.connector
import mysql_credentials

def show_error(type_of_error):
    match type_of_error:
        case "missing field":
            error_msg = "Missing field(s)."
        case "invalid username or password":
            error_msg = "The login credentials you have entered are incorrect. Please try again."
        case "already registered course":
            error_msg = "You are already registered for this course."
        case "empty schedule":
            error_msg = "You're not registered for any courses."
        case "terms agreement":
            error_msg = "You must agree with the terms and conditions to register."
        case "username":
            error_msg = ("Usernames for students must start with STU, usernames for faculty must "
                       "start with FAC and usernames for administrators must start with ADM")
        case "phone number format":
            error_msg = "Please enter your phone number in format ###-###-####"
        case "birthday format":
            error_msg = "Please format birthday MM/DD/YYYY"
        case _:
            error_msg = "Unknown error. Contact system administrator."
    messagebox.showerror(message=error_msg)


def connect_to_db():
     return mysql.connector.connect(host=mysql_credentials.host, port=mysql_credentials.port,
                                   user=mysql_credentials.user, password=mysql_credentials.password,
                                   database='course_management_system')

def subtract_dropped_courses(username, all_added_course_codes, db_connection):
    my_cursor = db_connection.cursor()
    query = str("SELECT dropped_course_code FROM student_dropped_courses WHERE Username = '" + str(username) + "'")
    my_cursor.execute(query)
    dropped_courses_entries = my_cursor.fetchall()
    for course_code_tuple in dropped_courses_entries:
        for course_code in course_code_tuple:
            if course_code in all_added_course_codes:
                all_added_course_codes.remove(course_code)
    return all_added_course_codes

def get_added_course_codes(username, db_connection):
    all_added_course_codes = []
    my_cursor = db_connection.cursor()
    query = str("SELECT added_course_code FROM student_added_courses WHERE Username = '" + str(username) + "'")
    my_cursor.execute(query)
    added_courses_entries = my_cursor.fetchall()
    # print(added_courses_entries)
    for course_code_tuple in added_courses_entries:
        for course_code in course_code_tuple:
            all_added_course_codes.append(course_code)
    # print(all_added_course_codes)
    return all_added_course_codes

def get_full_course_info(enrolled_course_codes, db_connection):
    full_course_details = []
    my_cursor = db_connection.cursor()
    for course_code in enrolled_course_codes:
        query = str("SELECT * FROM course_catalog WHERE code  = '" + str(course_code) + "'")
        my_cursor.execute(query)
        course_details = my_cursor.fetchall()[0]
        full_course_details.append(course_details)
    return full_course_details

def get_student_enrolled_course_codes(username):
    db_connection = connect_to_db()
    # all the courses the student has ever added (regardless of if they have been dropped or not)
    all_added_course_codes = get_added_course_codes(username, db_connection)
    return subtract_dropped_courses(username, all_added_course_codes, db_connection)

def get_student_schedule(username):
    db_connection = connect_to_db()
    scheduled_course_codes = get_student_enrolled_course_codes(username)
    return get_full_course_info(scheduled_course_codes, db_connection)
