import random
import string
import math

def calculer_entropie(longueur, num_minuscules, num_majuscules, num_chiffres, num_speciaux):
    caractere_total = num_minuscules + num_majuscules + num_chiffres + num_speciaux
    alphabet_total = 26 + 26 + 10 + len(string.punctuation)
    
    if caractere_total == 0:
        return 0  # Éviter la division par zéro
    
    entropie = longueur * math.log(alphabet_total, 2) - caractere_total * math.log(caractere_total, 2)
    
    return entropie

def generer_mot_de_passe():
    num_minuscules = 0
    num_majuscules = 0
    num_chiffres = 0
    num_speciaux = 0

    while True:
        try:
            num_minuscules = int(input("Nombre de minuscules : "))
            num_majuscules = int(input("Nombre de majuscules : "))
            num_chiffres = int(input("Nombre de chiffres : "))
            num_speciaux = int(input("Nombre de caractères spéciaux : "))
            break
        except ValueError:
            print("Veuillez entrer un nombre valide (composé uniquement de chiffres).")

    total_caracteres = num_minuscules + num_majuscules + num_chiffres + num_speciaux

    while True:
        longueur = int(input("Longueur du mot de passe : "))
        if longueur < total_caracteres:
            print("La longueur du mot de passe doit être supérieure ou égale au nombre total de caractères.")
        else:
            break

    caracteres = ''.join(random.choice(string.ascii_lowercase) for _ in range(num_minuscules))
    caracteres += ''.join(random.choice(string.ascii_uppercase) for _ in range(num_majuscules))
    caracteres += ''.join(random.choice(string.digits) for _ in range(num_chiffres))
    caracteres += ''.join(random.choice(string.punctuation) for _ in range(num_speciaux))

    if longueur > len(caracteres):
        caracteres += ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(longueur - len(caracteres)))

    mot_de_passe_liste = list(caracteres)
    random.shuffle(mot_de_passe_liste)
    mot_de_passe = ''.join(mot_de_passe_liste)

    entropie = calculer_entropie(longueur, num_minuscules, num_majuscules, num_chiffres, num_speciaux)

    force_mot_de_passe = "faible"
    if entropie >= 56:
        force_mot_de_passe = "fort"
    elif entropie >= 36:
        force_mot_de_passe = "moyen"

    return mot_de_passe, entropie, force_mot_de_passe
