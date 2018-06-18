from b_db import Mysqldb as DB 
from b_routines import ServiceTest as Serv

def main_back():

	db = DB(True)
	db.connect()
	lista_emp = db.GuetList("tbl_emp")
	lista_rep = db.GuetList("tbl_rep")
	db.close()

	Serv(lista_emp,lista_rep)

