'''from ..library.interface import pass_master, connect_server, register_pass_master

connect_server()
register_pass_master()
pass_master()'''

from hashlib import sha256
l = 'c'

crypt = sha256()
crypt.update(b'{l}')
c = crypt.hexdigest()
print(c)