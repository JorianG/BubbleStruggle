from tkinter import *
import time
import random
global root
global indice
indice = 0
root = Tk()
class jeu:
    '''
    La classe jeu permet de creer la fenetre dans laquelle on affichera les balles du jeu.
    Les balles presentes dans le jeu sont listees dans la liste self.balles.
    '''
    def __init__(self):
        self.Largeur = 800
        self.Hauteur = 600
        self.balles=[]
        
    def cree_fenetre(self):
        '''
        Cree la fenetre dans laquelle on veut afficher les balles
        In: self
        Out: cree un fenetre
        '''
        self.canvas=Canvas(root,width=self.Largeur,height=self.Hauteur,background="white")
        self.canvas.pack(side=LEFT, padx=5, pady=5)
        self.canvas.create_line(400,0,400,700)
    
    def __str__(self) -> str:
        x = ""
        for i in range (len(self.balles)):
            x+= " "
            x+= str(self.balles[i].taille)
        return x

        
class vecteur:
    '''
    La classe vecteur permet de garder en memoire le deplacement vertical et horizontal d'une balle.
    '''
    def __init__(self,x,y):
        self.deplacement_x=x
        self.deplacement_y=y       

class balle:
    '''
    Lorsqu'elle est cree, une balle a:
        une taille, correspondant a son rayon 
        une vitesse, de classe vecteur
        des coordonnees (postition x et y)
        une gravitee (constante)
    Lorsqu'une balle est cree, on ajoute celle-ci a la liste des balles faisant partie du jeu.
    La balle doit avoir des coordonnees comprises entre 50 et 790 pour x et entre 0 et 590 pour y.
    '''
    def __init__(self,taille, position_x, position_y,vitesse_x):
        assert position_x>=50 and position_x<=790 and position_y>0 and position_y<=590, "la balle n'est pas dans la fenetre"
        self.taille=taille
        self.vitesse=vecteur(vitesse_x,15)
        self.position_x=position_x
        self.position_y=position_y
        self.gravite= 10
        jeu.balles.append(self)
    
    def supprimer_balle(self,jeu):
        '''
        Supprime la balle de la liste des balles en jeu
        In: jeu
        Out: None
        '''
        if len(jeu.balles) != 0:    
            for i in range (len(jeu.balles)):
                if jeu.balles[i]==self:
                    jeu.balles.pop(i)
                    break

    def collision_harpon(self, jeu):
        '''
        Si la balle passe par la ligne du harpon (qui a été placé en 400), elle se divise en 2 balles 
        plus petites. Une de chaque cote du harpon et allant dans des directions opposées.
        Si la balle touche le harpon, la fonction renvoie True, sinon elle renvoie False
        In: jeu
        Out: boleen
        '''
        if ((self.position_x >= 400) and((self.position_x+self.vitesse.deplacement_x <= 400))or((self.position_x <= 400) and((self.position_x+self.vitesse.deplacement_x) >= 400) )):
            #la balle a touche le harpon
            if self.taille <= 5:
                #on la supprime si elle est trop petite
                print(self.taille)
                self.supprimer_balle(jeu)
            else: 
                #sinon, on la divise en 2
                #et on en place une de chaque cote du harpon
                balle(round(self.taille/2), 410, self.position_y,20)
                balle(round(self.taille/2), 390, self.position_y,-20)
                self.supprimer_balle(jeu)
            return True
        return False
            
    def calcul_nouvelle_position(self,jeu):
        """
        Modifie position_x et position_y apres avoir
        appliqué la nouvelle vitesse.
        
        """
        self.nouvelle_vitesse()
        if not(self.collision_harpon(jeu)):
            #si la balle ne touche pas le harpon, on la deplace
            self.position_x=self.position_x+self.vitesse.deplacement_x
            self.position_y=self.position_y+self.vitesse.deplacement_y

    def nouvelle_vitesse(self):
        """
        Calcule la nouvelle position de la balles en fonction de sa vitesse 
        et gere les collisions avec les murs 

        In: Self(posistion_x, position_y et le vecteur vitesse)
        Out: Change Self(posistion_x, position_y et le vecteur vitesse)
        """
        if (self.position_x <= 50 and self.vitesse.deplacement_x<0) or (self.position_x >= 790 and self.vitesse.deplacement_x>0):
            self.vitesse.deplacement_x = self.vitesse.deplacement_x * -1
        if self.position_y >= 590 and self.vitesse.deplacement_y>0 :
            self.vitesse.deplacement_y= (self.vitesse.deplacement_y+10) * -1
        x = self.vitesse.deplacement_x 
        y = self.vitesse.deplacement_y + self.gravite
        #dessine la trajectoire des balles 
        # jeu.canvas.create_line(self.position_x,self.position_y,self.position_x+self.vitesse.deplacement_x,self.position_y+self.vitesse.deplacement_y+self.gravite)
        self.afficher_balle
        self.vitesse.deplacement_x=x
        self.vitesse.deplacement_y=y

    def afficher_balle(self,jeu):
        """
        Ajoute l'objet balle de rayon self.taille aux coor de self dans le canvas.

        In:self.taille, self. position_x , self.position_y
        Out: create_oval
        """
        for i in range(len(jeu.balles)):   
            r=jeu.balles[i].taille
            x,y = (jeu.balles[i]. position_x,jeu.balles[i].position_y)
            # hexadecimal = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
            jeu.canvas.create_oval(x-r,y-r,x+r,y+r,width=1, outline="red",fill="red")
           
        

#test 1:
    

jeu = jeu()
jeu.cree_fenetre()
bal1 = balle(15,750,300,30)

    #pour 20 tours:
x=20
for i in range(x):
    for item in jeu.balles:
        item.afficher_balle(jeu)
        item.calcul_nouvelle_position(jeu)
print("end")

    
#tests 2:
#ball=balle(15,900,300,30)
#ball=balle(15,-3,300,30)
#ball=balle(15,300,900,30)
#ball=balle(15,-3,300,30)

#test 3:
'''
jeu = jeu()
jeu.cree_fenetre()
#ball = balle(15,790,300,30)
#ball = balle(15,790,300,-30)
#ball = balle(15,50,300,30)
#ball = balle(15,50,300,-30)
#ball = balle(15,300,590,30)
for i in range(5):
    for item in jeu.balles:
        item.afficher_balle(jeu)
        item.calcul_nouvelle_position(jeu)
'''
root.mainloop()