from Tkinter import *

class Monitor:

	def __init__(self,root,lista_emp):

		self.lista_emp = lista_emp


		self.MenuBar(root)
		self.IniciaList()

	def MenuBar(self,root):
		menubar 			= Menu(root)
		root.configure(menu = menubar)
		menuReports 		= Menu(menubar)
		menuDatabase	 	= Menu(menubar)
		menuAbout			= Menu(menubar)

		menubar.add_cascade(label = 'Relatórios',menu=menuReports)
		menubar.add_cascade(label = 'Database',menu=menuDatabase)
		menubar.add_cascade(label = 'Sobre',menu=menuAbout)

		menuDatabase.add_command(label="AtualizarDB", command=self.AtualizarDatabase)
		menuReports.add_command(label="Historico Rep", command=self.historyrep)


	def historyrep(self):
		PopupRep()


	def IniciaList(self):
		self.MsgName 		=[]
		self.botaoAtencao 	=[]
		self.MsgContageON 	=[]
		self.MsgContagetot 	=[]


	def Create_containers(self,root):
		self.ContainerStatus           	 	= Frame (root,bg="black")
		self.ContainerStatus.grid                 (row=0, sticky = N + W + E)

		self.ContainerDiv             		= Frame (root,bg="yellow")
		self.ContainerDiv.grid                 (row=1, sticky = N + W + E)

		self.ContainerDiv2              	= Frame (self.ContainerDiv,bg="yellow")
		self.ContainerDiv2.grid                 (row=1,pady=1, sticky = N + W + E)

		self.ContaineParte2					= Frame(root,bg="black")
		self.ContaineParte2.grid                 (row=2,sticky = N + W + E + S)

		self.ContaineEmpresas1				= Frame(self.ContaineParte2,bg="black")
		self.ContaineEmpresas1.grid                 (row=0,pady=2,padx=2, column=0, sticky = "N")

		#self.Containesep					= Frame(self.ContaineParte2,bg="yellow")
		#self.Containesep.grid                 (row=0,padx=3, column=1, sticky = N + W + E + S)

		self.ContainerGrafc					= Frame(self.ContaineParte2,bg="black")
		self.Cont

	def AtualizarDatabase(self):
		
		serv = Servico()
		serv.Stop()

		time.sleep(15)
		Telas.root.destroy()

		python = sys.executable
		os.execl(python, python, * sys.argv)

	def Create_emps(self):

		
		for item in  range (len(self.lista_emp)):
			self.Create_emp(item)



	def Create_emp(self,id_emp):
		
		self.MsgName.append				("")
		self.botaoAtencao.append 		("")
		self.MsgContageON.append		("")
		self.MsgContagetot.append 		("")

		qnt = (len(self.lista_emp)+1)/3
		

		name_emp 			= self.lista_emp[id_emp][1]
		On_Line_rep			= 00
		total_rep 			= self.lista_emp[id_emp][10]
		self.lista_emp[id_emp][12] = id_emp



		if (qnt*2 ) > id_emp >= (qnt):
			coluna = 4
			row_line = id_emp - (qnt)  + 1
		elif id_emp >= (qnt*2):
			coluna = 8
			row_line = id_emp - (qnt*2 ) + 1
		else:
			coluna = 0
			row_line = id_emp + 1

		

		if row_line == 1:

			self.MsgCabName				= Label (
									self.ContaineEmpresas1,
									text = "Empresa",
									font="arialblack 12 bold",
									bg="black",
									fg="white",
									width=15)

			self.MsgCabName.grid(
									row=0,
									column=coluna)




			self.MsgCabOn 		= Label (
									self.ContaineEmpresas1,
									text = "On" ,
									font="arialblack 12 bold",
									bg="black",
									fg="white",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1,
									width=5)

			
			self.MsgCabOn.grid (
									row=0,
									column=coluna+2,
									pady=3)


			self.MsgCabTot 		= Label (
									self.ContaineEmpresas1,
									text = "Total" ,
									font="arialblack 12 bold",
									bg="black",
									fg="white",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
			self.MsgCabTot.grid (
									row=0,
									column=coluna+3,
									pady=1)





		self.MsgName[id_emp]				= Label (
									self.ContaineEmpresas1,
									text = name_emp,
									font="arialblack 12 bold",
									bg="black",
									fg="white",
									width=15)

		self.MsgName[id_emp].grid(
									row=row_line,
									column=coluna)


			


		self.botaoAtencao[id_emp]  		= Button( 
									self.ContaineEmpresas1,
									font="arial 11 bold" , 
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									text='OK',
									bg="green3",
									width=2,
									height=1)

		self.botaoAtencao[id_emp].grid (
									row=row_line,
									column=coluna+1,
									sticky = "N")





		
		self.MsgContageON[id_emp] 		= Label (
									self.ContaineEmpresas1,
									text = (str(On_Line_rep)).zfill(2),
									font="arialblack 12 bold",
									bg="black",
									fg="yellow",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		self.MsgContageON[id_emp].grid (
									row=row_line,
									column=coluna+2,
									pady=1)


		self.MsgContagetot[id_emp] 		= Label (
									self.ContaineEmpresas1,
									text = (str(total_rep)).zfill(2),
									font="arialblack 12 bold",
									bg="black",
									fg="white",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		self.MsgContagetot[id_emp].grid (
									row=row_line,
									column=coluna+3,
									pady=3)

