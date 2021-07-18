from tkinter import *
from lib.src import pass_validation

# Função que acha a localização da tela
'''def cli_esq_mouse(re):
    print(f'X: {re.x} | Y: {re.y} | Geo: {window.geometry()}')'''

# Tela principal
def screen_login():
    global window, input_user, error
    window = Tk()
    window.title('Gerenciador de Senhas')
    window.iconphoto(False, PhotoImage(file='./img/seguranca.ico'))
    window.geometry('400x125+623+341')
    window.wm_resizable(width=False, height=False) # para não almentar a tela com o mouse 
    # mapeando o cursor do mouse e o tamanho da janela
    #window.bind('<Button-1>', cli_esq_mouse)
    input_user = Entry(window, font='Arial 13', show='*')
    input_user.grid(column=1, row=0)
    txt = Label(window, text='Senha mestra: ', font='Arial 14')
    txt.grid(column=0, row=0, padx=25, pady=10, )
    button = Button(window, text='Enviar', font='Arial 15', command=send_response)
    button.grid(column=1, row=2, padx=0, pady=5)
    error = Label(window, text='')
    error.grid(column=1, row=3)
    window.mainloop()

def screen_menu():
    window2 = Tk()
    window2.title('Gerenciador de Senhas')
    window2.iconphoto(False, PhotoImage(file='./img/seguranca.ico'))
    window2.geometry('550x400+380+150')
    window2.wm_resizable(width=False, height=False)
    window2.mainloop()

# Pega a informação da caixa de input
def send_response():
    texts = str(input_user.get())
    send_label(pass_validation(texts))

# Manda a condição para o back-end
def send_label(arg=0):
    if arg == 1:
        window.destroy()
        screen_menu()
    elif arg == 0:
        error['text'] = 'Senha inválida!'