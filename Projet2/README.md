# Projet 2 - Générateur de Mots de Passe et Passphrases

Ce projet consiste en un programme simple qui offre les fonctionnalités suivantes :
1. Générer un mot de passe aléatoire.
2. Tester un mot de passe pour évaluer sa robustesse.
3. Générer une passphrase sécurisée.

## Comment ça fonctionne

Le programme interagit avec l'utilisateur pour accomplir ces trois tâches. Voici comment il gère différentes situations :

### Génération de Mot de Passe
- L'utilisateur peut spécifier la longueur souhaitée pour le mot de passe.
- Le programme vérifie si la longueur est cohérente (par exemple, supérieure à 0).
- Si la longueur est incorrecte, il demande à l'utilisateur de la revoir.
- Si la longueur est trop longue, il complète le mot de passe avec des caractères aléatoires pour atteindre la longueur souhaitée.

### Test de Mot de Passe
- L'utilisateur peut entrer un mot de passe pour évaluer sa sécurité.
- Le programme analyse la robustesse du mot de passe en utilisant certaines règles, telles que la longueur et la complexité des caractères.
- Il renvoie un commentaire sur la force du mot de passe, indiquant s'il est fort, moyen ou faible.

### Génération de Passphrase
- Le programme génère une passphrase, qui est généralement plus sécurisée qu'un simple mot de passe.
- Il demande à l'utilisateur de spécifier la longueur souhaitée pour la passphrase.
- Il s'assure que la longueur est cohérente et génère la passphrase en conséquence.

## Comment l'utiliser

Pour utiliser le programme, suivez les instructions qui s'affichent à l'écran. Le menu vous guidera à travers les trois fonctionnalités.