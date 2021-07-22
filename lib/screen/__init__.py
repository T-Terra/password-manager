from tkinter import *
from lib.src import pass_validation, insert_into, select_data, update_password_master, delete_data

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
    txt.grid(column=0, row=0, padx=25, pady=10)
    button = Button(window, text='Enviar', font='Arial 15', command=send_response)
    button.grid(column=1, row=2, padx=0, pady=5)
    error = Label(window, text='')
    error.grid(column=1, row=3)
    window.mainloop()

# Janela do menu
def screen_menu():
    global option_user, window2
    window2 = Tk()
    window2.title('Gerenciador de Senhas')
    window2.iconphoto(False, PhotoImage(file='./img/seguranca.ico'))
    window2.geometry('550x400+380+150')
    window2.wm_resizable(width=False, height=False)
    Label(window2, text='1 - Inserir novo registro', font='Arial 18', bg='purple4', fg='white').place(x=125, y=30)
    Label(window2, text='2 - Listar senhas', font='Arial 18', bg='purple4', fg='white').place(x=125, y=80)
    Label(window2, text='3 - Recadastrar senha mestra', font='Arial 18', bg='purple4', fg='white').place(x=125, y=130)
    Label(window2, text='4 - Deletar dados', font='Arial 18', bg='purple4', fg='white').place(x=125, y=180)
    Label(window2, text='5 - Sair do programa', font='Arial 18', bg='purple', fg='white').place(x=125, y=230)
    Label(window2, text='Sua opção:', font='Arial 18', bg='purple3', fg='white').place(x=40, y=290)
    option_user = Entry(window2, font='Arial 18')
    option_user.place(x=170, y=290, width=25, height=33)
    Button(window2, text='Enviar', font='Arial 15', bg='green', fg='white', command=send_menu).place(x=205, y=290, height=33)
    window2.mainloop()

# Pega a informação da caixa de input
def send_response():
    texts = str(input_user.get())
    send_label(pass_validation(texts))

def send_menu():
    op = int(option_user.get())
    menu(op)

# Manda a condição para o back-end
def send_label(arg=0):
    if arg == 1:
        window.destroy()
        screen_menu()
    elif arg == 0:
        error['text'] = 'Senha inválida!'

# Função de gera o menu
def menu(resp=0):
    from time import sleep
    while True:
        """main_menu = ['Inserir novo registro', 'Listar senhas', 'Recadastrar senha mestra', 'Deletar dados', 'Sair do programa']
        print(20 * '=')
        for k, v in enumerate(main_menu):
            print(f'{k+1} - {v}')"""
        if resp == 1:
            insert_into()
        elif resp == 2:
            select_data()
        elif resp == 3:
            update_password_master()
        elif resp == 4:
            delete_data()
        elif resp == 5:
            print('Saindo do programa...')
            window2.destroy()
            sleep(1.5)
            break