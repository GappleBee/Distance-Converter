def Kilometres():
    miles = entryBox.get()
    kilometres = float(miles) * 1.6093
    outputBox["text"] = str(miles) + " mile(s) is " + str(kilometres) + " kilometre(s)"


def Miles():
    kilometres2 = entryBox2.get()
    miles2 = float(kilometres2) * 0.6214
    outputBox2["text"] = (
        str(kilometres2) + " kilometre(s) is " + str(miles2) + " mile(s)"
    )


miles = 0
kilometres = 0
miles2 = 0
kilometres2 = 0

window = Tk()
window.title("Distance Converter")
window.geometry("600x400")

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
