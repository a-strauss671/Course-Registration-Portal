import tkinter
from tkinter import messagebox
import customtkinter
from PIL import Image, ImageTk
import mysql_credentials
import mysql.connector
from professor_page import open_professor_page
from student_page import open_student_page
from administrator_page import open_administrator_page
from shared_functionality import *
#------------------------------------------ STATIC PAGE SETUP-----------------------------------------------------------
root = tkinter.Tk()
root.geometry("700x700")
root.title("Course Management System")

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

img_path = ImageTk.PhotoImage(Image.open("images/registration_img.png"))
bg_img = tkinter.Label(root, image=img_path)
bg_img.place(relheight=1, relwidth=1)

page_title = customtkinter.CTkLabel(root, text='Registration')
page_title.pack(pady=20)

frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=40, pady=20, fill='both', expand=True)

#------------------------------------------------FUNCTIONS--------------------------------------------------------------
def create_new_user_in_db(user_info):
    mydb = mysql.connector.connect(host=mysql_credentials.host, port=mysql_credentials.port,
                                   user=mysql_credentials.user, password=mysql_credentials.password,
                                     database='course_management_system')

    mycursor = mydb.cursor()
    placeholders = ', '.join(['%s'] * len(user_info))
    columns = ', '.join(user_info.keys())
    query = "INSERT into logins ( %s ) VALUES ( %s ) " % (columns, placeholders)
    mycursor.execute(query, list(user_info.values()))
    mydb.commit()

    messagebox.showinfo(message="Account Created!")
    root.destroy()

def take_to_next_page(user_info):
    match user_info["user_type"]:
        case "ADM":
            open_administrator_page(user_info)
        case "STU":
            open_student_page(user_info)
        case "FAC":
            open_professor_page(user_info)
        case _:
            show_error("unknown user type")

def check_user_info(user_info):
    phone_number = user_info["phone_number"]
    birthday = user_info["birthday"]
    username = user_info["username"]
    phone_number_formatted = (len(phone_number) == 12 and phone_number[0:3].isnumeric() and phone_number[3] == '-' and
                              phone_number[4:7].isnumeric() and phone_number[7] == '-' and phone_number[8:].isnumeric())
    birthday_formatted = (len(birthday) == 10 and birthday[0:2].isnumeric() and birthday[2] == '/' and
                          birthday[3:5].isnumeric() and birthday[5] == '/' and birthday[6:].isnumeric())


    if username[:3] in ["ADM", "STU", "FAC"]:
        if not phone_number_formatted:
            show_error("phone number format")
            return False
        else:
            if not birthday_formatted:
                show_error("birthday format")
                return False
            else:
                user_info["user_type"] = user_info["username"][:3]
                return True

    else:
        show_error("username")
        return False

def get_fields():
    user_info = {"first_name": first_name_text.get(),
                  "last_name": last_name_text.get(),
                  "username": username_text.get(),
                  "password": password_text.get(),
                  "department": department_dropdown.get(),
                  "email": email_text.get(),
                  "phone_number": phone_number_text.get(),
                  "birthday": birthday_text.get(),
    }
    return user_info

def click_register():
    user_info = get_fields()
    complete_info = user_info["first_name"] and user_info["last_name"] and user_info["username"] and user_info["password"] \
                    and user_info["department"] and user_info["email"] and user_info["phone_number"] and user_info["birthday"]
    if not terms_and_conditions_agreed.get():
        show_error("terms agreement")
    elif complete_info:
        if check_user_info(user_info):
            create_new_user_in_db(user_info)
            take_to_next_page(user_info)
    else:
        show_error("missing field")



def cancel():
    root.destroy()

#------------------------------------------RESPONSIVE ELEMENTS SETUP----------------------------------------------------
first_name_text = customtkinter.CTkEntry(frame, placeholder_text="")
first_name_text.pack(padx=10, pady=10)

last_name_text = customtkinter.CTkEntry(frame, placeholder_text="Last name")
last_name_text.pack(padx=10, pady=10)

username_text = customtkinter.CTkEntry(frame, placeholder_text="Username")
username_text.pack(padx=10, pady=10)

password_text = customtkinter.CTkEntry(frame, placeholder_text="Password", show="***")
password_text.pack(padx=10, pady=10)

department_list = ["English", "History", "Journalism", "Biology", "Computer Science", "Mathematics", "Theater", "Chemistry",
                   "Economics", "N/A"]
department_dropdown= customtkinter.CTkComboBox(master=frame, values=department_list)
department_dropdown.pack(padx=10, pady=10)

email_text = customtkinter.CTkEntry(frame, placeholder_text="Email")
email_text.pack(padx=10, pady=10)

phone_number_text = customtkinter.CTkEntry(frame, placeholder_text="Phone number")
phone_number_text.pack(padx=10, pady=10)

birthday_text = customtkinter.CTkEntry(frame, placeholder_text="Birthday (MM/DD/YYY)")
birthday_text.pack(padx=10, pady=10)

terms_and_conditions_agreed = tkinter.IntVar()
agreement_box = customtkinter.CTkCheckBox(frame, text="Agree to terms and conditions", variable=terms_and_conditions_agreed)
agreement_box.pack(padx=10, pady=10)

register_button = customtkinter.CTkButton(frame, text='Register', command=click_register)
register_button.pack(padx=10, pady=10)

cancel_button = customtkinter.CTkButton(frame, text='Cancel', command=cancel)
cancel_button.pack(padx=10, pady=10)

root.mainloop()

