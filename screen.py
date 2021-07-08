from tkinter import *

window = Tk()
window.title('Gerenciador de Senhas')
window.geometry('400x250')
txt = Label(window, text='Texto para teste')
txt.grid(column=0, row=0, padx=153, pady=10)
button = Button(window, text='clique')
button.grid(column=0, row=1, padx=10, pady=10)
window.mainloop()