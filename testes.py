import threading
import sys
import time
from Front_inicia import main_front as FT
from back_inicia import main_back as BK

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



RT = Threads(target=FT)
RT.start()
time.sleep(5)
RT = Threads(target=BK)
RT.start()