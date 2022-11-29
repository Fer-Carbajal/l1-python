def tempsEnSeconde(temps):
    return ((temps[0]*24*60+temps[1]*60+temps[2])*60+temps[3])
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""


temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    min=seconde//60
    seconde%=60
    heures=min//60
    min%=60
    jours=heures//24
    heures%=24
    return(jours,heures,min,seconde)
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    
seconde =(100000)
print(secondeEnTemps(seconde))



#fonction auxiliaire ici
def afficheTemps(temps):
    affichePluriel(temps[0],"jour")
    affichePluriel(temps[1],"heure")
    affichePluriel(temps[2],"minute")
    affichePluriel(temps[3],"seconde")
    print ("\n")

def affichePluriel(val,mot):
    if val!=0:
        print (" ", val, mot, end="")
    if val>1:
        print ("s", end="")
    
afficheTemps((1,0,14,23))   


def demandeTemps():
    jour=int(input("Nombre de jours"))
    heure=int(input("Nombre de heures"))
    min=int(input("Nombre de minutes"))
    sec=int(input("Nombre de secondes"))
    while heure>23 or min>59 or sec>59:
        print ("Entrée mal formée, recommender")
        jour=int(input("Nb jours"))
        heure=int(input("Nb heures"))
        min=int(input("Nb minutes"))
        sec=int(input("Nb seconde"))
    return (jour,heure,min,sec)
afficheTemps(demandeTemps())

def sommeTemps(temps1,temps2):
    return secondeEnTemps(tempsEnSeconde(temps1)+tempsEnSeconde(temps2))
    
afficheTemps(sommeTemps((2,3,4,25),(5,22,57,1)))

def proportionTemps(temps,proportion): 
    return secondeEnTemps(int(tempsEnSeconde(temps)*proportion))
afficheTemps(proportionTemps(proportion=0.2, temps=(2,0,3,6)))

def tempsEnDate(temps):
    jour,heure,min,sec=temps
    annee=jour//365 +1970
    jour=jour%365
    return(annee,jour,heure,min,sec)

def afficheDate(date=-1):#valeur par defaut
    annee, jour,heure, min,sec=date
    print("Annee", annee, end="")
    afficheTemps((jour,heure,min,sec))

temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))
afficheDate()

import time
print (time.time()
print(time.gmtime(time.time())))



