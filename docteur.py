class Docteur():
   
    def __init__(self, w, h):
        self.x = int(w/2)
        self.y = int(h/2)
        self.symbole='W'
        self.vie=True
        self.peuBouger=True
        self.nbZappeur=0
        self.nbPoints=0
        
    def bouger(self, move):
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
        else:
            pass
            
        
    def zap(self, grille):
        for i in range(self.x-1, self.x+1):
            for j in range(self.y-1, self.y+1):
                if grille[i][j].symbole=='D':
                    grille[i][j].meurt
    
    def ajouteZap(self):
        self.nbZappeur+=1
        
    def teleporte(self, w, h, diff, grille):
       
        while True:
            x=random.randint(0,w)
            y=random.randit(0,h)
            
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