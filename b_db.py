################################################################################
#                                                                              #   
#   Este codigo foi desenvolvido por Joannis Basile em 8/06/2018               #
#   destinado ao sistema de monitoramento dos modulos da RealPonto             #
#                                                                              #
#   esta classe e responsavel por trabalhar com o banco de dados               #
#   executando as funcoes simples de envios de querys ao mysql                 #
#                                                                              #
################################################################################

import mysql.connector

from f_gettime import GetTime as GTime
from f_log import LogManager as Lg


class Mysqldb:
	def __init__(self,bol_log):
		self.bol_log = bol_log
		
		if bol_log:
			t 				= GTime()
			log_name 		= "Log_DB.txt"
			self.log = Lg(log_name)


		self.CheckConfigFile()

	def CheckConfigFile(self): 
		arq 		= open("db.config","r")
		text 		= arq.readlines()
		line 		= text[0].split(":")
		self.host	= str(line[1])
		line 		= text[1].split(":")
		self.user	= str(line[1])
		line 		= text[2].split(":")
		self.pasw	= str(line[1])
		line 		= text[3].split(":")
		self.dbs	= str(line[1])
		


	def connect(self):

		try:
			
			db = mysql.connector.connect(	host 		= self.host,	
											user		= self.user,
											password	= self.pasw,
											db 			= self.dbs)


			
			self.connection = db
			self.cursor = db.cursor()


			if self.bol_log:
				tme	 = GTime()
				date = tme.get_full_1()
				msg  = ("connection has been established with successful at " 
					+ date + " in " + self.dbs +" \n")
				self.log.insert(msg)

		except:
			if self.bol_log:
				tme	 = GTime()
				date = tme.get_full_1()
				msg  = "Error conection with db at " + date + " in " + self.dbs + " \n"
				self.log.insert(msg)

	def close(self):
		self.cursor.close()
		self.connection.close()
		
		if self.bol_log:
			tme	 = GTime()
			date = tme.get_full_1()
			msg  = "Db connection has been closed at " + date +" \n"
			self.log.insert(msg)

	def GuetList(self,tbl):
		list_db = []
		
		if tbl == 'tbl_rep':
			tbl = tbl + " ORDER BY name_rep"

		query = ("SELECT * FROM " + tbl)

		
		try: 
			self.cursor.execute(query)
			logmsg = "Query execution was successfully executed:\n   ---> " + query + " << "
		except:
			logmsg = "Error in query execution:\n   ---> " + query + " << "


		if self.bol_log:
			tme	 = GTime()
			date = tme.get_full_1()
			msg  = logmsg + date +" \n"
			self.log.insert(msg)


		for row in self.cursor.fetchall():
			row = list(row)
			list_db.append(row)
			
		return list_db
			
		