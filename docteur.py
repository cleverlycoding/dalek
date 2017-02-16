import random
from pion import Pion

class Docteur(Pion):

    def __init__(self, w, h):
        self.x = int(w/2)
        self.y = int(h/2)
        self.symbole = 'W'
        self.vie = True
        self.peut_bouger = True
        self.nb_zappeur = 2
        self.nb_points = 0
        self.pos_initiale = None
        self.pos_finale = None

    def bouger(self, move, grille, w, h):
        self.pos_initiale = [self.x, self.y]
        if move == 'N':
            self.y -= 1
        elif move == 'S':
            self.y += 1
        elif move == 'E':
            self.x += 1
        elif move == 'O':
            self.x -= 1
        elif move == "NE":
            self.x += 1
            self.y -= 1
        elif move == "NO":
            self.x -= 1
            self.y -= 1
        elif move == "SE":
            self.x += 1
            self.y += 1
        elif move == "SO":
            self.x -= 1
            self.y += 1
        elif move == "T":
            self.teleporte(w, h, "E", grille)
        elif move == "Z":
            self.zap(grille)
        else:
            pass
        self.pos_finale = [self.x, self.y]


    def zap(self, grille):
        if self.nb_zappeur > 0:
            for i in range(self.x-1, self.x+1):
                for j in range(self.y-1, self.y+1):
                    if grille[i][j].symbole == 'D':
                        grille[i][j].meurt()
            self.nb_zappeur -= 1

    def ajouteZap(self):
        self.nb_zappeur += 1

    def teleporte(self, w, h, diff, grille):

        while True:
            x = random.randint(0, w)
            y = random.randint(0, h)

            if diff == 'E':
                nb_daleks = 0
                if grille[x][y].symbole != 'F':
                    for i in range(x-2, x+2):
                        for j in range(y-2, y+2):
                            if grille[i][j].symbole == 'D':
                                nb_daleks += 1
                                if nb_daleks == 0:
                                    self.x = x
                                    self.y = y
                                    break

            elif diff == 'O':
                if grille[x][y].symbole != 'D':
                    if grille[x][y].symbole != 'F':
                        self.x = x
                        self.y = y
                        break

            else:
                if grille[x][y].symbole != 'F':
                    self.x = x
                    self.y = y
                    break


    def meurt(self):
        self.vie = False
        self.peut_bouger = False
        