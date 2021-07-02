'''from ..library.interface import pass_master, connect_server, register_pass_master

connect_server()
register_pass_master()
pass_master()'''

from hashlib import sha256


def cryptography(pass_cryp=''):
    crypt = sha256()
    crypt.update(b'{}'.format(pass_cryp))
    c = crypt.hexdigest()
    return print(c)

cryptography(input('senha: '))