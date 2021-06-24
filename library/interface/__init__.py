import pymysql.cursors

pass_master_key = 'suco'

def connect_server():
    global cursor
    try:
        con = pymysql.Connect(host='localhost', user='root', password='', database='pass')
        cursor = con.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS words (
        username TEXT NOT NULL,
        pass_word TEXT NOT NULL
        );
        ''')
    except:
        print('Erro - 404 server not found!')

def insert_into():
    user = str(input('nome de usuário: '))
    pass_key = str(input('Cadastre sua senha mestra: '))
    query = '''INSERT INTO words (username, pass_word) VALUES (%s, %s)'''
    cursor.execute(query, (user, pass_key))

def pass_master():
    global pass_word
    pass_word = str(input('Senha mestra: '))
    if pass_word == pass_master_key:
        menu()
    else:
        print('Erro! Senha inválida.')

def list_passwords():
    print(20 * '=')
    print(pass_word)
    print(20 * '=')

def response_menu():
    global resp
    resp = int(input('Sua opção: '))

def menu():
    from time import sleep
    while True:
        main_menu = ['Cadastrar senha mestra', 'Listar senhas', 'Sair do programa']
        for k, v in enumerate(main_menu):
            print(f'{k+1} - {v}')
        response_menu()
        if resp == 1:
            insert_into()
        elif resp == 2:
            list_passwords()
        elif resp == 3:
            print(20 * '=')
            print('Saindo do programa...')
            sleep(2)
            break
        