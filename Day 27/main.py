import tkinter

window = tkinter.Tk()
window.title('My GUI')
window.minsize(width=600, height=400)

label = tkinter.Label(text="I'm Srikanth", font=('cambiria', 24, 'italic'))
label.pack()



window.mainloop()
