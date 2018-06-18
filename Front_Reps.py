# -*- coding: utf-8 -*-
#
#
#
#  variaveis vindas do banco: tem prefixo db.
#
#  lista_emp:
#  [0] = id_emp (DB)
#  [1] = name   (DB)
#  [2] = scream (DB)
#  [3] = column (DB)
#  [4] = line   (DB)
#  [5] = delay  (DB)
#  [6] = ID DA EMPRESA NA TELA
#  [7] =
#  [8] =
#  [9] =
#
#
# lista_rep:
#  [0] = id_rep (DB)
#  [1] = id_emp (DB)
#  [2] = name   (DB)
#  [3] = ip     (DB)
#  [4] = port   (DB)
#  [5] = status (DB)
#  [6] = ID DO REP NA TELA
#  [7] = NUMERO DA TELA QUE SE ENCONTRA O REP(PARA FACILITAR O UPDATE)
#

from Tkinter import *

class Scream:

	def __init__(self,root,num,lista_emp,lista_rep):

		self.lista_rep = lista_rep
		self.lista_emp = lista_emp
		self.num	   = num
		self.Init_List()
		self.Create_container_geral(root)
		self.Create_container_colunas(root)
		self.Create_emps(num)
		self.Create_reps(num)

	def Init_List(self):
		self.Container_Empresa	= []
		self.MsgName 			= []
		self.botaoAtencao 		= []
		self.botaoContage		= []
		self.MsgHora 			= []
		self.ContainerColuna 	= []
		self.Container_Empresa 	= []
		self.ButtonList			= []
		self.ButtonListR		= []
		self.listrow 			= []
		#self.listIdEmp			= []



	def Create_container_geral(self,root):


		self.Containerpai = Frame 	(root,bg="black")

		self.Containerpai.grid   	(row=0, 
										column= 0,
										sticky = N + S + E + W)

		#criado para dar o espacamento da tela
		self.ContainerRelogios = Frame 	(self.Containerpai,bg="black")

		self.ContainerRelogios.grid   	(row=0, 
										column= 0,
										padx=3,
										pady=5,
										sticky = N + S + E + W)

	def Create_container_colunas(self,root):

		#Cria os containers de cada empresa.
		#cria 11 colunas
		for coluna in range (11):

			#Inicializção de variaveis, 
			#criando a lista com os espaços necessários

			self.ContainerColuna.append(coluna)

			
			self.ContainerColuna[coluna] = Frame (self.ContainerRelogios,
																bg="black")

			self.ContainerColuna[coluna].grid	(
												row=0,
												column=coluna+1,
												pady=5, 
												padx=0, 
												columnspan=1, 
												sticky="N")


	def Create_emps(self,num):

		id_emp_scream1 = 0
		for item in  range (len(self.lista_emp)):
			
			if self.lista_emp[item][2] == num:
				self.lista_emp[item].extend([''])
				self.Container_Empresa.append 	("")
				self.MsgName.append				("")
				self.botaoAtencao.append 		("")
				self.botaoContage.append 		("")
				self.MsgHora.append 			("")
				self.listrow.append 			(0)

		for item in  range (len(self.lista_emp)):
			
			if self.lista_emp[item][2] == num:
				
				self.lista_emp[item][6] = id_emp_scream1
				self.Create_emp(item,id_emp_scream1)
				id_emp_scream1 = id_emp_scream1 + 1
 

	def Create_emp(self,id_emp,id_emp_scream):
		
		name_emp 			= self.lista_emp[id_emp][1]
		Coluna_container	= self.lista_emp[id_emp][3]
		Linha_container		= self.lista_emp[id_emp][4]
		#id_emp_scream 		= self.lista_emp[id_emp][8]


		
		self.Container_Empresa[id_emp_scream]	= Frame(
									self.ContainerColuna[Coluna_container],
									bg="black")


		self.Container_Empresa[id_emp_scream].grid(
									row=Linha_container,
									column=0,
									pady=0, 
									padx=3, 
									columnspan=1, 
									sticky="N")



		self.MsgName[id_emp_scream]				= Label (
									self.Container_Empresa[id_emp_scream],
									text = name_emp,
									font="arialblack 12 bold",
									bg="black",
									fg="white")

		self.MsgName[id_emp_scream].grid(
									row=0,
									column=0,
									sticky = "N")


			


		self.botaoAtencao[id_emp_scream]  		= Button( 
									self.Container_Empresa[id_emp_scream],
									font="arial 11 bold" , 
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									text='A',
									bg="green3",
									width=2,
									height=1)

		self.botaoAtencao[id_emp_scream].grid (
									row=0,
									column=1,
									sticky = "N")





		
		self.botaoContage[id_emp_scream] 		= Button (
									self.Container_Empresa[id_emp_scream],
									text = "00/00",
									font="arial 11 bold",
									bg="black",
									fg="white",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									width=2,
									bd=0,
									height = 1)

			
		self.botaoContage[id_emp_scream].grid (
									row=1,
									column=1,
									pady=1,
									sticky = "N")






			
		self.MsgHora[id_emp_scream] 				= Label (
									self.Container_Empresa[id_emp_scream],
									text = "Hora 00:00",
									font="arial 11 bold",
									bg="black",
									fg="white")
																			
		self.MsgHora[id_emp_scream].grid (
									row=1,
									column=0,
									pady=3.5, 
									sticky = "N")




	def Create_reps(self,num):

		id_rep = 0
		for item in  range (len(self.lista_rep)):
			
			id_emp 	= self.lista_rep[item][1]
			
			for index in range (len(self.lista_emp)):
				if self.lista_emp[index][0] == id_emp:
					indexemp = index
					break

			if self.lista_emp[indexemp][2] == num:
				self.lista_rep[item].extend(['',''])
				self.lista_rep[item][6] = id_rep
				self.lista_rep[item][7] = num
				self.Create_rep(item,indexemp)
				
				id_rep = id_rep + 1

		
		#for item in  range (len(self.lista_emp)):
	#		if self.lista_emp[item][2] == num:
	#			idd = self.lista_emp[item][8]
#				a = self.listrow[idd]
#				self.lista_emp[item][10] = a
				




	def Create_rep(self,id_rep,indexemp):


		self.ButtonList.append 		("")
		self.ButtonListR.append 	("")
		
		
		name_rep			= self.lista_rep[id_rep][2]
		coontainer_emp		= self.lista_emp[indexemp][6]
		
		buton_id			= self.lista_rep[id_rep][6]

		if self.listrow[coontainer_emp]>31:
			fatorcol = 2
			fatorlin = -34
		else:
			fatorcol = 0
			fatorlin = 0

		self.ButtonList[buton_id] = Button(
									self.Container_Empresa[coontainer_emp],
									font="arial 11 bold" ,  
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									text=name_rep,
									width = 12,
									height = 1,
									bg = "white")

		self.ButtonList[buton_id].grid       (row=self.listrow[coontainer_emp]+2+fatorlin, 
														column=0+fatorcol
														, sticky = "N")

				
		self.ButtonListR[buton_id]= Button(
									self.Container_Empresa[coontainer_emp],
									font="arial 11 bold" ,  
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									text="R",
									width = 2,
									height = 1,
									bg = "white")
		#self.ButtonListR[buton_id].bind  ("<Button-1>",lambda e: PopupRel(id_rep))

		self.ButtonListR[buton_id].grid       (
									row=self.listrow[coontainer_emp]+2+fatorlin, 
								 	column=1+fatorcol, 
								 	sticky = "N")



		self.listrow[coontainer_emp] = self.listrow[coontainer_emp] + 1

       			

	def update(self,rep,Case_color):

		if self.num == self.lista_rep[rep][7]:
			Id_scream 	= self.lista_rep[rep][6]


			if Case_color == 1:
				self.ButtonList[Id_scream].config 	(bg = "red",fg = "white")
				self.ButtonListR[Id_scream].config 	(bg = "red",fg = "white")
		
			if Case_color == 2:
				self.ButtonList[Id_scream].config 	(bg = "green3",fg = "black")
				self.ButtonListR[Id_scream].config 	(bg = "DarkOrange1",fg = "black")
			
			if Case_color == 3:
				self.ButtonList[Id_scream].config 	(bg = "green3",fg = "black")
				self.ButtonListR[Id_scream].config 	(bg = "green3",fg = "black")

			if Case_color == 4:
				self.ButtonList[Id_scream].config 	(bg = "cyan",fg = "black")
				
			if Case_color == 5:
				self.ButtonList[Id_scream].config 	(bg = "red",fg = "cyan")




		#if Case_color != 4:
		#	qnt_on = 0
		#	for item in  range (len(self.lista_rep)):
		#		if id_emp == self.lista_rep[item][1]:
		#			if self.lista_rep[item][7] == True:
		#				qnt_on = qnt_on + 1

		#	for item in  range (len(self.lista_emp)):
		#		if self.lista_emp[item][0] == id_emp:
		##			index_empp 	= item
		##			Id_scream 	= self.lista_emp[item][6]
		#			total_rep 	= self.lista_emp[item][8]
		#			break

			
		#	self.botaoContage[Id_scream].config (text= str(qnt_on)
		#								 + "/" + str(total_rep))

		#	Telas.GUI_Monitor.updateContage(index_empp,qnt_on)





	def updHora(self, emp_index):
		Id_scream 	= self.lista_emp[emp_index][6]
		hora 		= self.lista_emp[emp_index][7]

		self.MsgHora[Id_scream].config (text = hora)







