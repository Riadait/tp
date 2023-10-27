import password_generator
import password_tester
import passphrase_generator

def generer_mot_de_passe():
    mot_de_passe, entropie, force_mot_de_passe = password_generator.generer_mot_de_passe()
    print("Mot de passe généré :", mot_de_passe)
    print("Entropie du mot de passe (en bits) :", entropie)
    print ("Votre Force:", force_mot_de_passe)
    

def tester_mot_de_passe():
    while True:
        password_to_test = input("Veuillez entrer un mot de passe : ")
        strength = password_tester.test_password_strength(password_to_test)
        
        if strength == "Mot de passe fort":
            break
        else:
            critere_manquant = [criterion for criterion in ["minuscule", "majuscule", "chiffre", "caractère spécial"] if criterion not in strength]
            message = "Le mot de passe ne respecte pas les critères :"
            if len(password_to_test) < 8:
                critere_manquant.append(" Mot de passe trop court")
            if critere_manquant:
                message += " " + ", ".join(critere_manquant)
            print(message)

def generer_passphrase():
    generated_passphrase = passphrase_generator.generate_passphrase()
    print("Passphrase générée :", generated_passphrase)

def menu():
    while True:
        print("Menu:")
        print("1. Générer un mot de passe")
        print("2. Tester un mot de passe")
        print("3. Générer une passphrase")
        print("4. Quitter")
        choice = input("Veuillez choisir une option (1/2/3/4): ")
        
        if choice == "1":
            generer_mot_de_passe()
        elif choice == "2":
            tester_mot_de_passe()
        elif choice == "3":
            generer_passphrase()
        elif choice == "4":
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    menu()
