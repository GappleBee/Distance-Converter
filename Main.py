def Kilometres():  # Function for converting to kilometres
    global miles
    global kilometres
    miles = entryBox.get()
    kilometres = float(miles) * 1.6093
    outputBox["text"] = str(miles) + " mile(s) is " + str(kilometres) + " kilometre(s)"


def Miles():  # Function for converting to miles
    global miles2
    global kilometres2
    kilometres2 = entryBox2.get()
    miles2 = float(kilometres2) * 0.6214
    outputBox2["text"] = (
        str(kilometres2) + " kilometre(s) is " + str(miles2) + " mile(s)"
    )


# Setting the original values for the distances so they can be used in the GUI as soon as it starts up
miles = 0
kilometres = 0
miles2 = 0
kilometres2 = 0

# Setting up the window
window = Tk()
window.title("Distance Converter")
window.geometry("600x400")

# Creating the messages, boxes and buttons required for converting to kilometres
label = Label(window, text="Convert from miles to kilometres:")
label.pack()

entryBox = Entry(window, text=0)
entryBox.pack()

button = Button(window, text="Convert to kilometres", command=Kilometres)
button.pack()

outputBox = Message(
    window, text=str(miles) + " mile(s) is " + str(kilometres) + " kilometre(s)"
)
outputBox.pack()

# Creating the messages, boxes and buttons required for converting to miles
label2 = Label(window, text="Convert from kilometres to miles:")
label2.pack()

entryBox2 = Entry(window, text=0)
entryBox2.pack()

button2 = Button(window, text="Convert to miles", command=Miles)
button2.pack()

outputBox2 = Message(
    window, text=str(kilometres2) + " kilometre(s) is " + str(miles2) + " mile(s)"
)
outputBox2.pack()

window.mainloop()
