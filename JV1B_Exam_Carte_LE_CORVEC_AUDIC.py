class Carte:
    def __init__(self,cout_mana = 0,name="",description = ""):
        self.__mana = cout_mana
        self.__nom = name
        self.__descrip = description

    def getValeur_Mana(self):
        return self.__mana
    
    def getName(self):
        return self.__nom
    
    def getDescription(self):
        return self.__descrip
    
class Mage:
    def __init__(self,name,point_vie ,total_mana ,cout_mana,defausse,main = [],zone_de_jeu = [] ):
        self.__nom = name
        self.__pv = point_vie
        self.__tt_mana = total_mana
        self.__mana = cout_mana
        self.__defausse = defausse
        self.__main = main
        self.__zone_jeu = zone_de_jeu

    def getName(self):
        return self.__nom
    
    def getPv(self):
        return self.__pv
    
    def getTotalMana(self):
        return self.__tt_mana
    
    def getMana_Mage(self):
        return self.__mana
    
    def getDefausse(self):
        return self.__defausse
    
    def getMain(self):
        return self.__main
    
    def getZone_Jeu(self):
        return self.__zone_jeu
    

    def Joue_carte(self,carte):
        for i in range(len(self.__main)):
            self.__main[i]== carte
            self.__main.insert(self.__zone_jeu,carte)
            self.__main.pop(1)
            self.__mana -= carte.self.__mana


#Ce que j ai compris sur le procédé de récupération de mana :si le Mage n°2 passe son tour alors le mage n°1 gagne des point de mana sinon rien ?
#Vu que je n'ai surment pas compris j'ai juste créé une méthode sui permete de recupérer ces points de mana.
    def recup_pv(self):
        self.__mana += self.__tt_mana

    def attaque(self,atk):
        self.__pv-= self.__atk


class Cristal (Carte):

    def __init__(self,cout_mana = 0,name="",description = "",valeur_cristal = 0):
        super().__init__(cout_mana = 0,name="",description = "")
        self.__valeur_cri = valeur_cristal

    def getValeurCristal(self):
        return self.__valeur_cri

class Creature (Carte):

    def __init__(self,cout_mana = 0,name="",description = "",point_vie = 0, score_attaque = 0 ):
        super().__init__(cout_mana = 0,name="",description = "")
        self.__pv_creature = point_vie
        self.__atk = score_attaque

    def getPvCreature(self):
        return self.__pv_creature
    
    def getAttaque(self):
        return self.__atk
    
    def Attaque_Creature(self,mage):
        mage.self.__pv -= self.__atk
        return mage._self.__pv
    

    def mort_Creature(self):
        if self.__pv_creature <= 0:
            return True 
        return False

class Blast (Carte):

    def __init__(self,cout_mana = 0,name="",description = "",valeur_blast = 0):
        super().__init__(cout_mana = 0,name="",description = "")
        self.__valeur_blast = valeur_blast


    def getValeur(self):
        return self.__valeur_blast


#cree une ce qu'il y a dans la claase Carte

mage1 = Mage("Merlin",100,50,0,[],["Blast1","Ogre" ,"Cristal1"],[])
mage2 = Mage("Perlapinpin",100,50,0,[],["Blast2","Dragon" ,"Cristal2"],[])

cristal1 = Cristal(2,"Cristal1","Peut être jouée (ce qui la place sur la zone de jeu du joueur) en payant son coût de mana, auquel cas elle reste dans la zone de jeu. Peut attaquer un-e Mage ou une autre Creature, auquel cas cettedernière l’attaque ensuite en retour. Peut perdre des points de vie, et même mourir : ellepasse alors de la zone de jeu à la défausse.",5)
cristal2 = Cristal(2,"Cristal1","Peut être jouée (ce qui la place sur la zone de jeu du joueur) en payant son coût de mana, auquel cas elle reste dans la zone de jeu. Peut attaquer un-e Mage ou une autre Creature, auquel cas cettedernière l’attaque ensuite en retour. Peut perdre des points de vie, et même mourir : ellepasse alors de la zone de jeu à la défausse.",5)

creature1 = Creature (10,"Ogre","Peut attaquer un-e Mage ou une autre Creature, peut perdre des points de vie, et même mourir",10,15 )
creature2 = Creature (10,"Dragon","Peut attaquer un-e Mage ou une autre Creature, peut perdre des points de vie, et même mourir",10,15 )

blast1 = Blast(3,"Blast1","Un Blast peut être lancé contre uneCreature ou un Mage, ce qui lui enlève un nombre de points de vie égal à sa valeur. UnBlast est défaussé une fois qu’il a été joué",50)
blast2 = Blast(3,"Blast1","Un Blast peut être lancé contre uneCreature ou un Mage, ce qui lui enlève un nombre de points de vie égal à sa valeur. UnBlast est défaussé une fois qu’il a été joué",50)



#Si la créature est morte alors on la defausse
if Creature.mort_Creature == True:
     Mage.getZone_Jeu -= Creature
     Mage.getDefausse += Creature 


#Quand Mage joue Cristal son mana augmente de la valeur du Cristal
if Mage.Joue_carte(Cristal): 
    Mage.getZone_Jeu += Cristal
    Mage.getMana_Mage += Cristal.getValeur_Mana


#Quand Mage joue BLaste, enlève un nombre de points de vie égal à sa valeur d'une' Creature ou d'un Mage,  . Un Blast est défaussé une fois qu’il a été joué.

if mage2.Joue_carte("Blast1"): 
    mage2.getPv -= blast1.getValeur
    creature2.getPvCreature -= blast1.getValeur
    mage1.getDefausse -= creature1

if mage2.Joue_carte("Blast2"): 
    mage1.getPv -= blast2.getValeur
    creature1.getPvCreature -= blast2.getValeur
    mage2.getDefausse -= creature2









    
