from docteur import Docteur
from daleks import Daleks

class Grille():

	def set(self, x, y, val):
		if x >= 0 and x <= self.w:
			if y >= 0 and y <= self.h:
				self._grid[x][y] = val


	def __init__(self, w, h):
		super(Grille, self).__init__()
		self.w = w
		self.h = h

		self._grid = [["*" for _ in range(w)] for _ in range(h)]
		self.nb_dalek = 5
		self.daleks = [Daleks() for i in range(self.nb_dalek)]
		for i in self.daleks:
			i.positionner(self)
			self._grid[i.x][i.y] = i.symbole


		self.docteur = Docteur(self.w, self.h)
		self._grid[self.docteur.x][self.docteur.y] = self.docteur.symbole
		#init dalek

	def _print(self):
		for row in self._grid:
			for i in row:
				print(i, end=' ')
			print()

	def get_pos(self, x, y):
		return self._grid[x][y]

	def move(self, rep):
		self._grid[self.docteur.y][self.docteur.x] = "*"
		self.docteur.bouger(rep)
		self._grid[self.docteur.y][self.docteur.x] = self.docteur.symbole

		for i in self.daleks:
			print(i.x, i.y, self.get_pos(i.x, i.y))
			self._grid[i.x][i.y] = "*"
			i.bouger(self)
			print(i.x, i.y, self.get_pos(i.x, i.y))
			self._grid[i.x][i.y] = i.symbole


	def get(self):
		return self._grid
