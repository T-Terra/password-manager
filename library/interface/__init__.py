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
        if resp == 3:
            print(20 * '=')
            print('Saindo do programa...')
            sleep(2)
            break
        