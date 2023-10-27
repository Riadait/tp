import random

def generate_passphrase():
    with open("C:/Users/riri9/tp1/Projet2/mot.txt", "r", encoding="utf-8") as file:
        mots = file.read().splitlines()
    
    mots_choisis = random.sample(mots, 6)
    passphrase = "_".join(mots_choisis)
    return passphrase
