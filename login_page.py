import tkinter
from shared_functionality import show_error
from shared_functionality import connect_to_db
from professor_page import open_professor_page
from student_page import open_student_page
from administrator_page import open_administrator_page
#------------------------------------------MACROS-----------------------------------------------------------------------
PASSWORD_COLUMN_NUMBER = 3
USER_TYPE_COLUMN_NUMBER = 8
FACULTY_USER_TYPE = "FAC"
STUDENT_USER_TYPE = "STU"
#------------------------------------------STATIC PAGE SETUP------------------------------------------------------------
root = tkinter.Tk()
root.geometry("700x700")
root.title("Course Management System")
root.configure(bg="#C1E1C1")
#------------------------------------------------FUNCTIONS--------------------------------------------------------------
def get_fields():
    return {"username": username_text.get(), "password": password_text.get()}

def validate_username_and_password(my_db, user_entry):
    my_cursor = my_db.cursor()
    username = user_entry['username']
    password = user_entry['password']
    query = str("SELECT * FROM logins WHERE username = '" + str(username) + "'")
    my_cursor.execute(query)
    user_details = my_cursor.fetchall()

    if (not user_details) or (password != user_details[0][PASSWORD_COLUMN_NUMBER]):
        show_error("invalid username or password")
    elif password == user_details[0][PASSWORD_COLUMN_NUMBER]:
            return True

    return False

def get_user_type(db_connection, user_entry):
    my_cursor = db_connection.cursor()
    username = user_entry['username']
    query = str("SELECT * FROM logins WHERE username = '" + str(username) + "'")
    my_cursor.execute(query)
    user_info = my_cursor.fetchall()
    return user_info[0][USER_TYPE_COLUMN_NUMBER]

def click_login():
    user_entry = get_fields()
    if not(user_entry["username"] and user_entry["password"]):
        show_error("missing field")
    else:
        db_connection = connect_to_db()
        if validate_username_and_password(db_connection, user_entry):
            root.destroy()
            user_type = get_user_type(db_connection, user_entry)
            if user_type == FACULTY_USER_TYPE:
                open_professor_page(user_entry["username"])
            elif user_type == STUDENT_USER_TYPE:
                open_student_page(user_entry["username"])
            else:
                open_administrator_page(user_entry["username"])


def click_register():
    root.destroy()
    import registration_page


#------------------------------------------RESPONSIVE ELEMENTS SETUP----------------------------------------------------
page_name_label = tkinter.Label(root, text="LOGIN", font=("Georgia", 20))
page_name_label.pack()

username_label = tkinter.Label(root, text="Username", font=("Georgia", 14), bg='#C1E1C1')
username_label.place(x=100, y=100)
username_text = tkinter.Entry(root, width=30, bg='#fffdaf')
username_text.place(x=200, y=100)

password_label = tkinter.Label(root, text="Password", font=("Georgia", 14), bg='#C1E1C1')
password_label.place(x=100, y=180)
password_text = tkinter.Entry(root, width=30, show="***", bg='#fffdaf')
password_text.place(x=200, y=180)

login_button = tkinter.Button(root, text="Login", bg='#fffdaf', command=click_login, width=9, height=2)
login_button.place(x=100, y=300)

register_button = tkinter.Button(root, text="Register", bg='#fffdaf', command=click_register, width=9, height=2)
register_button.place(x=240, y=300)

root.mainloop()

