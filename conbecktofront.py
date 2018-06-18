from f_log import LogManager as Lg
from f_gettime import Telas

class Soquet:
	def __init__ (self,list_rep):
		self.list_rep = list_rep
		for qnt in range (len(list_rep)):
			self.list_rep[qnt][5] = 7

	def SendToFront(self,rep,ids,stat):
		#print rep, stat
		Telas.Rep[0].update(rep,stat)
		Telas.Rep[1].update(rep,stat)
		if stat != 4:
			self.insert(rep,stat,ids)

	def insert(self,rep,value,ids):
		if self.list_rep[rep][5] != value and self.list_rep[rep][5] != 7:
			self.list_rep[rep][5]=value
			print ids, value

		self.list_rep[rep][5]=value

	def isnertdb(self, eds, value):
		pass