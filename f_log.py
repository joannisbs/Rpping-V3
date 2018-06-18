################################################################################
#                                                                              #   
#   Este codigo foi desenvolvido por Joannis Basile em 8/06/2018               #
#   destinado ao sistema de monitoramento dos modulos da RealPonto             #
#                                                                              #
#   esta classe e responsavel por trabalhar com os logs do sistema             #
#   executando as funcoes simples de forma que facilite as interacoes          #
#                                                                              #
################################################################################




class LogManager:
	def __init__(self,name):	
		self.name = name
	def insert(self,msg):
		log = open(self.name,"ab+")
		log.write(msg)
		log.close()