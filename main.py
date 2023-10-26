from qcm import QCM

if __name__ == "__main__":
    from questions import questionnaire

    qcm = QCM(questionnaire)
    qcm.début()
    qcm.votre_score()
