class Question:
    def __init__(self, question, options, réponse):
        self.question = question
        self.options = options
        self.réponse = réponse

    def correction(self, réponse_user):
        return réponse_user.lower() == self.réponse

# Liste de questions et réponses
questionnaire = [
    Question("Combien d'enfant a Son Goku ?", ["a) 1 ", "b) 2 ", "c) 3"], "b"),
    Question("Quel est le nom du premier personnage que Son Goku rencontre au début de Dragon Ball ?", ["a) Yamcha", "b) Krilin", "c) Bulma"], "c"),
    Question("Que fait Vegeta lors de l'affrontement de Bou petit avec Sangoku ? ?", ["a) Il laisse Sangoku affronter Bou petit", "b) Il se bat aux côtés de Goku", "c)Il se bat tout seul avec Bou Petit"], "a"),
    Question("Comment est détruit la Terre dans la saga Bou ?", ["a) Par l'énorme boule lancée par Vegeto ", "b) Par un Final Flash de Vegeta ", "c) Par une énorme boule de feu sortie de la main de Bou petit"], "c"),
    Question("Combien de fois la Lune a-t-elle été détruite ?", ["a) Une fois", "b) Deux fois", "c) Trois fois"], "b"),
    Question("Comment est ressuscité Sangoku pour la deuxième fois ?", ["a) Par les boules de cristal", "b) Grâce à la fusion avec Vegeta avec les boucles d'oreilles", "c) Par le sacrifice du grand maître des dieux"], "c"),
    Question("Qui tue Freezer ?", ["a) Goku", "b) Vegeta", "c) Trunks"], "c"),
    Question("Que fait le petit Sangohan lors de la pleine lune ?", ["a) rien", "b) il dort", "c) Il se transforme en gorille"], "c"),
    Question("Qui tue Nappa ?", ["a) Vegeta", "b) Goku", "c) Piccolo"], "a"),
    Question("Qui est Cell ?", ["a) Un Saiyan", "b) Un cyborg", "c) un alien"], "b"),
]
