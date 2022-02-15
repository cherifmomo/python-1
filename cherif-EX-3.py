from random import randrange

jeu = []
for c in ["pique", "coeur", "trèfle", "carreau"]:
    for v in range(7, 14):
        carte = (v, c)
        jeu.append(carte)


def tirage():
    rangA = randrange(len(jeu))
    playerA = jeu[rangA]
    jeu.pop(rangA)
    playerB = jeu[randrange(len(jeu))]

    print('Le joueur A a tiré la carte : ', playerA[0], ' de ', playerA[1])
    print('Le joueur B a tiré la carte : ', playerB[0], ' de ', playerB[1])
    print('\n')
    if playerA[0] > playerB[0]:
        print("Le joueur A a gagné")
    elif playerA[0] == playerB[0]:
        print("Bataille")
    else:
        print("Le joueur B a gagné")


tirage()
