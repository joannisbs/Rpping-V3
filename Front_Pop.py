from Tkinter import *
from VariaveisGlobais import * 
import ttk
from LeBanco import Mysqldb

def PopupRel(id_rep):

	def on_check_clik():
		Var.Lista.Relogios[id_rep][11] = True
		show.destroy()

		



	show = Tk()
	show.wm_title("Relogio")

	id_emp 			= Var.Lista.Relogios[id_rep][1]
	Name_rep		= Var.Lista.Relogios[id_rep][2]
	IP_rep			= Var.Lista.Relogios[id_rep][3]
	Porta_rep		= Var.Lista.Relogios[id_rep][4]
	Modelo_rep		= Var.Lista.Relogios[id_rep][5]
	Numero_rep		= Var.Lista.Relogios[id_rep][6]
	#Stado			= Var.Lista.Relogios[id_rep][7]
	#Hora			= Var.Lista.Relogios[id_rep][8]
	Quant_Empresas = len(Var.Lista.Empresas)
	for indexempresas in range (Quant_Empresas):
		if id_emp == Var.Lista.Empresas[indexempresas][0]:
			Index_emp = indexempresas
			break

	name_emp		= Var.Lista.Empresas[Index_emp][1]

	lable1 = Label(show, text = "Empresa: "  + name_emp)
	lable1.grid(row=0,pady=5,padx=20)

	lable1 = Label(show, text = "Unidade: "  + Name_rep)
	lable1.grid(row=1,pady=5,padx=20)

	lable = Label(show, text = "IP: " + IP_rep)
	lable.grid(row=2,pady=5,padx=20)

	#lable2 = Label(show, text = "Porta Testada: "  + Porta_rep)
	#lable2.grid(row=3,pady=5,padx=20)

	#lable3 = Label(show, text = "Numero do Rep: " + Numero_rep)
	#lable3.grid(row=4,pady=5,padx=20)
	var = IntVar()
	Checkbutton(show,text="Deseja abrir Popup ao ficar On-Line?",variable=var,command=on_check_clik).grid(row=5)


	botaos = Button(show, text="Ok", command=show.destroy)
	botaos.grid(row=6,pady=5,padx=20)

def PopupRep():

	def ok():

		name = var2.get()
		#print name

		for item in  range (len(Var.Lista.Relogios)):
			if Var.Lista.Relogios[item][2]==name:
				id_rep = Var.Lista.Relogios[item][0]
		

		Controle.db = Mysqldb()
		Controle.db.connect()
		Controle.db.get_history(id_rep)
		Controle.db.close()
		frame = Frame(show)
		frame.pack(pady=5)

		scroll = Scrollbar(frame)
		scroll.pack(side=RIGHT,fill=Y)
		listbox = Listbox(frame,width = 25)
		listbox.pack(side=LEFT,fill=Y)
		scroll.config(command=listbox.yview)
		listbox.config(yscrollcommand=scroll.set)

		for index in range (len(Var.Lista.History)):
			item = Var.Lista.History[index]
			date = item[3]
			print date
			dia = str(date[7:9])
			mes = str(date[4:6])
			ano = str(date[1:3])
			hora = str(date[10:15])

			if item[2] == 3:
				texto2 = ' Ficou On-Line!'
				cor = 'green'
			elif item[2] == 1:
				texto2 = ' Ficou Off-Line!'
				cor = 'red'
			else:
				texto2 = str(item[2])
			
			texto = (dia + '/' + mes +  '/' + ano + ' ' + hora + texto2)
			listbox.insert(END, texto)
			listbox.itemconfig(index, {'fg':cor})
			#l = Label(show, text= dia + '/' + mes +  '/' + ano )
			#l.pack(pady=5)

	def selct():
		name = var.get()
		listrep = []
		for item in  range (len(Var.Lista.Empresas)):
			if Var.Lista.Empresas[item][1]==name:
				ids =  Var.Lista.Empresas[item][0]

		for item in  range (len(Var.Lista.Relogios)):
			if Var.Lista.Relogios[item][1]==ids:
				listrep.append(Var.Lista.Relogios[item][2])
		botaos.config(state="disabled")
		option2.config(state="normal")

		option2['values']=listrep

	def selct2():
		name = var2.get()
		print name
		botaos.config(state="normal")

	show = Tk()
	show.wm_title("Historico Rep")

	var = StringVar(show)
	var.set('RP TESTE')
	var2 = StringVar(show)
	var2.set('RP TESTE')
	listemp = []
	for item in  range (len(Var.Lista.Empresas)):
		listemp.append(Var.Lista.Empresas[item][1])

	l = Label(show, text='Empresas:')
	l.pack(pady=5)

	option = ttk.Combobox( show,textvariable = var, values = listemp)
	option.bind("<<ComboboxSelected>>",lambda event:selct())
	option.pack(pady=5,padx = 15)

	l = Label(show, text='Rep:')
	l.pack(pady=5)

	option2 = ttk.Combobox( show,textvariable = var2, values = listemp,state="disabled")
	option2.bind("<<ComboboxSelected>>",lambda event:selct2())
	option2.pack(pady=5)

	botaos = Button(show, text="Ok", command=ok,state="disabled")
	botaos.pack()


