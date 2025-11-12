import tkinter
from PIL import Image, ImageTk

def open_administrator_page(logged_in_username):
    root = tkinter.Tk()
    root.geometry("700x700")
    root.title("Course Management System")
    root.configure(bg="#C1E1C1")

    img_path = ImageTk.PhotoImage(Image.open("images/administrator_page_img.png"))
    bg_img = tkinter.Label(root, image=img_path)
    bg_img.place(relheight=1, relwidth=.5)

    page_number_label = tkinter.Label(root, text="ADMINISTRATOR HOME PAGE", font=("Georgia", 20))
    page_number_label.pack()

    background_green = '#C1E1C1'
    button_yellow = '#FFFFED'

    def upload_courses():
        root.destroy()
        from upload_courses import open_upload_courses_page
        open_upload_courses_page()

    def view_catalogue():
        root.destroy()
        import view_catalogue


    upload_course_button = tkinter.Button(root, text='Upload Courses', font=('Georgia', 18), command=upload_courses, width=30, height=3, bg='#FFFFED')
    upload_course_button.place(x=900, y=300)

    view_catalogue_button = tkinter.Button(root, text='View Course Catalog', font=('Georgia', 18), command=view_catalogue, width=30, height=3, bg='#FFFFED')
    view_catalogue_button.place(x=900, y=400)

    root.mainloop()