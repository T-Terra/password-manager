import pymysql.cursors
from hashlib import sha256
from tkinter import *

# Faz a conexão ao banco de dados
def connect_server():
    global cursor, con
    try:
        con = pymysql.Connect(host='localhost', user='root', password='', database='pass')
        cursor = con.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS service_storage (
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        service TEXT NOT NULL,
        pass_word TEXT NOT NULL
        );
        ''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS M_pass (
        pass_word_master TEXT NOT NULL
        );
        ''')
    except (ConnectionError):
        print('ERROR - 404 server not found!')

# Criptografa a senha mestra
def cryptography(pass_cryp=0):
    crypt = sha256()
    crypt.update(str.encode(pass_cryp))
    hash = crypt.hexdigest()
    return hash

# Função para inserir dados no banco de dados
def insert_into():
    connect_server()
    try:
        user = str(input('nome de usuário: '))
        pass_key = str(input('Cadastre sua senha: '))
        file_log(user)
        file_log(pass_key)
        hash_user = cryptography(user)
        hash_pass = cryptography(pass_key)
        query = "INSERT INTO service_storage (service, pass_word) VALUES ('"+hash_user+"','"+hash_pass+"'"");"
        cursor.execute(query)
        con.commit()
        print('Registros inseridos!')
    except:
        print('ERROR! Dados não foram inseridos.')
    cursor.close() 

# Função que mostra os dados do banco
def select_data():
    connect_server()
    try:
        query = """SELECT * FROM service_storage;"""
        cursor.execute(query)
        result = cursor.fetchall()
        for id, user, p_word in result:
            print(20 * '=')
            print(f'ID:{id}\nUsuário: {user}\nSenha: {p_word}')
    except:
        print('ERROR! dados não encontrados.')
    cursor.close()

# Registra a senha mestra no banco de dados
def register_pass_master():
    global pass_master_key
    connect_server()
    query = """SELECT * FROM M_pass;"""
    cursor.execute(query)
    result = cursor.fetchall()
    if result == ():
        pass_master_key = str(input('Cadastre sua senha mestra: '))
        hash_pass = cryptography(pass_master_key)
        query = "INSERT INTO M_pass (pass_word_master) VALUES ('"+hash_pass+"'"");"
        cursor.execute(query)
        con.commit()
        print('Senha mestra atualizada com sucesso!')
    cursor.close()

# Função que define a senha mestra para acessar o gerenciador
def pass_validation(screen_p=''):
    connect_server()
    query = """SELECT * FROM M_pass;"""
    cursor.execute(query)
    result_validate = cursor.fetchall()
    for k, v in enumerate(result_validate):
        for p, m in enumerate(v):
            pass_validate = m
    #pass_word = str(input('Senha mestra: '))
    hash_pass = cryptography(screen_p)
    if hash_pass == pass_validate:
        menu()
    else:
        print('Erro! Senha inválida.')
    cursor.close()
# Atualiza a senha mestra no banco de dados
def update_password_master():
    connect_server()
    try:
        re_register = str(input('Recadastrar senha: '))
        hash_pass = cryptography(re_register)
        print('Senha salva com sucesso!!')
        query = "UPDATE M_pass set pass_word_master = '"+hash_pass+"'"";"
        cursor.execute(query)
        con.commit()
    except:
        print('ERROR! Não foi possível cadastrar a senha mestra.')
    cursor.close()

# Deleta os dados pelo ID do usuário
def delete_data():
    connect_server()
    try:
        delete_users = str(input('Qual registro deseja apagar? ID: '))
        query = "DELETE FROM service_storage WHERE id='"+delete_users+"'"";"
        cursor.execute(query)
        con.commit()
        print('Registro apagado com sucesso!')
    except:
        print('ERROR! ID inválido ou não existe.')
    cursor.close()

# Função que recebe a resposta do menu
def response_menu():
    global resp
    resp = int(input('Sua opção: '))
    print(20 * '=')

def file_log(arg=''):
    with open('triggers.log', 'a') as log:
        log.write(f'Inserindo no bando de dados {arg}\n')

def send_response():
    pass_validation(str(value))

# Interface gráfica
def screen():
    global value
    window = Tk()
    window.title('Gerenciador de Senhas')
    window.geometry('400x250')
    input_user = Entry(window)
    input_user.pack()
    txt = Label(window, text='Senha mestra: ')
    value = input_user.get()
    txt.grid(column=0, row=0, padx=60, pady=10, )
    input_user.grid(column=1, row=0)
    button = Button(window, text='Enviar', command=send_response)
    button.grid(column=1, row=2, padx=0, pady=10)
    print(value)
    window.mainloop()

# Função de gera o menu
def menu():
    from time import sleep
    while True:
        main_menu = ['Inserir novo registro', 'Listar senhas', 'Recadastrar senha mestra', 'Deletar dados', 'Sair do programa']
        print(20 * '=')
        for k, v in enumerate(main_menu):
            print(f'{k+1} - {v}')
        response_menu()
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
            cursor.close()
            sleep(1.5)
            break