from tkinter import *

UsernameList = []


root = Tk()

# window size and colour
root.geometry('650x330')
root.configure(bg='light steel blue')


# defining and configuring the menu frame
main_menu = Frame(root)
main_menu.configure(bg="light steel blue")
main_menu.grid(row=0, column=0)


SignInMenu_button = Button(main_menu, text="Yes!", font="Helvetica 15",
                           command=lambda: Sign_In())
SignInMenu_button.grid(row=3, column=0, pady=50)

SignIn_button = Button(main_menu, text="Sign in", font="Helvetica 15",
                       command=lambda: Sign_In())
SignIn_button.grid(row=3, column=0, pady=50)


def Sign_In():
    global signIn_menu
    # gives the bingo menu a location on the screen, so it is visible
    signIn_menu.grid(row=0, column=0)
    # using .grid_forget() to remove the main menu from the screen
    main_menu.grid_forget()


def ValidateUserCredentials(username, password):
    while usernamefound == False:
        for i in range(len(usernamelist)):
            if username != usernamelist[i]:
                usernnamefound = True


# defining and configuring the outcome frame
signIn_menu = Frame(root)
signIn_menu.grid(row=0, column=0)
signIn_menu.grid_forget()


UsernameLabel = Label(signIn_menu, text="Username")
UsernameLabel.grid(row=0, column=0)
# creating label
PasswordLabel = Label(signIn_menu, text="PasswordLabel")
PasswordLabel.grid(row=1, column=0)

SubmitInformationButton = Button(signIn_menu, text="Submit", activebackground="pink", activeforeground="blue",
                                 command=lambda ValidateUserCredentials: (UsernameStringVar, PasswordStringVar))
SubmitInformationButton.grid(row=3, column=2)


UsernameStringVar = StringVar()
EntryBox1 = Entry(signIn_menu, textvariable=UsernameStringVar, width=20)
EntryBox1.grid(row=0, column=3)

PasswordStringVar = StringVar()
EntryBox2 = Entry(signIn_menu, textvariable=PasswordStringVar, width=20)
EntryBox2.grid(row=2, column=3)

UsernameList = []

# test
root.mainloop()
