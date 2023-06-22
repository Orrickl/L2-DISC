from tkinter import *

root = Tk()

#window size and colour
root.geometry('650x330')
root.configure(bg='light steel blue')


# defining and configuring the menu frame
main_menu = Frame(root)
main_menu.configure(bg="light steel blue")
main_menu.grid(row=0, column=0)


SignInMenu_button = Button(main_menu
, text="Yes!", font="Helvetica 15",
                             command=lambda: Sign_In())
SignInMenu_button.grid(row=3, column=0, pady=50)

SignIn_button = Button(main_menu
, text="Sign in", font="Helvetica 15",
                             command=lambda: Sign_In())
SignIn_button.grid(row=3, column=0, pady=50)

def Sign_In():
    global signIn_menu
    signIn_menu.destroy()
    # recreates the bingo menu so that it can be used again
    signIn_menu = Frame(root)
    # gives the bingo menu a location on the screen, so it is visible
    signIn_menu.grid(row=0, column=0)
    # using .grid_forget() to remove the main menu from the screen
    main_menu.grid_forget()

# defining and configuring the outcome frame
signIn_menu = Frame(root)
signIn_menu.grid(row=0, column=0)
signIn_menu.grid_forget()


#test
root.mainloop()