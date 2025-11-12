import tkinter
from tkinter import messagebox
from tkinter import ttk
import mysql_credentials
import mysql.connector

def open_upload_courses_page():
    #--------------------------------------STATIC PAGE SETUP----------------------------------------------------------------
    root = tkinter.Tk()
    root.geometry("700x700")
    root.title("Course Management System")
    root.configure(bg="#C1E1C1")

    page_title = tkinter.Label(root, text="UPLOAD COURSES", font=("Georgia", 20))
    page_title.pack()
    #--------------------------------------FUNCTIONS------------------------------------------------------------------------
    def get_professors():
        professors_list = []
        mydb = mysql.connector.connect(host=mysql_credentials.host, port=mysql_credentials.port,
                                       user=mysql_credentials.user, password=mysql_credentials.password,
                                       database='course_management_system')
        mycursor = mydb.cursor()
        query = str("SELECT last_name FROM logins WHERE user_type= '" + "FAC" + "'")
        mycursor.execute(query)
        for professor_surname, in mycursor:
            professors_list.append("Dr. " + professor_surname)
        return professors_list

    def show_error_message(type_of_error):
        match type_of_error:
            case "starting time before ending time":
                message = "The end time must be AFTER the start time."
            case "missing fields":
                message = "Missing field(s)"
            case _:
                message = "Unknown error. Contact system administrator."

        messagebox.showerror(title="Failed to Upload Course", message=message)

    def get_fields():
        course_details = {"name": course_name_text.get(),
                      "days": course_days_text.get(),
                      "start": starting_time_text.get(),
                      "end": end_time_text.get(),
                      "description": course_description_text.get(),
                      "professor": professor_dropdown.get(),
                      "code": course_code_text.get(),
        }
        return course_details

    def check_input(course_details):
        if starting_times.index(course_details["start"]) > ending_times.index(course_details["end"]):
            show_error_message("starting time before ending time")
            return False
        return True

    def create_new_course_in_db(course_details):
        import mysql.connector
        mydb = mysql.connector.connect(host=mysql_credentials.host, port=mysql_credentials.port,
                                       user=mysql_credentials.user, password=mysql_credentials.password,
                                       database='course_management_system')

        mycursor = mydb.cursor()
        placeholders = ', '.join(['%s'] * len(course_details))
        columns = ', '.join(course_details.keys())
        query = "INSERT into course_catalog ( %s ) VALUES ( %s ) " % (columns, placeholders)
        mycursor.execute(query, list(course_details.values()))

        mydb.commit()
        messagebox.showinfo(message='Course uploaded!')

    def upload_course():
        course_details = get_fields()
        for (attribute, value) in course_details.items():
            if not value:
                show_error_message("missing fields")
                break
        else:
            if check_input(course_details):
                print(tuple(course_details.values()))
                create_new_course_in_db(course_details)


    def view_catalogue():
        root.destroy()
        import view_catalogue

    #-------------------------------------- RESPONSIVE ELEMENTS SETUP-------------------------------------------------------
    course_name_label = tkinter.Label(root, text="Course name", font=("Georgia", 14))
    course_name_label.place(x=100, y=100)
    course_name_text = tkinter.Entry(root, width=30, bg='#fffdaf')
    course_name_text.place(x=200, y=100)

    course_code_label = tkinter.Label(root, text="Course code", font=("Georgia", 14))
    course_code_label.place(x=100, y=200)
    course_code_text = tkinter.Entry(root, width=30, bg='#fffdaf')
    course_code_text.place(x=200, y=200)

    course_days_label = tkinter.Label(root, text="Course days", font=("Georgia", 14))
    course_days_label.place(x=100, y=300)
    course_days_text = ttk.Combobox(root, values=['MWF', 'TTh'], width=5)
    course_days_text.place(x=200, y=300)

    course_time_label = tkinter.Label(root, text='Course time', font=("Georgia,", 14))
    course_time_label.place(x=100, y=400)

    starting_times = ['8:15 a.m.', '9:50 a.m.', '11:15 a.m.', '12:35 p.m.', '1:45 p.m.', '2:50 p.m.', '7:00 p.m.']
    starting_time_text = ttk.Combobox(root, values=starting_times, width=8)
    starting_time_text.place(x=210, y=400)

    to_label = tkinter.Label(root, text="to", bg="#C1E1C1")
    to_label.place(x=310, y=400)

    ending_times = ['9:50 a.m.', '11:15 a.m.', '12:35 p.m.', '1:45 p.m.', '2:50 p.m.', '4:00 p.m.', '10:00 p.m.']
    end_time_text = ttk.Combobox(root, values=ending_times, width=8)
    end_time_text.place(x=330, y=400)

    course_description_label = tkinter.Label(root, text='Course Description')
    course_description_label.place(x=100, y=500)

    course_description_text = tkinter.Entry(root, width=30, bg='#fffdaf')
    course_description_text.place(x=250, y=500)

    assign_professor_label = tkinter.Label(root, text='Assign professor')
    assign_professor_label.place(x=100, y=600)


    professor_list = get_professors()
    professor_dropdown = ttk.Combobox(root, values=professor_list, width=12)
    professor_dropdown.place(x=220, y=600)

    upload_course_button = tkinter.Button(root, text='Upload Course', command=upload_course)
    upload_course_button.place(x=100, y=700)

    cancel_button = tkinter.Button(root, text="Cancel")
    cancel_button.place(x=250, y=700)

    view_course_catalogue_button = tkinter.Button(root, text='View Course Catalog', command=view_catalogue)
    view_course_catalogue_button.place(x=100, y=800)
    root.mainloop()