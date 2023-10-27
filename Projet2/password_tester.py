import string

def test_password_strength(password):
    while True:
        minuscule = any(c.islower() for c in password)
        majuscule = any(c.isupper() for c in password)
        chiffre = any(c.isdigit() for c in password)
        special = any(c in string.punctuation for c in password)

        critere_manquant = []
        if not minuscule:
            critere_manquant.append(" une minuscule")
        if not majuscule:
            critere_manquant.append("majuscule")
        if not chiffre:
            critere_manquant.append("chiffre")
        if not special:
            critere_manquant.append("caractère spécial")

        if len(password) < 8 or critere_manquant:
            message = "Le mot de passe ne respecte pas les critères :"
            if len(password) < 8:
                message += " Mot de passe trop court"
            if critere_manquant:
                message += " " + ", ".join(critere_manquant)
            print(message)
            password = input("Veuillez entrer un nouveau mot de passe : ")
        else:
            return "Mot de passe fort"



