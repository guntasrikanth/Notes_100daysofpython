import tkinter

window = tkinter.Tk()
window.title('My GUI')
window.minsize(width=600, height=400)
window.config(padx=10, pady=10)

# Label

label = tkinter.Label(text="I'm Srikanth", font=('cambric', 24, 'italic'))
# label.pack()
# label.place(x=100, y=23)
label.grid(row=0, column=0)
label.config(padx=10, pady=10)

# Button

def clicked_me():
    label['text'] = input_data.get()
    print(input_data.get())


button = tkinter.Button(text='Click', command=clicked_me)
# button.pack()
button.grid(row=1, column=1)


button1 = tkinter.Button(text='Click', command=clicked_me)
# button.pack()
button1.grid(row=0, column=2)

# Entry

input_data = tkinter.Entry(width=10)
# input_data.pack()
input_data.grid(row=2, column=3)

window.mainloop()