from ..library.interface import pass_master, connect_server, register_pass_master

connect_server()
register_pass_master()
pass_master()

'''import hashlib


def cryptography():
    crypt = hashlib.sha256()
    crypt.update(b'hello jhakghfjgda')
    print(crypt.hexdigest())
    print(crypt.digest_size)


cryptography()'''