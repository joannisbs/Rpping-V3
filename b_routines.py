import socket
import os
import shutil
import threading
from conbecktofront import *
import copy

class StopThread(StopIteration):
	pass
threading.SystemExit = SystemExit, StopThread

class Threads(threading.Thread):
	def stop(self):
		self.__stop = True
		#Controle.db.close()


	def _bootstrap(self, stop_thread=False):
		
		
		self.__stop = False
		sys.settrace(self.__trace)
		super()._bootstrap()

	def __trace(self, frame, event, arg):
		if self.__stop:
			raise StopThread()
		return self.__trace



class ServiceTest:
	def __init__(self,list_emp,list_rep):
		self.list_rep = list_rep
		self.list_emp = list_emp
		lisrep = copy.copy(list_rep)
		self.StF = Soquet(lisrep)
		self.InitThread()
		

	def InitThread(self):
		self.Threads_emp = []
		qnt_emp = len(self.list_emp)
		for index_emp in range (qnt_emp):
			self.Threads_emp.append('')
			self.Threads_emp[index_emp] = Threads(target=self.TestaEmp,
									kwargs={'Emp_index':index_emp})

			self.Threads_emp[index_emp].start()

	def Stop(self):
		
		qnt_emp = len(self.Threads_emp)
		for index_emp in range (qnt_emp):
			self.Threads_emp.stop()

	def TestaEmp(self,Emp_index):
		id_emp 		= self.list_emp[Emp_index][0]
		Quant_Rep 	= len(self.list_rep)
		for rep in range (Quant_Rep):
			if self.list_rep[rep][1] == id_emp:
				ID_rep			= self.list_rep[rep][0]
				IP_rep			= self.list_rep[rep][3]
				Porta_rep		= self.list_rep[rep][4]
				self.StF.SendToFront(rep,ID_rep,4)
				resultado = self.TestaPorta(IP_rep,Porta_rep)
				self.StF.SendToFront(rep,ID_rep,resultado)
		self.TestaEmp(Emp_index)


	def TestaPorta(self,ip,port):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#print ip + " porta = " + port
		#print "Test Ping"
		if self.TestaPing(ip):
			#if Controle.Stop : return 5
			try:
				#if Controle.Stop : return 5
				s.connect((ip,int(port)))		
				s.close()
				return 3

			except:
				return 2

		else:
			return 1



	def TestaPing(self,ip):
		
		try:
			resposta = os.system("ping " + ip + " -c 2 -s 0 > /dev/null")
			if resposta == 0 :
				#print "ping ok"
				return True
			else:
				#print "Falha ping"
				return False	
		except:
			return False

