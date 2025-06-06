def demander_reponse_numerique_utilisateur(min,max):
    while True:
        reponse_str = input(f"Votre réponse (entre {min} et {max}) : ")
        try:
            reponse_int = int(reponse_str)
        except:
            print("Erreur! Veuillez rentrer un chiffre svp")
        else:
            if reponse_int < min or reponse_int > max:
                print(f"Veuillez entrer un nombre entre {min} et {max}")
            else:
                return reponse_int

def poser_question(question):
    choix = question[1]
    bonne_reponse = question[2]
    print(f"QUESTION:\n")
    print("  " + question[0])
    for i in range(len(choix)):
        print(f"  {i+1})", choix[i])
    print()
    resultat_reponse_correcte = False
    reponse = demander_reponse_numerique_utilisateur(1, len(choix))
    if choix[reponse - 1].lower() == bonne_reponse.lower():
        print("Bonne réponse")
        resultat_reponse_correcte = True
    else:
        print("Mauvaise réponse")
    print()
    return resultat_reponse_correcte

def lancer_questionnaire(questionnaire):
    score = 0
    for i, question in enumerate(questionnaire):  
        print(f"Question {i+1}/{len(questionnaire)}")
        print("score:", score)
        if poser_question(question):
            score += 1
    print("Score final : " + str(score) + "/" + str(len(questionnaire)))

questionnaire = [
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"),
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    ("Quelle est la capitale du Japon ?", ("Yokohama", "Osaka", "Kyoto", "Tokyo"), "Tokyo"),
    ("Quelle est la capitale de l'Allemagne ?", ("Dublin", "Munich", "Berlin", "Cologne", "Hambourg"), "Berlin"),
]

lancer_questionnaire(questionnaire)