import random

class Docteur():
   
    def __init__(self, w, h):
        self.x = int(w/2)
        self.y = int(h/2)
        self.symbole='W'
        self.vie=True
        self.peuBouger=True
        self.nbZappeur=2
        self.nbPoints=0
        self.posiInit=None
        self.posiFinal=None
        
    def bouger(self, move, grille, w, h):
        self.posiInit = [self.x, self.y]
        if move=='N':
            self.y-=1
        elif move=='S':
            self.y+=1
        elif move=='E':
            self.x+=1
        elif move=='O':
            self.x-=1
        elif move=="NE":
            self.x+=1
            self.y-=1
        elif move=="NO":
            self.x-=1
            self.y-=1
        elif move=="SE":
            self.x+=1
            self.y+=1
        elif move=="SO":
            self.x-=1
            self.y+=1
        elif move=="T":
            self.teleporte(w, h, "E", grille)
        elif move=="Z":
            self.zap(grille)
        else:
            pass
        self.posiFinal = [self.x, self.y]
            
        
    def zap(self, grille):
        if self.nbZappeur > 0:
            for i in range(self.x-1, self.x+1):
                for j in range(self.y-1, self.y+1):
                    if grille[i][j].symbole=='D':
                        grille[i][j].meurt
        nbZappeur -=1				
    
    def ajouteZap(self):
        self.nbZappeur+=1
        
    def teleporte(self, w, h, diff, grille):
       
        while True:
            x=random.randint(0,w)
            y=random.randint(0,h)
            
            if diff=='E':
                nbDaleks = 0
                if grille[x][y].symbole!='F':
                    for i in range(x-2, x+2):
                        for j in range(y-2, y+2):
                            if grille[i][j].symbole=='D':
                                nbDaleks+=1
                                if nbDaleks == 0:
                                    self.x=x
                                    self.y=y
                                    break
                        
            
            elif diff=='O':
                if grille[x][y].symbole!='D':
                    if grille[x][y].symbole!='F':
                        self.x=x
                        self.y=y
                        break
                
            else:
                if grille[x][y].symbole!='F':
                    self.x=x
                    self.y=y
                    break
    
        
    def meurt(self):
        self.vie=False
        self.peuBouger=False