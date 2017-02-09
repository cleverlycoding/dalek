import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Vue(object):
	"""docstring for Vue"""
	def __init__(self, parent):
		super(Vue, self).__init__()
		self.parent = parent

	def affiche_menu(self):
		pass

	def affiche_jeu(self, grille):
		pass

	def affiche_fin(self):
		pass
		