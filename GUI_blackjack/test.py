from guiBlackJack import GUIblackjack
from random import shuffle # import le mélange de carte
from time import sleep # import le temps d'attente

class jeu_de_carte :
    def __init__(self) :
        c = [(nbre, '♥') for nbre in range(1,14)]
        t = [(nbre, '♣') for nbre in range(1,14)]
        k = [(nbre, '♦') for nbre in range(1,14)]
        p = [(nbre, '♠') for nbre in range(1,14)]
        self.paquet = c+t+k+p
        
    def melange_carte(self):
        shuffle(self.paquet)
        
    def pioche_carte(self):
        return self.paquet.pop()
    
paquet = jeu_de_carte()

paquet.melange_carte() 

jeu = GUIblackjack()

jeu.refresh([],[])

croupier = []
joueur = []
centre = 0

argentcroupier = 100
argentjoueur = 100
argentcentre = 0

jeu.refresh(croupier, joueur,t = 'Bienvenue sur la table de BlackJack', cacheCroupier = True)
sleep(1)

jeu.refresh(croupier, joueur,t = 'Vous êtes prêt(e) ça va bientôt commencer', cacheCroupier = True)
jeu.affJetons(argentcroupier, argentjoueur, argentcentre)
sleep(1)

jeu.refresh(croupier, joueur,t = 'Mettez une mise de 5 au minimum', cacheCroupier = True)
jeu.affJetons(argentcroupier, argentjoueur, argentcentre)

click = jeu.waitClick()

jeu.refresh(croupier, joueur,t = '', cacheCroupier = True)
jeu.affJetons(argentcroupier, argentjoueur, argentcentre)

click = None

while click != '_E' :
    click = jeu.waitClick()
    
    if click == '_U' and argentjoueur > 0 :
        argentjoueur = argentjoueur - 5
        argentcentre = argentcentre + 5
        jeu.refresh(croupier, joueur,t = '', cacheCroupier = True)
        jeu.affJetons(argentcroupier, argentjoueur, argentcentre)
    
    elif click == '_U' and argentjoueur == 0 :
        jeu.refresh(croupier, joueur,t = "Vous n'avez pas assez d'argent pour miser d'avantage", cacheCroupier = True)
        jeu.affJetons(argentcroupier, argentjoueur, argentcentre)
    
    elif argentcentre == 0 and click == '_D':
        jeu.refresh(croupier, joueur,t = "Il n'y a pas de mise sur la table", cacheCroupier = True)
        jeu.affJetons(argentcroupier, argentjoueur, argentcentre)
    
    elif argentcentre > 0 and click == '_D' :
        argentcentre = argentcentre - 5
        argentjoueur = argentjoueur + 5
        jeu.refresh(croupier, joueur,t = '', cacheCroupier = True)
        jeu.affJetons(argentcroupier, argentjoueur, argentcentre)
        
jeu.refresh(croupier, joueur,t = 'Distribution des cartes en cours...', cacheCroupier = True)
jeu.affJetons(argentcroupier, argentjoueur, argentcentre)
sleep(1)

joueur.append(paquet.pioche_carte())
jeu.refresh(croupier, joueur,t = '', cacheCroupier = True)
jeu.affJetons(argentcroupier, argentjoueur, argentcentre)
sleep(0.5)

croupier.append(paquet.pioche_carte())
jeu.refresh(croupier, joueur,t = '', cacheCroupier = True)
jeu.affJetons(argentcroupier, argentjoueur, argentcentre)
sleep(0.5)

joueur.append(paquet.pioche_carte())
jeu.refresh(croupier, joueur,t = '', cacheCroupier = True)
jeu.affJetons(argentcroupier, argentjoueur, argentcentre)
sleep(0.5)

croupier.append(paquet.pioche_carte())
jeu.refresh(croupier, joueur,t = '', cacheCroupier = True)
jeu.affJetons(argentcroupier, argentjoueur, argentcentre)
sleep(0.5)

argentcroupier = argentcroupier - argentcentre

argentcentre = argentcentre + argentcentre

jeu.refresh(croupier, joueur,t = '', cacheCroupier = True)

jeu.affJetons(argentcroupier, argentjoueur, argentcentre)

totaljoueur = 0
totalcroupier = 0

cpt = 0 # compte la main du joueur
cpt1 = 0 # compte la main du croupier

for carte in joueur :
    cpt += carte[0]

for carte1 in croupier:
    cpt1 += carte[0]
    
jeu.refresh(croupier, joueur,t = "Pioche (o) ne pas prendre de carte (n)", cacheCroupier = True)
jeu.affJetons(argentcroupier, argentjoueur, argentcentre)

click = jeu.waitClick() 

while click != 'n' and cpt < 21:
    if click == 'o' :
        carte = paquet.pioche_carte()
        joueur.append(carte)
        cpt += carte[0]
        sleep(0.5)
        jeu.refresh(croupier, joueur,t = "", cacheCroupier = True)
        jeu.affJetons(argentcroupier, argentjoueur, argentcentre)
    click = jeu.waitClick()  

while cpt1 < 21 :
    carte1 = paquet.pioche_carte()
    croupier.append(carte1)
    cpt1 += carte[0]
    sleep(0.5)
    jeu.refresh(croupier, joueur,t = "", cacheCroupier = False)
    jeu.affJetons(argentcroupier, argentjoueur, argentcentre)
    sleep(1)

if cpt < cpt1 or cpt1 > cpt:
    joueur

def messSpecial(self, mess):
        """
        Cette méthode permet d'afficher un message au millieu sans prendre toute la place sur l'écran.
        """
        police = pygame.font.Font(os.path.join(pathname, "led.ttf"),30)
        texte = police.render(mess, True, pygame.Color("#8a1627"))
        #pour centrer le texte
        rectTexte = texte.get_rect()
        rectTexte.center = self.fenetre.get_rect().center
        self.fenetre.blit(texte,rectTexte)
        #Rafraîchissement de l'écran
        pygame.display.update()

if cpt > 21 : 
    jeu.refresh(croupier, joueur,t = "Restart?(r)", cacheCroupier = True)
    jeu.affJetons(argentcroupier, argentjoueur, argentcentre)
    jeu.messCentre("Game Over")
    click = jeu.waitClick()
    if click == 'r':
        jeu.jeu_de_carte()

elif cpt == 21:
    jeu.refresh(croupier, joueur,t = "Rejouer? (r)", cacheCroupier = True)
    jeu.affJetons(argentcroupier, argentjoueur, argentcentre)
    jeu.messCentre("Gagné(e)")
    
