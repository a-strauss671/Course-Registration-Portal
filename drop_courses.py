import tkinter
from tkinter import ttk
from shared_functionality import *

#-------------------------------------------------MACROS----------------------------------------------------------------
COURSE_CODE_COLUMN_NUM = 6

def open_drop_courses(logged_in_username):
    #------------------------------------------PAGE SETUP---------------------------------------------------------------
    root = tkinter.Tk()
    root.geometry("700x700")
    root.title("Course Management System")
    root.configure(bg="#C1E1C1")

    page_number_label = tkinter.Label(root, text="DROP COURSES", font=("Georgia", 20))
    page_number_label.pack()
    #------------------------------------------------FUNCTIONS----------------------------------------------------------
    def drop_course():
        selected_course_code = course_text.get()
        if not selected_course_code:
            show_error("missing field")
        else:
            db_connection = connect_to_db()
            my_cursor = db_connection.cursor()

            placeholders = ', '.join(['%s'] * 2)
            columns = "username, dropped_course_code"

            query = "INSERT into student_dropped_courses ( %s ) VALUES ( %s ) " % (columns, placeholders)
            dropped_course_row = [logged_in_username, selected_course_code]
            my_cursor.execute(query, dropped_course_row)
            db_connection.commit()
            messagebox.showinfo(message="Course dropped!")


    def back_to_home():
        root.destroy()
        from student_page import open_student_page
        open_student_page(logged_in_username)


    def get_enrolled_courses():
        return get_student_enrolled_course_codes(logged_in_username)
    #------------------------------------------RESPONSIVE ELEMENTS SETUP----------------------------------------------------
    drop_course_label = tkinter.Label(root, text='Select course', bg='#C1E1C1', font=('Georgia', 14))
    drop_course_label.place(x=100, y=190)

    course_text = ttk.Combobox(root, values=get_enrolled_courses())
    course_text.place(x=100, y=220)

    drop_course = tkinter.Button(root, text='Drop Course', command=drop_course, font=('Georgia', 14))
    drop_course.place(x=100, y=300)

    back_to_home = tkinter.Button(root, text="Back to Home Page", command=back_to_home, font=('Georgia', 14))
    back_to_home.place(x=210, y=300)


    root.mainloop()