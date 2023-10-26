import random
from questions import Question

class QCM:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def début(self):
        random.shuffle(self.questions)
        for i, question in enumerate(self.questions):
            print(f"Question {i + 1}: {question.question}")
            for option in question.options:
                print(option)
            réponse_user = input("Votre réponse (a/b/c) : ")
            while réponse_user.lower() not in ['a', 'b', 'c']:
                print("Réponse invalide. Veuillez choisir une réponse entre a, b ou c.")
                réponse_user = input("Votre réponse (a/b/c) : ")
            if question.correction(réponse_user):
                print("Bonne réponse!\n")
                self.score += 1
            else:
                print(f"Mauvaise réponse. La réponse correcte était {question.réponse}.\n")
            
    def votre_score(self):
        print(f"Votre score final est de {self.score}/{len(self.questions)}")


