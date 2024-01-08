# Importation des libraries
from guiBlackJack import GUIblackjack # c'est quand même le plus important
from random import shuffle # Ici nous permet juste d'importer shuffle pour mélanger nos cartes
from time import sleep # Alors la j'adore, permet de rajouter un temps entre chaque requête (très utile)

class jeu_de_carte:
    def __init__(self):
        c = [(nbre, '♥') for nbre in range(1, 14)] # Ici on a les cartes de coeur
        t = [(nbre, '♣') for nbre in range(1, 14)] # Ici on a les cartes de treffle
        k = [(nbre, '♦') for nbre in range(1, 14)] # Ici on a les cartes de carreau
        p = [(nbre, '♠') for nbre in range(1, 14)] # Ici on a les cartes de pique
        self.paquet = c + t + k + p

    def melange_carte(self):
        shuffle(self.paquet) # mélange aléatoirement les cartes

    def pioche_carte(self):
        return self.paquet.pop() # pioche une carte, rien de compliqué

paquet = jeu_de_carte() # crée une instance de la class jeu_de_carte
# Et voila comment est née notre paquet de carte, important pour la suite
paquet.melange_carte() # Oui bon, comme dis en haut

class BlackjackGame:
# Constructeur
    def __init__(self):
        self.paquet = jeu_de_carte()
        self.paquet.melange_carte()
        self.jeu = GUIblackjack() #Ca ca crée une instance de la classe GUIblackjack dans jeu, quand va bcp utilisé
        # Ici on initialise les listes pour les cartes du croupier et du joueur, vide évidemment
        self.croupier = []
        self.joueur = []
        # La on initialise l'argent du joueur, du croupier et celle au centre
        self.argentcroupier = 1000
        self.argentjoueur = 100
        self.argentcentre = 0
        # Ici on initialise les compteurs
        self.totaljoueur = 0 # compte la main du joueur
        self.totalcroupier = 0 # compte la main du croupier
        # Ajout de la variable as_valeur pour déterminer si l'AS vaut 1 ou 11
        self.as_valeur = 11
        self.jeu.messCentre('Le BlackJack') # Je l'ai mis ici comme ca il n'apparait que quand on lance le jeu
        # et pas quand on continue la partie
        sleep(2.5)
     
# Méthode pour continuer et encommencer sans réinitialiser les gains obtenu lors de la partie précédente
# En soit il sert à rien
# C'est juste histoire de l'avoir comme ca
    def continuer_partie(self):
        self.argent_joueur()
        self.argent_croupier()
        self.jeu_de_carte()

# Méthode pour quitter le jeu
    def quitter_jeu(self):
        exit() # Et oui exit, ca existe, j'étais trop heureux quand je l'ai découvert
        
# Méthode pour miser       
    def mise_joueur(self):
        self.argentjoueur -= 5 # -5 jetons au joueur
        self.argentcentre += 5 # et +5 au centre
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre) # Mise a jour de l'afficahfge des jetons

    def enlever_mise_joueur(self):
        self.argentcentre -= 5 # -5 jetons au centre
        self.argentjoueur += 5 # et +5 au joueur
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre) # Mise a jour de l'afficahfge des jetons

# Méthode pour restart le jeu, à 0, c'est à dire ne pas continuer mais recommencer le jeu
    def restart(self):
        # c'est juste le constructeur que j'ai repris
        # pour remmetre le jeu à 0
        self.croupier = []
        self.joueur = []
        self.argentcroupier = 1000
        self.argentjoueur = 100
        self.argentcentre = 0
        self.totaljoueur = 0 # compte la main du joueur
        self.totalcroupier = 0 # compte la main du croupier
        self.jeu.refresh(self.croupier, self.joueur, t="", cacheCroupier=False)
        sleep(1)
        self.jeu.refresh(self.croupier, self.joueur, t="Restarting ...", cacheCroupier=False)
        sleep(0.5)
        self.jeu.refresh(self.croupier, self.joueur, t="Restarting .", cacheCroupier=False)
        sleep(0.5)
        self.jeu.refresh(self.croupier, self.joueur, t="Restarting ..", cacheCroupier=False)
        sleep(0.5)
        self.jeu.refresh(self.croupier, self.joueur, t="Restarting ...", cacheCroupier=False)
        sleep(0.5)
        self.jeu.messCentre('Le BlackJack')
        sleep(2.5)
        self.jeu_de_carte()

# Le jeu de base
    def jeu_de_carte(self):
        self.croupier = []
        self.joueur = []
        self.argentcentre = 0
# Phrases de lancement (pas forcément utile, mais j'aime bien)
    # Oui je suis un gamin, ca sert a rien mais je trouve ca stylé
        self.jeu.refresh(self.croupier, self.joueur, t='Chargement.', cacheCroupier=True) 
        sleep(0.5)
        self.jeu.refresh(self.croupier, self.joueur, t='Chargement..', cacheCroupier=True)
        sleep(0.5)
        self.jeu.refresh(self.croupier, self.joueur, t='Chargement...', cacheCroupier=True)
        sleep(0.5)
        self.jeu.refresh(self.croupier, self.joueur, t='Chargement.', cacheCroupier=True)
        sleep(0.5)
        self.jeu.refresh(self.croupier, self.joueur, t='Chargement..', cacheCroupier=True)
        sleep(0.5)
        self.jeu.refresh(self.croupier, self.joueur, t='Chargement...', cacheCroupier=True)
        sleep(0.5)        
        self.jeu.refresh(self.croupier, self.joueur, t='Bienvenue sur la table de BlackJack', cacheCroupier=True)
        sleep(1)
        self.jeu.refresh(self.croupier, self.joueur, t='Vous êtes prêt(e) ça va bientôt commencer', cacheCroupier=True)
        sleep(1.5)
        self.jeu.refresh(self.croupier, self.joueur, t='Mettez une mise de 5 au minimum', cacheCroupier=True)
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
        sleep(1)
        self.jeu.refresh(self.croupier, self.joueur, t='Appuyez sur ↑, ou sur ↓ pour modifié la mise', cacheCroupier=True)
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
        sleep(1)
        
        click = self.jeu.waitClick()
        self.jeu.refresh(self.croupier, self.joueur, t='', cacheCroupier=True)
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
        # On l'utilise pour s'assurer que la variable a une valeur avant d'être utilisée dans la condition de la boucle.
        click = None
        
# Permet l'utilisation des touches 'UP' et 'Down' pour définir la mise 
        while click != '_E':
            click = self.jeu.waitClick() # ca, ca sert à attendre le clic du joueur sur une touche
            if click == '_U' and self.argentjoueur > 0:
                self.mise_joueur() # mettre mise
            elif click == '_D' and self.argentcentre > 0:
                self.enlever_mise_joueur() # enlever mise
            elif click == 'x':
                self.jeu.refresh(self.croupier, self.joueur, t="Appuyez à nouveau pour quitter", cacheCroupier=False)
                sleep(0.5)
                self.jeu.refresh(self.croupier, self.joueur, t="Partie quittée.", cacheCroupier=False)
                sleep(0.5)
                self.jeu.messCentre("A bientôt !")
                sleep(0.5)
                self.quitter_jeu()
            elif click == 'a':
                self.argentcentre += self.argentjoueur
                self.argentjoueur = 0
            elif click == 'z':
                self.argentjoueur += self.argentcentre
                self.argentcentre = 0
            else:
                if click != '_U' or click != '_D' or click != '_E' or click != 'x':
                    self.jeu.refresh(self.croupier, self.joueur, t='Appuyez sur les bonnes touches !', cacheCroupier=True)
                    self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
                    sleep(0.5) 
            self.jeu.refresh(self.croupier, self.joueur, t='', cacheCroupier=True)
            self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
            
# Partage des cartes, juste histoire de le dire*
    # Les doublons c'est normal (pas touche)
        self.jeu.refresh(self.croupier, self.joueur, t='Distribution des cartes en cours..', cacheCroupier=True)
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
        sleep(0.5)
        self.jeu.refresh(self.croupier, self.joueur, t='Distribution des cartes en cours...', cacheCroupier=True)
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
        sleep(0.5)
    # Vrai distribution graphique des cartes
        self.joueur.append(paquet.pioche_carte())
        self.jeu.refresh(self.croupier, self.joueur, t='', cacheCroupier=True)
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
        sleep(0.5)
        self.croupier.append(paquet.pioche_carte())
        self.jeu.refresh(self.croupier, self.joueur, t='', cacheCroupier=True)
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
        sleep(0.5)
        self.joueur.append(paquet.pioche_carte())
        self.jeu.refresh(self.croupier, self.joueur, t='', cacheCroupier=True)
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
        sleep(0.5)
        self.croupier.append(paquet.pioche_carte())
        self.jeu.refresh(self.croupier, self.joueur, t='', cacheCroupier=True)
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
        sleep(0.5)
        # soustrait l'argent du croupier de la mise du joueur (qui se trouve au centre).
        self.argentcroupier = self.argentcroupier - self.argentcentre
        # double la mise du joueur et ajoute ce montant au centre, formant ainsi la mise totale pour la partie.
        self.argentcentre = self.argentcentre * 2
        # Actualisation
        self.jeu.refresh(self.croupier, self.joueur, t='', cacheCroupier=True)
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
        
    # Début de pioche
        self.jeu.refresh(self.croupier, self.joueur, t="Pioche (o) ne pas prendre de carte (n)", cacheCroupier=True)
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
        # On l'utilise pour s'assurer que la variable a une valeur avant d'être utilisée dans la condition de la boucle.
        click = None
        click = self.jeu.waitClick() # Encore une fois attend le clic du joueur
# Tour du joueur si utilisation de la touche 'o',donc choix de piocher
        while click != 'n' and self.totaljoueur < 21:
            if click == 'o':
                carte = paquet.pioche_carte() # permet d'aller chercher une carte dans le paquet
                self.joueur.append(carte) # rajoute la carte piocher à joueur, la liste qui étais vide la 
                self.carte_joueur()
            elif click == 'x':
                self.jeu.refresh(self.croupier, self.joueur, t="Appuyez à nouveau pour quitter", cacheCroupier=False)
                sleep(0.5)
                self.jeu.refresh(self.croupier, self.joueur, t="Partie quittée.", cacheCroupier=False)
                sleep(0.5)
                self.jeu.messCentre("A bientôt !")
                sleep(0.5)
                self.quitter_jeu()
# tour du croupier, si utilisation de 'n'onc choix de ne pas piocher                    
        self.jeu.refresh(self.croupier, self.joueur, t="Vous passez votre tour", cacheCroupier=True)
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
        sleep(0.5)
        self.jeu.refresh(self.croupier, self.joueur, t="Au tour du croupier", cacheCroupier=True)
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
        sleep(1.5)
        self.tour_croupier()                
        self.jeu.refresh(self.croupier, self.joueur, t="", cacheCroupier=False)
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
        self.distribuer_gains() # Et oui il faut redistribuer les gains, c'est une autre condition 'if'
        # ainsi que vérification du vainceur
        
# Condition dans le cas où l'argent du joueur ou du croupier est égual a 0, à appeler pour etre utilisé       
    def argent_joueur(self):
        if self.argentjoueur == 0:
            self.jeu.refresh(self.croupier, self.joueur, t="", cacheCroupier=False)
            self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
            self.jeu.messCentre("Plus d'argent")
            sleep(2)
            self.jeu.refresh(self.croupier, self.joueur, t="Restart ?(r) ou quitter ?(q)", cacheCroupier=False)
            self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
            click = self.jeu.waitClick()
            if click == 'r':
                self.restart()
            elif click == 'q':
                self.jeu.refresh(self.croupier, self.joueur, t="Partie quittée.", cacheCroupier=False)
                sleep(0.5)
                self.jeu.messCentre("A bientôt !")
                sleep(0.5)
                self.quitter_jeu()
                
    def argent_croupier(self):
        if self.argentcroupier == 0:
            self.jeu.messCentre("Le croupier n'a plus d'argent")
            sleep(2)
            self.jeu.refresh(self.croupier, self.joueur, t="Restart ?(r) ou quitter ?(q)", cacheCroupier=False)
            self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
            click = self.jeu.waitClick()
            if click == 'r':
                self.restart()
            elif click == 'q':
                self.jeu.refresh(self.croupier, self.joueur, t="Partie quittée.", cacheCroupier=False)
                sleep(0.5)
                self.jeu.messCentre("A bientôt !")
                sleep(0.5)
                self.quitter_jeu()

# Programme du croupier
    def tour_croupier(self):
        while self.totalcroupier < 17:
            carte_croupier = self.paquet.pioche_carte()
            self.croupier.append(carte_croupier)
        # Calcul du nouveau total du croupier après avoir pioché une carte.
            self.calculer_total_croupier()
        # Actualisation
            self.jeu.refresh(self.croupier, self.joueur, t="", cacheCroupier=False)
            self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
            sleep(1)

    def calculer_total_croupier(self):
        # Réinitialisation du total du croupier.
        self.totalcroupier = 0
        cpt_cp = 0
        # Parcours de chaque carte du croupier.
        for carte in self.croupier:
            # Si la carte est une figure (roi, dame, valet), elle vaut 10 points.
            if carte[0] or carte[1] > 10:
                self.totalcroupier += 10
            # Si la carte est un as, sa valeur est déterminée par la variable as_valeur (11 par défaut).
            elif carte[0] or carte[1] == 1:
                self.totalcroupier += self.as_valeur
                cpt_cp += 1
            else:
                self.totalcroupier += carte[0] # Sinon, la valeur de la carte est utilisée.
        
        # Correction du total, si un as a été compté comme 11 et le total dépasse 21.
        while cpt_cp > 0 and self.totalcroupier > 21:
            self.totalcroupier -= 10
            cpt_cp -= 1
            
# Permet de compter les cartes du joueur
    def carte_joueur(self):
        for carte in self.joueur: # compte les cartes du joueur (bon ca se vois quand même)
            if carte[0] or carte[1] > 10: #permet de verifier si une des deux premières carte est supérieur a 10
                self.totaljoueur += 10 # dans ce cas elle vaut 10
            elif carte[0] or carte[1] == 1: # permet de verifier si une des deux premières carte est un as 
                self.totaljoueur += 11 # dans ce cas elle est compté comme 11
            else:
                self.totaljoueur += carte[0]
                    
# Résultat de la partie et distribution des gains

    def calculer_main(self, main):
    # Calcul du total des valeurs des cartes dans la main du joueur/croupier.
        total = sum(carte[0] if carte[0] < 11 else 10 for carte in main)
    # Comptage du nombre d'as dans la main.
        as_count = sum(1 for carte in main if carte[0] == 1)
    # Correction du total si des as ont été comptés comme 11 et le total dépasse 21.
        while total > 21 and as_count:
            total -= 10
            as_count -= 1
        return total

    def distribuer_gains(self):
        # Calcul du total de la main du joueur et du croupier.
        cpt = self.calculer_main(self.joueur)
        cpt1 = self.calculer_main(self.croupier)
        if cpt > 21:
            self.jeu.refresh(self.croupier, self.joueur, t="Vous avez depasser 21", cacheCroupier=False)
            self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
            self.argentcroupier += self.argentcentre # prend la mise au centre pour la donner au croupier
            self.argentcentre = 0
            self.resultat("Perdu")
            sleep(1)
            self.jeu.refresh(self.croupier, self.joueur, t="", cacheCroupier=False)
        elif cpt1 > 21:
            self.jeu.refresh(self.croupier, self.joueur, t="Le croupier a depasser 21", cacheCroupier=False)
            self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
            self.argentjoueur += self.argentcentre # prend la mise au centre pour la donner au joueur
            self.argentcentre = 0
            self.resultat("Gagné(e)")
            sleep(1)
            self.jeu.refresh(self.croupier, self.joueur, t="", cacheCroupier=False)
        elif cpt == 21 and len(self.joueur) == 2: #cpt == 21:
            self.jeu.refresh(self.croupier, self.joueur, t="Vous avez fait un Blackjack", cacheCroupier=False)
            self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
            self.argentjoueur += self.argentcentre # prend la mise au centre pour la donner au joueur
            self.argentcentre = 0
            self.resultat("Blackjack !")
            sleep(1)
            self.jeu.refresh(self.croupier, self.joueur, t="", cacheCroupier=False)
        elif cpt1 == 21 and len(self.croupier) == 2: #cpt1 == 21:
            self.jeu.refresh(self.croupier, self.joueur, t="Le croupier a fait un Blackjack", cacheCroupier=False)
            self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
            self.argentcroupier += self.argentcentre # prend la mise au centre pour la donner au croupier
            self.argentcentre = 0
            self.resultat("Blackjack du croupier")
            sleep(1)
            self.jeu.refresh(self.croupier, self.joueur, t="", cacheCroupier=False)
        elif cpt > cpt1 and cpt <= 21:
            self.jeu.refresh(self.croupier, self.joueur, t="Vous avez fait un score supérieur au croupier", cacheCroupier=False)
            self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
            self.argentjoueur += self.argentcentre # prend la mise au centre pour la donner au joueur
            self.argentcentre = 0
            self.resultat("Gagné(e)")
            sleep(1)
            self.jeu.refresh(self.croupier, self.joueur, t="", cacheCroupier=False)
        elif cpt1 > cpt and cpt1 <= 21:
            self.jeu.refresh(self.croupier, self.joueur, t="Vous avez fait un score inférieur au croupier", cacheCroupier=False)
            self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
            self.argentcroupier += self.argentcentre # prend la mise au centre pour la donner au croupier
            self.argentcentre = 0
            self.resultat("Perdu(e)")
            sleep(1)
            self.jeu.refresh(self.croupier, self.joueur, t="", cacheCroupier=False)
        elif cpt == cpt1 and cpt < 21 and cpt1 < 21:
            self.jeu.refresh(self.croupier, self.joueur, t="Vous avez fait un score égual au croupier", cacheCroupier=False)
            self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
            self.argentjoueur += int(self.argentcentre / 2) # prend la moitié de la mise au centre pour la donner au joueur
            self.argentcroupier += int(self.argentcentre / 2) # prend la moitié de la mise au centre pour la donner au croupier
            self.argentcentre = 0
            self.resultat("Égalité")
            sleep(1)
            self.jeu.refresh(self.croupier, self.joueur, t="", cacheCroupier=False)
        self.argentcentre = 0
        
    def resultat(self, message):
        self.jeu.refresh(self.croupier, self.joueur, t=message, cacheCroupier=False)
        sleep(1)
        self.jeu.refresh(self.croupier, self.joueur, t="Continuer à jouer ?(c) ou quitter ?(q)", cacheCroupier=False)
        self.jeu.messCentre(message)
        self.jeu.affJetons(self.argentcroupier, self.argentjoueur, self.argentcentre)
        click = self.jeu.waitClick()
        if click == 'c':
            self.continuer_partie()
        elif click == 'q':
            self.jeu.refresh(self.croupier, self.joueur, t="Partie quittée.", cacheCroupier=False)
            sleep(0.5)
            self.jeu.messCentre("A bientôt !") <
            sleep(1)
            self.quitter_jeu()
            
# En gros ca, ca permet de vérifier si le script est exécuté en tant que programme principal
# plutôt qu'en tant que module importé dans un autre script.
# D'où "__main__" qui veut dire principal, et ouais 
if __name__ == "__main__":
    blackjack_game = BlackjackGame() # Ici on crée une instance de la classe BlackjackGame
                                     # Cela initialise essentiellement le jeu de blackjack.
    blackjack_game.jeu_de_carte() # Et la, on appelle la méthode jeu_de_carte() de l'instance blackjack_game
    # Et cette méthode permet d'initialisé une nouvelle partie de blackjack, distribue les cartes, gère les mises, et blablabla.

