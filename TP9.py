# Soit un fichier typé intitulé concours.txt qui comporte les enregistrements relatifs aux candidats d’un concours. Chaque enregistrement
# est composé de : CIN, NOM, PRENOM, GROUPE, AGE et DECISION (type contenant les identificateurs suivants : admis, refusé, ajourné),
### et séparé par point-virgule (;). ###

##  Définir le module saisir() qui permet de remplir les données relatives aux candidats dans le fichier concours.txt ##

def saisir(): 
    new = "o"  # O -> oui ; N -> non
    fichier = open("concours.txt", "a")
    decision = {"a": "admis(e)", "r": "refuse(e)", "aj": "ajourne(e)"}

    while new == "o":
        cin = input("Saisir le Numero CIN : ")
        nom = input("Saisir le Nom : ")
        prenom = input("Saisir le prenom : ")
        age = input("saisir l age ")
        dec = input("saisir la decision a(admis(e)) r(refuse(e)) aj(ajourne(e)): ")
        ligne = cin+";"+nom+";"+prenom+";"+age+";"+decision[dec]+"\n"

    fichier.write(ligne)
    new = input("Saisir un nouveau candidat, (O / N) ?")
    fichier.close()

## Définir la fonction admis() qui permet de créer le fichier admis.txt comportant les données relatives aux candidat admis ##

def admis():
    fichier = open("concours.txt", "r")
    dest = open("admis.txt", "w")

    for ligne in fichier:
        L = ligne.split(";")
        if L[4].strip() == "admis(e)":
            dest.write(ligne)

    fichier.close()
    dest.close()

# Afin de sélectionner en priorité les candidats admis et âgés moins de 30 ans, créer le module attente() qui produira à partir du
# fichier admis.txt, un nouveau fichier intitulé attente.txt comportant les données relatives aux candidats admis et âgés de plus de 30
## ans. Une ligne du fichier attente.txt comprend le CIN, le NOM et PRENOM d’un candidat séparés par point-virgule (;). ##


def attente():
    fichier = open("admis.txt", "r")
    dest = open("attente.txt", "a")

    for ligne in fichier:
        L = ligne.split(";")
        if int(L[3]) > 30:
            enreg = L[0]+";"+L[1]+";"+L[2]+"\n"
        dest.write(enreg+"\n")

    fichier.close()
    dest.close()

# Définir le module statistiques(dec) qui permet de retourner le pourcentage des candidats pour la décision dec (admis, refusé et
# ajourné).
# Exemple : Le pourcentage des candidats :
## admis = (Nombre des candidats admis / Nombre des candidats) *100 ##


def statistiques(dec):
    fichier = open("concours.txt", "r")

    L = fichier.readlines()
    fichier.close()

    L1 = []  # candidats admis
    L2 = []  # candidats refuses
    L3 = []  # candidats ajournes

    for ligne in L:
        L = ligne.split(";")
        if L[4].strip() == "admis(e)":
            L1.append(ligne)
        elif L[4].strip() == "refuse(e)":
            L2.append(ligne)
        else:
            L3.append(ligne)

    if dec == "admis":
        return (len(L1)/len(L))*100
    elif dec == "refuse":
        return (len(L2)/len(L))*100
    else:
        return (len(L3)/len(L))*100

##  Définir le module supprimer() qui supprimera du fichier admis.txt les candidat âgés plus que 30 ##


def supprimer():
    fichier = open("admis.txt", "r")
    candidat = []  # contient les candidats restants

    for ligne in fichier:
        L = ligne.split(";")
        if int(L[3]) < 30:
            candidat.append(ligne)
    fichier.close()

# reecrire la nouvelle liste
    fichier = open("admis.txt", "w")
    fichier.writelines(candidat)
    fichier.close()
