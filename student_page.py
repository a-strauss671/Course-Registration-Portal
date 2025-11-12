import tkinter
from PIL import Image, ImageTk
from add_courses import open_add_courses
from drop_courses import open_drop_courses

def open_student_page(logged_in_username):
#------------------------------------------STATIC PAGE SETUP------------------------------------------------------------
    root = tkinter.Tk()
    root.geometry("700x700")
    root.title("Course Management System")
    root.configure(bg="#C1E1C1")

    img_path = ImageTk.PhotoImage(Image.open("images/student_page_img.png"))
    bg_img = tkinter.Label(root, image=img_path)
    bg_img.place(relheight=1, relwidth=.5)

    page_number_label = tkinter.Label(root, text="STUDENT HOME PAGE", font=("Georgia", 20))
    page_number_label.pack()

    background_green = '#C1E1C1'
    button_yellow = '#FFFFED'
#------------------------------------------------FUNCTIONS--------------------------------------------------------------
    def view_profile():
        root.destroy()
        from view_profile import open_view_profile
        open_view_profile(logged_in_username)

    def add_course():
        root.destroy()
        open_add_courses(logged_in_username)

    def drop_course():
        root.destroy()
        open_drop_courses(logged_in_username)

    def view_courses():
        root.destroy()
        import view_catalogue

    def view_my_sched():
        root.destroy()
        from view_my_schedule import open_view_my_schedule
        open_view_my_schedule(logged_in_username, "STU")
    #------------------------------------------RESPONSIVE ELEMENTS SETUP----------------------------------------------------
    view_profile_button = tkinter.Button(root, text='View Student Profile', font=('Georgia', 18), command=view_profile, width=30, height=3, bg='#FFFFED')
    view_profile_button.place(x=900, y=200)

    add_course_button = tkinter.Button(root, text='Add Courses', font=('Georgia', 18), command=add_course, width=30, height=3, bg='#FFFFED')
    add_course_button.place(x=900, y=300)

    drop_course_button = tkinter.Button(root, text='Drop Courses', font=('Georgia', 18), command=drop_course, width=30, height=3, bg='#FFFFED')
    drop_course_button.place(x=900, y=400)

    view_courses_button = tkinter.Button(root, text='View Course Catalog', font=('Georgia', 18), command=view_courses, width=30, height=3, bg='#FFFFED')
    view_courses_button.place(x=900, y=500)

    view_my_schedule_button = tkinter.Button(root, text='View My Scheduele',font=('Georgia', 18), command=view_my_sched, width=30, height=3, bg='#FFFFED' )
    view_my_schedule_button.place(x=900, y=600)

    root.mainloop()
