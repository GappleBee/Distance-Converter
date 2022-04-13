def Kilometres():  # Function for converting into kilometres
    miles = entryBox.get()
    kilometres = float(miles) * 1.6093
    outputBox["text"] = str(miles) + " mile(s) is " + str(kilometres) + " kilometre(s)"


def Miles():  # Function for converting into miles
    kilometres2 = entryBox2.get()
    miles2 = float(kilometres2) * 0.6214
    outputBox2["text"] = (
        str(kilometres2) + " kilometre(s) is " + str(miles2) + " mile(s)"
    )


# Setting up the original values for the distances so that they can be displayed before anything is typed in or clicked
miles = 0
kilometres = 0
miles2 = 0
kilometres2 = 0

# Setting up the window
window = Tk()
window.title("Distance Converter")
window.geometry("600x400")

# Setting up the messages, buttons and boxes for converting into kilometres
label = Label(window, text="Convert from miles to kilometres:")
label.pack()

entryBox = Entry(window, text="")
entryBox.pack()

button = Button(window, text="Convert to kilometres", command=Kilometres)
button.pack()

outputBox = Message(
    window, text=str(miles) + " mile(s) is " + str(kilometres) + " kilometre(s)"
)
outputBox.pack()

# Setting up the messages, buttons and boxes for converting into miles
label2 = Label(window, text="Convert from kilometres to miles:")
label2.pack()

entryBox2 = Entry(window, text="")
entryBox2.pack()

button2 = Button(window, text="Convert to miles", command=Miles)
button2.pack()

outputBox2 = Message(
    window, text=str(kilometres2) + " kilometre(s) is " + str(miles2) + " mile(s)"
)
outputBox2.pack()

window.mainloop()
