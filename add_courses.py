import tkinter
from tkinter import ttk
from shared_functionality import *

#-------------------------------------------------MACROS----------------------------------------------------------------
COURSE_CODE_COLUMN_NUM = 6

def open_add_courses(logged_in_username):
    #------------------------------------------PAGE SETUP---------------------------------------------------------------
    root = tkinter.Tk()
    root.geometry("700x700")
    root.title("Course Management System")
    root.configure(bg="#C1E1C1")

    page_number_label = tkinter.Label(root, text="ADD COURSES", font=("Georgia", 20))
    page_number_label.pack()
    #------------------------------------------------FUNCTIONS----------------------------------------------------------
    def add_course():
        already_registered_courses_list = get_student_enrolled_course_codes(logged_in_username)
        selected_course_code = course_text.get()
        db_connection = connect_to_db()
        my_cursor = db_connection.cursor()

        if selected_course_code in already_registered_courses_list:
            show_error("already registered course")

        else:
            placeholders = ', '.join(['%s'] * 2)
            columns = "username, added_course_code"

            query = "INSERT into student_added_courses ( %s ) VALUES ( %s ) " % (columns, placeholders)
            added_course_row = [logged_in_username, selected_course_code]
            my_cursor.execute(query, added_course_row)
            db_connection.commit()
            messagebox.showinfo(message="Course added!")


    def back_to_home():
        root.destroy()
        from student_page import open_student_page
        open_student_page(logged_in_username)

    def get_courses():
        db_connection = connect_to_db()
        my_cursor = db_connection.cursor()
        query = str("SELECT * FROM course_catalog")
        my_cursor.execute(query)
        courses = my_cursor.fetchall()
        course_code_list = []
        for course in courses:
            course_code_list.append(course[COURSE_CODE_COLUMN_NUM])
        return course_code_list

    #------------------------------------------RESPONSIVE ELEMENTS SETUP----------------------------------------------------
    add_course_label = tkinter.Label(root, text='Select course', bg='#C1E1C1', font=('Georgia', 14))
    add_course_label.place(x=100, y=190)

    course_text = ttk.Combobox(root, values=get_courses())
    course_text.place(x=100, y=220)

    add_course = tkinter.Button(root, text='Add Course', command=add_course, font=('Georgia', 14))
    add_course.place(x=100, y=300)

    back_to_home = tkinter.Button(root, text="Back to Home Page", command=back_to_home, font=('Georgia', 14))
    back_to_home.place(x=210, y=300)

    root.mainloop()