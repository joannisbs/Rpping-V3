################################################################################
#                                                                              #   
#   Este codigo foi desenvolvido por Joannis Basile em 8/06/2018               #
#   destinado ao sistema de monitoramento dos modulos da RealPonto             #
#                                                                              #
#   Esta classe retorna todos os formatos de data,                             #
#   facilitando assim a utilizacao de data em varios formatos                  #
#                                                                              #
################################################################################

from datetime import datetime


class GetTime(object):
	
	def __init__(self):
		now = datetime.now()
		self.hora 		= 	now.hour
		self.minuto	 	= 	now.minute
		self.segundo 	=   now.second
		self.day		=	now.day
		self.mes		=	now.month
		self.year		=	now.year

	def get_hour_minute(self):
		
		horaminuto = 	(str(self.hora).zfill(2) +":"+ 
						str(self.minuto).zfill(2) ) 
						
		return horaminuto

	def get_just_minute(self):
		
		time = str(self.minuto).zfill(2)			
		return time

	def get_just_hour(self):
		
		time = str(self.hora).zfill(2)			
		return time

	def get_just_second(self):
		
		time = str(self.segundo).zfill(2)			
		return time

	def get_full_1(self):
		# return YYYY_MM_DD-HH-MM
		date = (str(self.year).zfill(4)+"_"+
				str(self.mes).zfill(2)+"_"+
				str(self.day).zfill(2)+"-"+
				str(self.hora).zfill(2)+"-"+
				str(self.minuto).zfill(2))
		return date

	def get_full_db(self):
		#[18_06_04]10h12
		date = ("["+str(self.year)[2]+
					str(self.year)[3]+"_"+
				str(self.mes).zfill(2)+"_"+
				str(self.day).zfill(2)+"]"+
				str(self.hora).zfill(2)+"h"+
				str(self.minuto).zfill(2))
		return date



	def get_simple_semifull(self):
		#DD/MM-HH:MM
		date = (str(self.day).zfill(2)+"/"+
				str(self.mes).zfill(2)+"-"+
				str(self.hora).zfill(2)+":"+
				str(self.minuto).zfill(2))
		return date

class Telas:
	Rep = ['','']