from tkinter import *
from app.main import *
import tkinter.messagebox
import os
import app.manager.data
import app.manager.data_1



def manager_screen():

    global manager
    global manager_screen
    global selected_waiter
    global selected_item
    global main_screen

    manager = Tk()
    manager.title("pay on(manager)")
    manager.geometry("1100x500")
    manager.resizable(False, False)
    color = "black"
    color_1 = "#b3f542"
    color_2 = "#f5a442"
    manager.configure(bg=color_1)



    # ============ variables ============
    username = StringVar()
    password = StringVar()




    # ============ Functions ============

    def errorMsg(ms):
        if ms == 'error':
            tkinter.messagebox.showerror('دوباره امتحان کنید','مشکلی پیش آمده لطفا دوباره امتحان کنید')

    def back_to_main_manager():
        manager.destroy()
        main_screen()
    # ======= waiters function =======
    def clear_waiter_list():
        waiter_list.delete(0, END)

    def fill_waiter_list(waiter):
        for waiterr in waiter:
            waiter_list.insert(END, waiterr)

    def waiter_list_view():
        clear_waiter_list()
        waiter = app.manager.data.view()
        fill_waiter_list(waiter)
    # ======= waiters function =======
    # ======= items function =======
    def clear_item_list():
        item_list_manager.delete(0, END)

    def fill_item_list(items):
        for item_ in items:
            item_list_manager.insert(END, item_)

    def item_list_view():
        clear_item_list()
        items = app.manager.data_1.view()
        fill_item_list(items)
    # ======= items function =======


    # ============ Label ============
    waiter_name_label = Label(manager, text="Waiter", font=("Commons", 15), bg=color_1)
    waiter_name_label.grid(row = 0, column = 2)

    waiter_age_label = Label(manager, text="Age", font=("Commons", 15), bg=color_1)
    waiter_age_label.grid(row = 1, column = 2)

    waiter_income_label = Label(manager, text="Income", font=("Commons", 15), bg=color_1)
    waiter_income_label.grid(row = 2, column = 2)

    item_name_label = Label(manager, text="item Name", font=("Commons", 15), bg=color_1)
    item_name_label.grid(row = 0, column = 3)

    item_price_label = Label(manager, text="Item Price", font=("Commons", 15), bg=color_1)
    item_price_label.grid(row = 1, column = 3)

    # ============ Entry ============
    waiter_text = StringVar()
    waiter_name = Entry(manager, font=("Commons", 15), bg=color_2, foreground=color_1,
                      width=14,highlightbackground=color_2, textvariable=waiter_text)
    waiter_name.grid(row = 0, column=1)

    waiter_age = Entry(manager, font=("Commons", 15), bg=color_2, foreground=color_1,
                      width=14,highlightbackground=color_2)
    waiter_age.grid(row = 1, column = 1)

    waiter_income_text = StringVar()
    waiter_income = Entry(manager, font=("Commons", 15), bg=color_2, foreground=color_1,
                      width=14,highlightbackground=color_2, textvariable=waiter_income_text)
    waiter_income.grid(row = 2, column = 1)

    # --------

    item_text = StringVar()
    item_name = Entry(manager, font=("Commons", 15), bg=color_2, foreground=color_1,
                      width=14,highlightbackground=color_2, textvariable=item_text)
    item_name.grid(row = 0, column=4)

    # item_price_text = IntVar()
    item_price = Entry(manager, font=("Commons", 15), bg=color_2, foreground=color_1,
                      width=14,highlightbackground=color_2)
    item_price.grid(row = 1, column=4)
    # item_price.pack(pady=2)
    # ============ List Box ============
    # show waiters
    waiter_list = Listbox(manager, font=('Commons', 15), width=24,
                          height=15, bg=color_2, foreground=color_1, highlightbackground=color_2)
    waiter_list.grid(row = 0, column = 0, rowspan = 8)

    waiter_scroll = Scrollbar(manager, orient='horizontal')
    waiter_scroll.grid(row=8, column=0)

    waiter_list.configure(yscrollcommand = waiter_scroll.set)
    waiter_scroll.configure(command = waiter_list.yview)

    def get_selected_row(event):
        global selected_waiter
        index = waiter_list.curselection()[0]
        selected_waiter = waiter_list.get(index)
        print(selected_waiter)
        waiter_name.delete(0, END)
        waiter_name.insert(END, selected_waiter[1])
        waiter_age.delete(0, END)
        waiter_age.insert(END, selected_waiter[2])
        waiter_income.delete(0, END)
        waiter_income.insert(END, selected_waiter[3])




    waiter_list.bind("<<ListboxSelect>>", get_selected_row)


    # show list of items
    item_list_manager = Listbox(manager, font=('Commons', 15),
                                width=26, height=15, bg=color_2, foreground=color_1,
                      highlightbackground=color_2)
    item_list_manager.grid(row = 0, column = 5, rowspan = 8)

    item_scroll = Scrollbar(manager, orient="horizontal")
    item_scroll.grid(row = 8, column=5)

    item_list_manager.configure(yscrollcommand = item_scroll.set)
    item_scroll.configure(command = item_list_manager.yview)

    def get_selected_row_item(event):
        global selected_item
        index = item_list_manager.curselection()[0]
        selected_item = item_list_manager.get(index)
        item_name.delete(0, END)
        item_name.insert(END, selected_item[1])
        item_price.delete(0, END)
        item_price.insert(END, selected_item[2])




    item_list_manager.bind("<<ListboxSelect>>", get_selected_row_item)

    # ============ Button ============

    # add in waiter lists
    def add_to_waiter_list():
        clear_waiter_list()
        waiter = app.manager.data.insert(waiter_name.get(), waiter_age.get(), waiter_income.get())
        fill_waiter_list(waiter)
        waiter_list_view()

    add_waiter_list = Button(manager,  text="Add", font=("Commons", 14), width=11,
                             height=1, background=color_2, foreground=color_1,
                             highlightbackground=color, command=add_to_waiter_list)
    add_waiter_list.grid(row= 3, column = 1)

    # update in waiter lists
    def update_to_waiter_list():
        app.manager.data.update(selected_waiter[0], waiter_name.get(),
                                         waiter_age.get(), waiter_income.get())
        waiter_list_view()

    update_waiters_list = Button(manager,  text="Update", font=("Commons", 14), width=11,
                                 height=1, background=color_2, foreground=color_1,
                                 highlightbackground=color, command=update_to_waiter_list)

    update_waiters_list.grid(row= 4, column = 1)


    # delete in waiter list
    def delete_to_waiter_list():
        app.manager.data.delete(selected_waiter[0])
        waiter_list_view()

    delete_waiters_list = Button(manager,  text="Delete", font=("Commons", 14), width=11,
                                 height=1, background=color_2, foreground=color_1,
                                 highlightbackground=color, command=delete_to_waiter_list)
    delete_waiters_list.grid(row= 5, column = 1)

    def update_pay_money():
        app.manager.data.update_pay_money(selected_waiter[3] == 0, selected_waiter[0], waiter_age.get(), waiter_name.get())
        waiter_list_view()

    pay_waiters_list = Button(manager,  text="Pay Income", font=("Commons", 14), width=11,
                              height=1, background=color_2, foreground=color_1,
                              highlightbackground=color, command=update_pay_money)
    pay_waiters_list.grid(row= 6, column = 1)




    def refresh_lists():
        waiter_list_view()
        item_list_view()

    # for refresh lists
    refresh_key = Button(manager,  text="Refresh", font=("Commons", 14), width=11,
                         height=1, background=color_2, foreground=color_1,
                         highlightbackground=color, command=refresh_lists)
    refresh_key.grid(row= 6, column = 4)




    def add_to_item_list():
        clear_item_list()
        item = app.manager.data_1.insert(item_name.get(), item_price.get())
        fill_item_list(item)
        item_list_view()

    add_item_list = Button(manager,  text="Add Item", font=("Commons", 14), width=11,
                           height=1, background=color_2, foreground=color_1,
                           highlightbackground=color, command=add_to_item_list)
    add_item_list.grid(row= 2, column = 4)



    def update_to_item_list():
        app.manager.data_1.update(selected_item[0], item_name.get(), item_price.get())
        item_list_view()

    update_item_list = Button(manager,  text="Update Item", font=("Commons", 14), width=11,
                              height=1, background=color_2, foreground=color_1,
                              highlightbackground=color, command=update_to_item_list)
    update_item_list.grid(row= 3, column = 4)



    def delete_to_item_list():
        app.manager.data_1.delete(selected_item[0])
        item_list_view()

    delete_item_list = Button(manager,  text="Delete Item", font=("Commons", 14), width=11,
                    height=1, background=color_2, foreground=color_1,
                              highlightbackground=color, command=delete_to_item_list)
    delete_item_list.grid(row= 4, column = 4)



    def search_to_item_list():
        clear_item_list()
        items = app.manager.data_1.search(item_name.get(), item_price.get())
        fill_item_list(items)


    search_item_list = Button(manager,  text="Search", font=("Commons", 14), width=11,
                    height=1, background=color_2, foreground=color_1,
                              highlightbackground=color, command=search_to_item_list)
    search_item_list.grid(row= 5, column = 4)

    b_back = Button(manager,  text="Back", font=("Commons", 14), width=11, height=1,
                    background=color_2, foreground=color_1,
                    highlightbackground=color, command=back_to_main_manager)
    b_back.place(x=0, y=460)

    # =============================


    item_list_view()
    waiter_list_view()
    manager.mainloop()

manager_screen()