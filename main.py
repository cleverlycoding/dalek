import vue
from grille import Grille

class Partie:
	def __init__(self, parent, large, haut):
		self.parent = parent
		self.large = large
		self.haut = haut
		self.niveau = 0
		self.docteur = None
		self.daleks = None
		self.grid = Grille(large, haut)
		

class Jeu:
	def __init__(self, parent):
		self.parent = parent
		self.partie_active = None		

class Controleur:
	def __init__(self):
		self.modele = Jeu(self)
		self.vue = Vue(self)

if __name__ == '__main__':
	grille = Grille(10, 10)
	rep = ""
	vue.cls()
	while rep != "Q":		
		grille._print()
		rep = input("entrez qqch (Q pour quitter)")
		grille.move(rep)
		
		vue.cls()
