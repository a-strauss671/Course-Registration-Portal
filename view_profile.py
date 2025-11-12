import tkinter
from tkinter import *
from shared_functionality import *
#------------------------------------------MACROS-----------------------------------------------------------------------
FIRST_NAME_COLUMN_NUM = 0
LAST_NAME_COLUMN_NUM = 1
USERNAME_COLUMN_NUM = 2
PASSWORD_COLUMN_NUM = 3
DEPARTMENT_COLUMN_NUM = 4
EMAIL_COLUMN_NUM =5
PHONE_NUMBER_COLUMN_NUM = 6
BIRTHDAY_COLUMN_NUM = 7
USER_TYPE_COLUMN_NUM = 8
EDITABLE_USER_DETAIL_COLUMN_NAMES = ["password", "department", "email", "phone_number"]

def open_view_profile(logged_in_username):
#------------------------------------------------FUNCTIONS--------------------------------------------------------------
    def format_profile_details(column_name, user_data, position, editable):
        global password_text_box, department_text_box, email_text_box, phone_number_text_box
        column_label = tkinter.Label(root, text=column_name)
        column_label.place(x=position[0], y=position[1])
        if editable:
            match column_name:
                case "password":
                    password_text_box = tkinter.Entry(root)
                    password_text_box.insert(END, user_data)
                    password_text_box.place(x=(position[0] + 100), y=position[1])
                case "department":
                    department_text_box = tkinter.Entry(root)
                    department_text_box.insert(END, user_data)
                    department_text_box.place(x=(position[0] + 100), y=position[1])
                case "email":
                    email_text_box = tkinter.Entry(root)
                    email_text_box.insert(END, user_data)
                    email_text_box.place(x=(position[0] + 100), y=position[1])
                case "phone_number":
                    phone_number_text_box = tkinter.Entry(root)
                    phone_number_text_box.insert(END, user_data)
                    phone_number_text_box.place(x=(position[0] + 100), y=position[1])

        else:
            original_user_data = tkinter.Label(root, text=user_data)
            original_user_data.place(x= (position[0] + 100), y=position[1])

    def get_new_user_details(original_user_details):
        new_user_details = {"password": password_text_box.get(),
                            "department": department_text_box.get(),
                            "email": email_text_box.get(),
                            "phone_number": phone_number_text_box.get()}
        original_user_details.update(new_user_details)
        return original_user_details

    # ------------------------------------------STATIC PAGE SETUP-------------------------------------------------------
    root = tkinter.Tk()
    root.geometry("700x700")
    root.title("Course Management System")
    root.configure(bg="#C1E1C1")

    db_connection = connect_to_db()
    my_cursor = db_connection.cursor()
    query = str("SELECT * FROM logins WHERE Username = '" + str(logged_in_username) + "'")
    my_cursor.execute(query)
    user_details = my_cursor.fetchall()[0]
    original_user_details = {"first_name": user_details[FIRST_NAME_COLUMN_NUM],
                               "last_name": user_details[LAST_NAME_COLUMN_NUM],
                               "username": user_details[USERNAME_COLUMN_NUM],
                               "password": user_details[PASSWORD_COLUMN_NUM],
                               "department": user_details[DEPARTMENT_COLUMN_NUM],
                               "email": user_details[EMAIL_COLUMN_NUM],
                               "phone_number": user_details[PHONE_NUMBER_COLUMN_NUM],
                              "birthday": user_details[BIRTHDAY_COLUMN_NUM],
                               }
    x_coordinate = 100
    y_coordinate = 100
    for column_name, user_data in original_user_details.items():
        if column_name not in EDITABLE_USER_DETAIL_COLUMN_NAMES:
            editable = False
        else:
            editable = True
        position = (x_coordinate, y_coordinate)
        format_profile_details(column_name, user_data, position, editable)
        y_coordinate += 50


    def save_changes():
        new_user_details = get_new_user_details(original_user_details)
        my_cursor = db_connection.cursor()
        for column_name in EDITABLE_USER_DETAIL_COLUMN_NAMES:
            query = str("UPDATE logins SET %s ='" + str(new_user_details[column_name]) + "' WHERE username = '" + str(new_user_details["username"]) + "'") % column_name
            my_cursor.execute(query)
        messagebox.showinfo(message="Information successfully updated!")

    def go_back_home():
        root.destroy()
        from student_page import open_student_page
        open_student_page(logged_in_username)

    page_title = tkinter.Label(root, text="EDIT STUDENT PROFILE", font=("Georgia", 20))
    page_title.pack()

    save_changes_button = tkinter.Button(root, text="Save changes", command=save_changes)
    save_changes_button.place(x=100, y=500)

    home_button = tkinter.Button(root, text="Home", command=go_back_home)
    home_button.place(x=200, y=500)

    root.mainloop()