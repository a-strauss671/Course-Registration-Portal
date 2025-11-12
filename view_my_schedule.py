import tkinter
from shared_functionality import *
#------------------------------------------MACROS-----------------------------------------------------------------------
FACULTY_USER_TYPE = "FAC"
STUDENT_USER_TYPE = "STU"
COURSE_NAME_COLUMN_NUM = 0
COURSE_DAYS_COLUMN_NUM = 1
COURSE_START_TIME_COLUMN_NUM = 2
COURSE_END_TIME_COLUMN_NUM = 3
COURSE_DESC_COLUMN_NUM = 4
COURSE_PROFESSOR_COLUMN_NUM = 5
COURSE_CODE_COLUMN_NUM = 6

def open_view_my_schedule(logged_in_username, user_type):
    #------------------------------------------PAGE SETUP---------------------------------------------------------------
    root = tkinter.Tk()
    root.geometry("700x700")
    root.title("Course Management System")
    root.configure(bg="#C1E1C1")

    page_number_label = tkinter.Label(root, text="VIEW MY SCHEDULE", font=("Georgia", 20))
    page_number_label.pack()

    #------------------------------------------------FUNCTIONS----------------------------------------------------------
    def get_professor_title(db_connection, logged_in_username):
        my_cursor = db_connection.cursor()
        query = str("SELECT last_name FROM logins WHERE username = '" + str(logged_in_username) + "'")
        my_cursor.execute(query)
        professor_surname = my_cursor.fetchall()[0][0]
        return "Dr. " + professor_surname

    def get_courses_taught(professor_title, db_connection):
        my_cursor = db_connection.cursor()
        query = str("SELECT * FROM course_catalog WHERE Professor = '" + str(professor_title) + "'")
        my_cursor.execute(query)
        courses_taught = my_cursor.fetchall()
        return courses_taught

    def format_schedule(schedule):
        course_name_x_coord = 70
        course_code_x_coord = 350
        days_x_coord = 450
        times_x_coord = 540
        professor_x_coord = 750
        description_x_coord = 900
        y_coord = 200
        for course in schedule:
            y_coord += 50
            course_name = tkinter.Label(root, text=course[COURSE_NAME_COLUMN_NUM], bg="#C1E1C1")
            days = tkinter.Label(root, text=course[COURSE_DAYS_COLUMN_NUM], bg="#C1E1C1")
            times = tkinter.Label(root, text=f"{course[COURSE_START_TIME_COLUMN_NUM]} to {course[COURSE_END_TIME_COLUMN_NUM]}", bg="#C1E1C1")
            professor = tkinter.Label(root, text=course[COURSE_PROFESSOR_COLUMN_NUM], bg="#C1E1C1")
            description = tkinter.Label(root, text=course[COURSE_DESC_COLUMN_NUM], bg="#C1E1C1")
            course_code = tkinter.Label(root, text=course[COURSE_CODE_COLUMN_NUM], bg="#C1E1C1")
            course_name.place(x=course_name_x_coord, y=y_coord)
            course_code.place(x=course_code_x_coord, y=y_coord)
            days.place(x=days_x_coord, y=y_coord)
            times.place(x=times_x_coord, y=y_coord)
            professor.place(x=professor_x_coord, y=y_coord)
            description.place(x=description_x_coord, y=y_coord)


    def go_back_home():
        root.destroy()
        if user_type == FACULTY_USER_TYPE:
            from professor_page import open_professor_page
            open_professor_page(logged_in_username)
        elif user_type == STUDENT_USER_TYPE:
            from student_page import open_student_page
            open_student_page(logged_in_username)
        else:
            show_error("Restricted access")

    def close():
        root.destroy()

    db_connection = connect_to_db()
    if user_type == FACULTY_USER_TYPE:
        professor_title = get_professor_title(db_connection, logged_in_username)
        schedule = get_courses_taught(professor_title, db_connection)
        if not schedule:
            show_error("empty schedule")
        else:
            format_schedule(schedule)

    elif user_type == STUDENT_USER_TYPE:
        schedule = get_student_schedule(logged_in_username)
        if not schedule:
            show_error("empty schedule")
        else:
            format_schedule(schedule)

    else:
        show_error("restricted access")
    #------------------------------------------RESPONSIVE ELEMENTS SETUP----------------------------------------------------
    course_name_label = tkinter.Label(root, text='COURSE NAME', font=("Georgia", 14))
    course_name_label.place(x=70, y=200)

    course_code_label = tkinter.Label(root, text='CODE', font=("Georgia", 14))
    course_code_label.place(x=350, y=200)

    course_days_label = tkinter.Label(root, text='DAYS', font=("Georgia", 14))
    course_days_label.place(x=450, y=200)

    course_time_label = tkinter.Label(root, text='TIMES', font=("Georgia", 14))
    course_time_label.place(x=540, y=200)

    professor_label = tkinter.Label(root, text='PROFESSOR', font=("Georgia", 14))
    professor_label.place(x=750, y=200)

    course_description_label = tkinter.Label(root, text='DESCRIPTION', font=("Georgia", 14))
    course_description_label.place(x=900, y=200)

    close_button = tkinter.Button(root, text='Close', command=close)
    close_button.place(x=70, y=600)

    go_back_home_button = tkinter.Button(root, text ="Home", command=go_back_home)
    go_back_home_button.place(x=150, y =600)

    root.mainloop()
