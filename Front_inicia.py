from b_db import Mysqldb as DB 
from Tkinter import *
from Front_Reps import Scream
from f_gettime import Telas

def main_front():

	db = DB(True)
	db.connect()
	lista_emp = db.GuetList("tbl_emp")
	lista_rep = db.GuetList("tbl_rep")
	db.close()

	root = Tk()

	RotScream(root,lista_emp,lista_rep)


	#root.wm_withdraw()


#Relo1.mainloop()
	root.mainloop()


class RotScream:
	def __init__(self,root,lista_emp,lista_rep):
		lable1 = Label(root, text = "REAL PONTO - LOADING...")
		lable1.grid(row=0,pady=5,padx=20)

		self.iniciascream1(root,lista_emp,lista_rep)
		self.iniciascream2(root,lista_emp,lista_rep)

	def iniciascream1(self,root,lista_emp,lista_rep):
		self.Relo1 = Toplevel(master=None)
		self.Relo1.geometry('1950x950')
		#self.Relo1.bind('<F11>',self.togglefull1)
		self.Relo1.update()
		self.Relo1.grid_rowconfigure(0,weight=1)
		self.Relo1.grid_columnconfigure(0,weight=1)
		self.Relo1.resizable(True,True)
		self.Relo1.configure(background="black")		
		#Relo1.geometry(Relo1.geometry())
		self.Relo1.title("Monitor Relogios 1")
		#self.Relo1.protocol("WM_DELETE_WINDOW",on_closing)
		Telas.Rep[0] = Scream(self.Relo1,1,lista_emp,lista_rep)

	def iniciascream2(self,root,lista_emp,lista_rep):
		self.Relo2 = Toplevel(master=None)
		self.Relo2.geometry('1950x950')
		#self.Relo2.bind('<F11>',self.togglefull1)
		self.Relo2.update()
		self.Relo2.grid_rowconfigure(0,weight=1)
		self.Relo2.grid_columnconfigure(0,weight=1)
		self.Relo2.resizable(True,True)
		self.Relo2.configure(background="black")		
		#Relo2.geometry(Relo2.geometry())
		self.Relo2.title("Monitor Relogios 1")
		#self.Relo2.protocol("WM_DELETE_WINDOW",on_closing)
		Telas.Rep[1] = Scream(self.Relo2,2,lista_emp,lista_rep)

