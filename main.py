from tkinter import *

UsernameList = []
linelist = []

root = Tk()

# window size and colour
root.geometry('650x330')
root.configure(bg='light steel blue')


# defining and configuring the menu frame
main_menu = Frame(root)
main_menu.configure(bg="light steel blue")
main_menu.grid(row=0, column=0)


# fdgdfg
def sign_in():
    global signIn_menu
    # gives the bingo menu a location on the screen, so it is visible
    signIn_menu.grid(row=0, column=0)
    # using .grid_forget() to remove the main menu from the screen
    main_menu.grid_forget()


def log_in(username, password):
    if validate_user_credentials(username, password) == True:
        signIn_menu.grid_forget()
        outcome_statement(username, password)
        # dsfgd


def validate_user_credentials(username, password):
    print(username)
    print(read("Usernames.txt", ".readlines()")[0])
    print(read("Usernames.txt", ".readlines()")[0])
    for i in range(len(read("Usernames.txt", ".readlines()"))):
        print(i)
        if username == read("Usernames.txt", ".readlines()")[i]:
            password_number = i
            if password == read("Passwords.txt", ".readlines()")[password_number]:
                print("correct")
                open_popup("correct", "lets go")
                return True
            open_popup("Unknown Password", "error")
            return False
        open_popup("Unknown Username", "error")
        return False


# dsfgdfg
def open_popup(message, title):
    top = Toplevel(root)
    top.geometry("220x50")
    top.title(title)
    Label(top, text=message).grid(row=1, column=1)


def write(info_to_write, file_to_write_to):
    """opens a file and writs into it"""
    with open(file_to_write_to, "w", encoding="utf-8") as file_to_open:
        file_to_open.write(info_to_write)


def read(file_to_read, *mode):
    """opens a file and reads and prints it"""
    with open(file_to_read, "r", encoding="utf-8") as f:
        contents = f.readlines() if mode == "readlines()" else f.read()
    return contents

def outcome_statement(Username, password):
    outcome_menu.grid(row=0, column=0)

def update_grid(entry_name_var):
    write(entry_name_var, )


write("P", "Passwords.txt")
write("U", "Usernames.txt")


# defining and configuring the outcome frame
signIn_menu = Frame(root)
signIn_menu.grid(row=0, column=0)
signIn_menu.grid_forget()
# ejrdkjrhg


outcome_menu = Frame(root)
outcome_menu.grid(row=0, column=0)
outcome_menu.grid_forget()
# ejrdkjrhg

entry_name_var = StringVar()

entry_name_var.set('placeholder')

entry_name = Entry(outcome_menu, textvariable=entry_name_var)
entry_name.grid(row = 0, column = 0)

text_amount_var = StringVar()

text_amount_var.set('1')

text_amount_entry = Entry(outcome_menu, textvariable=text_amount_var)
text_amount_entry.grid(row = 0, column = 1)

update_button = Button(outcome_menu, command=update_grid(entry_name_var, username))
update_button.grid(row= 2, column= 1)


UsernameLabel = Label(signIn_menu, text="Username")
UsernameLabel.grid(row=0, column=0)
# creating label
PasswordLabel = Label(signIn_menu, text="Password")
PasswordLabel.grid(row=2, column=0)

UsernameStringVar = StringVar()
EntryBox1 = Entry(signIn_menu, textvariable=UsernameStringVar, width=20)
EntryBox1.grid(row=0, column=2)


PasswordStringVar = StringVar()
EntryBox2 = Entry(signIn_menu, textvariable=PasswordStringVar, width=20)
EntryBox2.grid(row=2, column=2)


SubmitInformationButton = Button(signIn_menu, text="Submit", activebackground="pink", activeforeground="blue",
                                 command=lambda: log_in(UsernameStringVar.get(), PasswordStringVar.get()))
SubmitInformationButton.grid(row=3, column=2)

SignInMenu_button = Button(main_menu, text="Yes!", font="Helvetica 15",
                           command=lambda: sign_in())
SignInMenu_button.grid(row=3, column=0, pady=50)

SignIn_button = Button(main_menu, text="Sign in", font="Helvetica 15",
                       command=lambda: sign_in())
SignIn_button.grid(row=3, column=0, pady=50)

# test
root.mainloop()
