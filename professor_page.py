import tkinter
from PIL import Image, ImageTk
from view_my_schedule import open_view_my_schedule

def open_professor_page(logged_in_username):
    FACULTY_USER_TYPE = "FAC"
    STUDENT_USER_TYPE = "STUD"
    #------------------------------------------STATIC PAGE SETUP------------------------------------------------------------
    root = tkinter.Tk()
    root.geometry("700x700")
    root.title("Course Management System")
    root.configure(bg="#C1E1C1")

    img_path = ImageTk.PhotoImage(Image.open("images/professor_img.png"))
    bg_img = tkinter.Label(root, image=img_path)
    bg_img.place(relheight=1, relwidth=.5)

    page_number_label = tkinter.Label(root, text="PROFESSOR HOME PAGE", font=("Georgia", 20))
    page_number_label.pack()

    background_green = '#C1E1C1'
    button_yellow = '#FFFFED'

    #------------------------------------------------FUNCTIONS--------------------------------------------------------------
    def view_catalogue():
        root.destroy()
        import view_catalogue

    def view_my_sched():
        root.destroy()
        open_view_my_schedule(logged_in_username, FACULTY_USER_TYPE)
    #------------------------------------------RESPONSIVE ELEMENTS SETUP----------------------------------------------------
    view_catalogue_button = tkinter.Button(root, text='View Course Catalog', font=('Georgia', 18), command=view_catalogue,
                                           width=30, height=3, bg='#FFFFED')
    view_catalogue_button.place(x=900, y=300)

    view_my_schedule_button = tkinter.Button(root, text="View My Schedule", font=('Georgia', 18), command=view_my_sched,
                                             width=30, height=3, bg='#FFFFED')
    view_my_schedule_button.place(x=900, y=400)
    root.mainloop()
