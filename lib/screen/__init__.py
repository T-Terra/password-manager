from tkinter import *
from lib.src import *

# Função que acha a localização da tela
'''def cli_esq_mouse(re):
    print(f'X: {re.x} | Y: {re.y} | Geo: {window.geometry()}')'''
# Tela principal
def screen():
    global window, input_user
    window = Tk()
    window.title('Gerenciador de Senhas')
    window.iconphoto(False, PhotoImage(file='./img/seguranca.ico'))
    window.geometry('400x250+623+341')
    window.wm_resizable(width=False, height=False) # para não almentar a tela com o mouse 
    # mapeando o cursor do mouse e o tamanho da janela
    #window.bind('<Button-1>', cli_esq_mouse)
    input_user = Entry(window, font='Arial 12')
    input_user.grid(column=1, row=0)
    txt = Label(window, text='Senha mestra: ')
    txt.grid(column=0, row=0, padx=50, pady=10, )
    button = Button(window, text='Enviar', command=pass_validation)
    button.grid(column=1, row=2, padx=0, pady=10)
    window.mainloop()

# Pega a informação da caixa de input
def get_text():
    texts = input_user.get()