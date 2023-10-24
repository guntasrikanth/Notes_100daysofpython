import tkinter

window = tkinter.Tk()
window.title('My GUI')
window.minsize(width=600, height=400)

# Label

label = tkinter.Label(text="I'm Srikanth", font=('cambric', 24, 'italic'))
label.pack()

# label['text'] = "Second check" - we can assign text to label by any given way
# label.config(text='last one')

# Button

def clicked_me():
    label['text'] = input_data.get()
    print(input_data.get())


button = tkinter.Button(text='Click', command=clicked_me)
button.pack()

#Entry

input_data = tkinter.Entry(width=10)
input_data.pack()
# print(input_data.get())



window.mainloop()
