# ivoxprojects
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title("navbar")


def Frame1():
    global frame
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=5, padx=5, fill="both", expand=True)

    label = customtkinter.CTkLabel(
        master=frame,
        text="Frame 1",
        text_font=("Trebuchet MS", 35, "bold"),
        anchor=customtkinter.CENTER,
    )
    label.place(relx=0.35, rely=0.4)


def Frame2():
    global frame
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=5, padx=5, fill="both", expand=True)

    label = customtkinter.CTkLabel(
        master=frame,
        text="Frame 2",
        text_font=("Trebuchet MS", 35, "bold"),
        anchor=customtkinter.CENTER,
    )
    label.place(relx=0.35, rely=0.4)


def Frame3():
    global frame
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=5, padx=5, fill="both", expand=True)

    label = customtkinter.CTkLabel(
        master=frame,
        text="Frame 3",
        text_font=("Trebuchet MS", 35, "bold"),
        anchor=customtkinter.CENTER,
    )
    label.place(relx=0.35, rely=0.4)


def CloseFrame():
    frame.destroy()


# region navbar
navbar = customtkinter.CTkFrame(master=root)
navbar.pack(padx=5, pady=5, fill="x")

label = customtkinter.CTkLabel(
    master=navbar, text="ivoxprojects", text_font=("Trebuchet MS", 15)
)
label.pack(side=customtkinter.RIGHT)

button1 = customtkinter.CTkButton(
    master=navbar,
    text="Frame 1",
    text_font=("Trebuchet MS", 12, "bold"),
    text_color="white",
    hover=True,
    hover_color="gray",
    height=40,
    width=70,
    border_width=2,
    corner_radius=5,
    border_color="#3b8cc6",
    bg_color="#262626",
    fg_color="#262626",
    command=lambda: [CloseFrame(), Frame1()],
)
button1.pack(side=customtkinter.LEFT)

button2 = customtkinter.CTkButton(
    master=navbar,
    text="Frame 2",
    text_font=("Trebuchet MS", 12, "bold"),
    text_color="white",
    hover=True,
    hover_color="gray",
    height=40,
    width=70,
    border_width=2,
    corner_radius=5,
    border_color="#3b8cc6",
    bg_color="#262626",
    fg_color="#262626",
    command=lambda: [CloseFrame(), Frame2()],
)
button2.pack(side=customtkinter.LEFT, padx=5)

button3 = customtkinter.CTkButton(
    master=navbar,
    text="Frame 3",
    text_font=("Trebuchet MS", 12, "bold"),
    text_color="white",
    hover=True,
    hover_color="gray",
    height=40,
    width=70,
    border_width=2,
    corner_radius=5,
    border_color="#3b8cc6",
    bg_color="#262626",
    fg_color="#262626",
    command=lambda: [CloseFrame(), Frame3()],
)
button3.pack(side=customtkinter.LEFT)
# endregion

Frame1()
root.mainloop()
