from tkinter import *
from app.main import *
from app.manager.manager_sign_in import *
import tkinter.messagebox


def mngr_screen():

    global mngr
    global mngr_screen
    global main_screen

    mngr = Tk()
    mngr.title("pay on(manager)")
    mngr.geometry("1100x500")
    mngr.resizable(False, False)
    color = "black"
    color_1 = "#b3f542"
    color_2 = "#f5a442"
    mngr.configure(bg=color_1)

    # =========== Function ===========
    def errorMsg(ms):
        if ms == 'username':
            tkinter.messagebox.showerror('Wrong Username','نام کاربری وارد شده نامعتبر است لطفا دوباره تلاش کنید')
        elif ms == 'password':
            tkinter.messagebox.showerror('Wrong Password','رمز وارد شده نادرست است لطفا دوباره امتحان کنید')
        elif ms == 'invalid':
            tkinter.messagebox.showerror('اظلاعات غلط','اطلاعات وارد شده غلط میباشد لطفا دوباره تلاش کنید')

    def back_to_main_mngr():
        mngr.destroy()
        main_screen()


    username1 = 'mobin'
    password1 = "1234"

    def login():
        if username.get() == username1:
            if password.get() == password1:
                manager_screen()
            else:
                errorMsg('password')

        else:
            errorMsg('username')

    # =========== Labels ===========
    sign_label = Label(mngr, text='Sign To Manager Menu', font=('Commons', 16), bg=color_1, foreground=color_2)
    sign_label.pack(side=TOP,pady=20)

    user_label = Label(mngr, text='Username', font=('Commons', 14), bg=color_1, foreground=color_2)
    user_label.pack(side=TOP)


    # =========== Variables ===========
    username_var = StringVar()
    password_var = StringVar()


    # =========== Entry ===========
    username = Entry(mngr,width=16, font=('Commons', 16), bg=color_2, foreground=color_1,
                      highlightbackground=color_2, textvariable=username_var)
    username.pack(side=TOP, pady=20)

    pass_label = Label(mngr, text='Password', font=('Commons', 14), bg=color_1, foreground=color_2)
    pass_label.pack(side=TOP)

    password = Entry(mngr, width=16, font=('Commons', 16), bg=color_2, foreground=color_1,
                      highlightbackground=color_2,show='X', textvariable=password_var)
    password.pack(side=TOP, pady=20)



    # =========== Button ===========
    log_in = Button(mngr, text="Login", font=("Commons", 14), width=11, height=1, bg=color_2, foreground=color_1,
                      highlightbackground=color_2, command=login)
    log_in.pack(side=TOP, pady=20)

    log_in = Button(mngr, text="Back", font=("Commons", 14), width=11, height=1, bg=color_2, foreground=color_1,
                      highlightbackground=color_2, command=back_to_main_mngr)
    log_in.place(x=0, y=460)


    mngr.mainloop()

mngr_screen()