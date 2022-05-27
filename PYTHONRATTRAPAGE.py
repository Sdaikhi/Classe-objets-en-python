#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Point3d:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
         ###pas compris###


# In[3]:


#Question 2

class Rectangle:
    def __init__(self,longueur,largeur):
        self.longueur = longueur
        self.largeur = largeur
        
    # périmètre
    def Perimetre(self):
        return 2*(self.longueur + self.largeur)
    
    # air
    def Surface(self):
        return self.longueur*self.largeur


# Instanciation : création d'un objet rectangle   
mRectangle = Rectangle(3, 4)


print("Le périmètre du rectangle est : ",mRectangle.Perimetre())
print("L'air du rectangle est : ", mRectangle.Surface())


# In[16]:


#Question 4

class CompteBancaire:
    def __init__(self, idNumber, nomPrenom, solde):
        self.idNumber = idNumber
        self.nomPrenom = nomPrenom
        self.solde = solde
        
    def versement(self, argent):
        self.solde = self.solde + argent
    
    def retrait(self, argent):
        if(self.solde < argent):
            print(" Impossible d'effectuer l'opération. Solde insuffisant !")
        else:
            self.solde = self.solde - argent
    
    def afficher(self):
        print("Compte numéro : " , self.idNumber)
        print("Nom & Prénom : ", self.nomPrenom)
        print("Solde  : ", self.solde , " EUR ")
        print("Sauf erreur ou omisssion ! ")
        
monCompte = CompteBancaire(16168891, " Karim Benzema", 10000)
monCompte.versement(10000)
monCompte.retrait(3000)
monCompte.afficher()


# In[20]:


#Question 3

from math import *
class Cercle:
    def __init__(self,a,b,r):
        self.a = 3
        self.b = 7
        self.r = 8
    
    def perimetre(self):
        return 2*pi*self.r
       
        
    def surface(self):
        return pi*self.r**2

    def formEquation(self,x,y):      
        return (x-self.a)**2 + (y-self.b)**2 -self.r**2
    def test_appartenance(self,x,y):
        if(self.formEquation(x,y)==0):
            print("le point : (",x,y,") appartient au cercle C")
        else:
            print("le point : (",x,y,") n'appartient pas au cercle C")
            
        
   
C = Cercle(1,2,1)

print("le périmètre du cercle C est  : ", C.perimetre())
print("le surface du cercle C est  : ", C.surface())
C.test_appartenance(1,1)
    


# In[ ]:





# In[ ]:




