from lib.src import pass_validation, connect_server, register_pass_master
from lib.screen import screen, get_text

# Main program
screen()
connect_server()
register_pass_master()
pass_validation()