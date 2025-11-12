import tkinter
import mysql_credentials
#------------------------------------------PAGE SETUP-------------------------------------------------------------------
root = tkinter.Tk()
root.geometry("700x700")
root.title("Course Management System")
root.configure(bg="#C1E1C1")

#------------------------------------------------FUNCTIONS--------------------------------------------------------------
def close():
    root.destroy()

def get_courses_from_db():
    import mysql.connector
    mydb = mysql.connector.connect(host=mysql_credentials.host, port=mysql_credentials.port,
                                   user=mysql_credentials.user, password=mysql_credentials.password,
                                   database='course_management_system')
    mycursor = mydb.cursor()
    query = str("SELECT * FROM course_catalog")
    mycursor.execute(query)
    return mycursor.fetchall()

def format_courses(courses_table):
    course_name_x_coord = 70
    course_code_x_coord = 350
    days_x_coord = 450
    times_x_coord = 540
    professor_x_coord = 750
    description_x_coord = 900
    y_coord = 100
    for course_details in courses_table:
        y_coord += 50
        course_name = tkinter.Label(root, text=course_details[0], bg="#C1E1C1")
        days = tkinter.Label(root, text=course_details[1], bg="#C1E1C1")
        times = tkinter.Label(root, text=f"{course_details[2]} to {course_details[3]}", bg="#C1E1C1")
        professor = tkinter.Label(root, text=course_details[5], bg="#C1E1C1")
        description = tkinter.Label(root, text=course_details[4], bg="#C1E1C1")
        course_code = tkinter.Label(root, text=course_details[6], bg="#C1E1C1")
        course_name.place(x=course_name_x_coord, y=y_coord)
        course_code.place(x=course_code_x_coord, y=y_coord)
        days.place(x=days_x_coord, y=y_coord)
        times.place(x=times_x_coord, y=y_coord)
        professor.place(x=professor_x_coord, y=y_coord)
        description.place(x=description_x_coord, y=y_coord)

    close_button = tkinter.Button(root, text='Close', command=close)
    close_button.place(x=70, y=(y_coord+ 50))
    root.mainloop()

#------------------------------------------RESPONSIVE ELEMENTS SETUP----------------------------------------------------
page_title = tkinter.Label(root, text="VIEW COURSE CATALOG", font=("Georgia", 20))
page_title.pack()

course_name_label = tkinter.Label(root, text='COURSE NAME', font=("Georgia", 14))
course_name_label.place(x=70, y=100)

course_code_label = tkinter.Label(root, text='CODE', font=("Georgia", 14))
course_code_label.place(x=350, y=100)

course_days_label = tkinter.Label(root, text='DAYS', font=("Georgia", 14))
course_days_label.place(x=450, y=100)

course_time_label = tkinter.Label(root, text='TIMES', font=("Georgia", 14))
course_time_label.place(x=540, y=100)

professor_label = tkinter.Label(root, text='PROFESSOR', font=("Georgia", 14))
professor_label.place(x=750, y=100)

course_description_label = tkinter.Label(root, text='DESCRIPTION', font=("Georgia", 14))
course_description_label.place(x=900, y=100)

courses_table = get_courses_from_db()
format_courses(courses_table)

