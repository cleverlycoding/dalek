import random
class Daleks():
    
    def __init__(self):
        self.symbole='D'
        self.vie=True
        self.peuBouger=True  
    
    def meurt(self):
        self.vie=False
        self.peuBouger=False
        self.symbole='F'
        
    def positionner(self, grille):
        while True:
            x=random.randint(0, grille.w - 1)
            y=random.randint(0, grille.h - 1)
            if grille.get_pos(x, y) != "W":
                if grille.get_pos(x, y) != "D":
                    self.x=x
                    self.y=y
                    break
        
    def bouger(self, grille):
        for i in range(0, grille.w - 1):
            for j in range(0, grille.h - 1):
                if grille.get_pos(i, j) == "W":
                    if i > self.x:
                        self.x+=1
                    elif i == self.x:
                        pass
                    else:
                        self.x-=1
                        
                    if j > self.y:
                        self.y+=1
                    elif j == self.y:
                        pass
                    else:
                        self.y-=1
                    if self.y > grille.h-1:
                        self.y = grille.h-1
                    if self.y < 0:
                        self.y = 0
                    if self.x > grille.w-1:
                        self.x = grille.w-1
                    if self.x < 0:
                        self.x = 0
