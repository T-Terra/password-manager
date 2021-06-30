import pymysql.cursors

# Faz a conexão ao banco de dados
def connect_server():
    global cursor, con
    try:
        con = pymysql.Connect(host='localhost', user='root', password='', database='pass')
        cursor = con.cursor()
        #print('Conexão efetuada com sucesso!')
        cursor.execute('''CREATE TABLE IF NOT EXISTS words (
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
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
    connect_server()
    try:
        user = str(input('nome de usuário: '))
        pass_key = str(input('Cadastre sua senha: '))
        date = '\'' + user + '\'' + ',' + '\'' + pass_key + '\'' + ');' 
        query = """INSERT INTO words (username, pass_word) VALUES ("""
        sql = query + date
        cursor.execute(sql)
        con.commit()
        print('Registros inseridos!')
    except:
        print('ERROR! Dados não foram inseridos.')
    cursor.close()   

# Função que mostra os dados do banco
def select_data():
    global id_user
    connect_server()
    try:
        query = """SELECT * FROM words;"""
        cursor.execute(query)
        result = cursor.fetchall()
        for id, user, p_word in result:
            print(20 * '=')
            print(f'ID:{id}\nUsuário: {user}\nSenha: {p_word}')
            id_user = str(id)
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
        date = '\'' + pass_master_key + '\'' + ');' 
        query = """INSERT INTO M_pass (pass_word_master) VALUES ("""
        sql = query + date
        cursor.execute(sql)
        con.commit()
        print('Senha mestra atualizada com sucesso!')
    cursor.close()

# Função que define a senha mestra para acessar o gerenciador
def pass_master():
    global pass_word
    connect_server()
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
    cursor.close()
# Atualiza a senha mestra no banco de dados
def update_password_master():
    connect_server()
    try:
        re_register = str(input('Recadastrar senha: '))
        print('Senha salva com sucesso!!')
        query = """UPDATE M_pass set pass_word_master = """
        data = '\'' + re_register + '\'' + ';'
        sql = query + data
        cursor.execute(sql)
        con.commit()
    except:
        print('ERROR! Não foi possível cadastrar a senha mestra.')
    cursor.close()

# Deleta os dados pelo ID do usuário
def delete_data():
    connect_server()
    try:
        delete_users = str(input('Qual registro deseja apagar? ID: '))
        query = """DELETE FROM words WHERE id="""
        data = delete_users + ';'
        sql = query + data
        cursor.execute(sql)
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
            sleep(2)
            break
