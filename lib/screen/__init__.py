from tkinter import *


def cli_esq_mouse(re):
    print(f'X: {re.x} | Y: {re.y} | Geo: {window.geometry()}')

def screen():
    global window
    window = Tk()
    window.title('Gerenciador de Senhas')
    window.iconphoto(False, PhotoImage(file='./img/seguranca.ico'))
    window.geometry('400x250+623+341')
    window.wm_resizable(width=False, height=False) # para não almentar a tela com o mouse 
    # mapeando o cursor do mouse e o tamanho da janela
    window.bind('<Button-1>', cli_esq_mouse)
    input_user = Entry(window)
    txt = Label(window, text='Senha mestra: ')
    txt.grid(column=0, row=0, padx=60, pady=10, )
    input_user.grid(column=1, row=0)
    button = Button(window, text='Enviar')
    button.grid(column=1, row=2, padx=0, pady=10)
    window.mainloop()