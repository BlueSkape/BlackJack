from guiBlackJack import GUIblackjack
from random import shuffle
from time import sleep

class jeu_de_carte:
    def __init__(self):
        c = [(nbre, '♥') for nbre in range(1, 14)]
        t = [(nbre, '♣') for nbre in range(1, 14)]
        k = [(nbre, '♦') for nbre in range(1, 14)]
        p = [(nbre, '♠') for nbre in range(1, 14)]
        self.paquet = c + t + k + p

    def melange_carte(self):
        shuffle(self.paquet)

    def pioche_carte(self):
        return self.paquet.pop()
    
paquet = jeu_de_carte()

paquet.melange_carte()

class BlackjackGame:
    def __init__(self):
        self.paquet = jeu_de_carte()
        self.paquet.melange_carte()

        self.jeu = GUIblackjack()

        self.croupier = []
        self.joueur = []
        self.argentcroupier = 100
        self.argentjoueur = 100
        self.argentcentre = 0
       
    def tour_croupier(self):
        total_croupier = 0
        for carte in self.croupier:
            total_croupier += carte[0]

        while total_croupier < 17:
            carte_croupier = self.paquet.pioche_carte()
            self.croupier.append(carte_croupier)
            total_croupier += carte_croupier[0]
            sleep(0.5)
            self.jeu.refresh(self.croupier, self.joueur, t="", cacheCroupier=True)
            self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)

    def jeu_de_carte(self): # Permet de restart le jeu
        self.croupier = []
        self.joueur = []
        self.argentcentre = 0
        self.jeu.refresh(self.croupier, self.joueur,t = 'Bienvenue sur la table de BlackJack', cacheCroupier = True)
        sleep(1)

        self.jeu.refresh(self.croupier, self.joueur,t = 'Vous êtes prêt(e) ça va bientôt commencer', cacheCroupier = True)
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
        sleep(1)

        self.jeu.refresh(self.croupier, self.joueur,t = 'Mettez une mise de 5 au minimum', cacheCroupier = True)
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)

        click = self.jeu.waitClick()

        self.jeu.refresh(self.croupier, self.joueur,t = '', cacheCroupier = True)
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)

        click = None

        while click != '_E' :
            click = self.jeu.waitClick()
            
            if click == '_U' and self.argentjoueur > 0 :
                self.argentjoueur = self.argentjoueur - 5
                self.argentcentre = self.argentcentre + 5
                self.jeu.refresh(self.croupier, self.joueur,t = '', cacheCroupier = True)
                self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
            
            elif click == '_U' and self.argentjoueur == 0 :
                self.jeu.refresh(self.croupier, self.joueur,t = "Vous n'avez pas assez d'argent pour miser d'avantage", cacheCroupier = True)
                self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
            
            elif self.argentcentre == 0 and click == '_D':
                self.jeu.refresh(self.croupier, self.joueur,t = "Il n'y a pas de mise sur la table", cacheCroupier = True)
                self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
            
            elif self.argentcentre > 0 and click == '_D' :
                self.argentcentre = self.argentcentre - 5
                self.argentjoueur = self.argentjoueur + 5
                self.jeu.refresh(self.croupier, self.joueur,t = '', cacheCroupier = True)
                self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
                
        self.jeu.refresh(self.croupier, self.joueur,t = 'Distribution des cartes en cours...', cacheCroupier = True)
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
        sleep(1)

        self.joueur.append(paquet.pioche_carte())
        self.jeu.refresh(self.croupier, self.joueur,t = '', cacheCroupier = True)
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
        sleep(0.5)

        self.croupier.append(paquet.pioche_carte())
        self.jeu.refresh(self.croupier, self.joueur,t = '', cacheCroupier = True)
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
        sleep(0.5)

        self.joueur.append(paquet.pioche_carte())
        self.jeu.refresh(self.croupier, self.joueur,t = '', cacheCroupier = True)
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
        sleep(0.5)

        self.croupier.append(paquet.pioche_carte())
        self.jeu.refresh(self.croupier, self.joueur,t = '', cacheCroupier = True)
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
        sleep(0.5)

        self.argentcroupier = self.argentcroupier - self.argentcentre

        self.argentcentre = self.argentcentre + self.argentcentre

        self.jeu.refresh(self.croupier, self.joueur,t = '', cacheCroupier = True)

        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)

        self.totaljoueur = 0
        self.totalcroupier = 0

        cpt = 0 # compte la main du joueur
        cpt1 = 0 # compte la main du croupier

        for carte in self.joueur :
            cpt += carte[0]

        for carte1 in self.croupier:
            cpt1 += carte[0]
            
        self.jeu.refresh(self.croupier, self.joueur,t = "Pioche (o) ne pas prendre de carte (n)", cacheCroupier = True)
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)

        click = self.jeu.waitClick() 

        while click != 'n' and cpt < 21:
            if click == 'o' :
                carte = paquet.pioche_carte()
                self.joueur.append(carte)
                cpt += carte[0]
                sleep(0.5)
                self.jeu.refresh(self.croupier, self.joueur,t = "", cacheCroupier = True)
                self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
            click = self.jeu.waitClick()
        

        if cpt > 21:
            self.jeu.refresh(self.croupier, self.joueur, t="Restart ? (r)", cacheCroupier=True)
            self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
            self.jeu.messCentre("Game Over")
            click = self.jeu.waitClick()
            if click == 'r':
                self.jeu_de_carte()

        elif cpt == 21:
            self.jeu.refresh(self.croupier, self.joueur, t="Restart ? (r)", cacheCroupier=True)
            self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
            self.jeu.messCentre("Gagné(e)")
            click = self.jeu.waitClick()
            if click == 'r':
                self.jeu_de_carte()
               
        self.tour_croupier()
        self.verifier_gagnant()

if __name__ == "__main__":
    blackjack_game = BlackjackGame()
    blackjack_game.jeu_de_carte()
