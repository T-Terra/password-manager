import pymysql.cursors

# Faz a conexão ao banco de dados
def connect_server():
    global cursor, con
    try:
        con = pymysql.Connect(host='localhost', user='root', password='', database='pass')
        cursor = con.cursor()
        print('Conexão efetuada com sucesso!')
        cursor.execute('''CREATE TABLE IF NOT EXISTS words (
        username TEXT NOT NULL,
        pass_word TEXT NOT NULL
        );
        ''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS M_pass (
        pass_word_master TEXT NOT NULL
        );
        ''')
    except (ConnectionError):
        print('ERROR - 404 server not found!')

# Função para inserir dados no banco de dados
def insert_into():
    try:
        user = str(input('nome de usuário: '))
        pass_key = str(input('Cadastre sua senha: '))
        date = '\'' + user + '\'' + ',' + '\'' + pass_key + '\'' + ');' 
        query = """INSERT INTO words (username, pass_word) VALUES ("""
        sql = query + date
        cursor.execute(sql)
        con.commit()
        print('Registros inseridos!')
        cursor.close()   
    except:
        print('ERROR! Dados não foram inseridos.')

# Função que mostra os dados do banco
def select_data():
    try:
        query = """SELECT * FROM words;"""
        cursor.execute(query)
        result = cursor.fetchall()
        for user, p_word in result:
            print(20 * '=')
            print(f'Usuário: {user}\nSenha: {p_word}')
    except:
        print('ERROR! dados não encontrados.')
        
# Função que define a senha mestra para acessar o gerenciador
def pass_master():
    global pass_word
    query = """SELECT * FROM M_pass;"""
    cursor.execute(query)
    result_validate = cursor.fetchall()
    for k, v in enumerate(result_validate):
        for p, m in enumerate(v):
            pass_validate = m
    pass_word = str(input('Senha mestra: '))
    if pass_word == pass_validate:
        menu()
    else:
        print('Erro! Senha inválida.')

# Registra a senha mestra no banco de dados
def register_pass_master():
    global pass_master_key
    query = """SELECT * FROM M_pass;"""
    cursor.execute(query)
    result = cursor.fetchall()
    if result == ():
        pass_master_key = str(input('Cadastre sua senha mestra: '))
        date = '\'' + pass_master_key + '\'' + ');' 
        query = """INSERT INTO M_pass (pass_word_master) VALUES ("""
        sql = query + date
        cursor.execute(sql)
        con.commit()
        print('Senha mestra atualizada com sucesso!')
        cursor.close()

# Atualiza a senha mestra no banco de dados
def update_password_master():
    print('==')

# Função que recebe a resposta do menu
def response_menu():
    global resp
    resp = int(input('Sua opção: '))

# Função de gera o menu
def menu():
    from time import sleep
    while True:
        main_menu = ['Inserir novo registro', 'Listar senhas', 'Recadastrar senha mestra', 'Sair do programa']
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
            print(20 * '=')
            print('Saindo do programa...')
            cursor.close()
            sleep(2)
            break
        