import lib.interface

# Main program
lib.interface.connect_server()
lib.interface.register_pass_master()
lib.interface.pass_validation()

'''from hashlib import sha256


def cryptography(pass_cryp=''):
    crypt = sha256()
    crypt.update(str.encode(pass_cryp))
    c = crypt.hexdigest()
    return print(c)

cryptography(input('senha: '))

crypt = sha256()
crypt.update(b'1234')
c = crypt.hexdigest()
print(c)'''