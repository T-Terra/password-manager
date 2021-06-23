import pymysql

def connect_server():
    try:
        con = pymysql.connect(host='localhost', user='root', password='', database='pass')
        cursor = con.cursor()
    except:
        print('Erro - 505 server not found!')
    cursor.execute('''CREATE TABLE IF NOT EXISTS words (
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );
    ''')

def pass_master():
    global pass_word
    pass_word = str(input('Cadastre a senha mestra: '))

def list_passwords():
    print(20 * '=')
    print(pass_word)
    print(20 * '=')

def response():
    global resp
    resp = int(input('Sua opção: '))

def menu():
    from time import sleep
    while True:
        main_menu = ['Recadastrar senha mestra', 'Listar senhas', 'Sair do programa']
        for k, v in enumerate(main_menu):
            print(f'{k+1} - {v}')
        response()
        if resp == 1:
            pass_master()
        elif resp == 2:
            list_passwords()
        elif resp == 3:
            print(20 * '=')
            print('Saindo do programa...')
            sleep(2)
            break
        