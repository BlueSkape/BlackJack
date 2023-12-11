
import pygame
from pygame.locals import *
#pour le rendre dispo de n'importe où
import os
pathname = os.path.dirname(__file__)

class GUIblackjack (object):
    def __init__(self):
        """
        Initialise une fenètre du jeu blackjack et l'affiche totalement vide.
        Cette classe ne contient aucun attribut public.
        """
        
        #initialisation de pygame
        pygame.init()
        
        self.xCard = 72
        self.yCard = 96
        self.wTapis = 1000
        self.hTapis = 645
        self.recJetonJ0 = pygame.Rect(50, 50, 72, 72)
        self.recJetonJ1 = pygame.Rect(self.wTapis - 50 - 72, self.hTapis - 50 - 72,72,72)
        self.recJetonPari = pygame.Rect(0, 0, 72, 72)
        
        self.y0 = 100
        self.y1 = self.hTapis - self.yCard - self.y0        
        
        #on définit la fenêtre de base de notre jeu
        self.fenetre = pygame.display.set_mode((self.wTapis, self.hTapis))
        #un titre sur cette fenêtre
        pygame.display.set_caption("Black Jack")
        #Chargement et collage du fond
        self.fond = pygame.image.load(os.path.join(pathname, "Images", "tapiscarte2.png")).convert()
        self.jeton = pygame.image.load(os.path.join(pathname, "Images", "jeton.png")).convert_alpha()
        
        #centrage du rectangle jetons pour les pari en plein centre le la fenetre
        self.recJetonPari.center = self.fenetre.get_rect().center
        
        #création d'un dictionnaire contenant toutes images de carte
        self.cards = {}
        #correspondance couleur et répertoire images
        repCouleur = {'♥' : 'hearts', '♦' : 'diamonds', '♣' : 'clubs', '♠' : 'spades'}
        for i in range(1, 14):
            for j in ['♥', '♦', '♣', '♠']:
                self.cards[(i, j)] = pygame.image.load(os.path.join(pathname, "Images", "cards", F"{repCouleur[j]}/{i}.png")).convert_alpha()
        self.verso = pygame.image.load(os.path.join(pathname, "Images", "cards", "verso.png")).convert_alpha()
        
        #affichage d'une première fenètre contenant une grille vide
        self.fenetre.blit(self.fond, (0,0))

        #Rafraîchissement de l'écran
        pygame.display.update()
    
    def refresh(self, j1, j2, t = "", cacheCroupier = False):
        """
        Cette méthode rafraichie l'affichage des deux listes de cartes passées en argument.
        
        j1 et j2 sont des objets indexables, dont les éléments sont de la forme (n, c).
            - n est un entier de 1 à 13 représentant la valeur faciale de la carte (11, 12, et 13 étant respectivement le valet, la dame et le roi).
            - c est un caractère unicode parmi '♥', '♦', '♣', '♠' représentant la couleur de la carte.
        D'autre  part j1 et j2 doivent disposer d'une méthode __len__ pour répondre a la fonction len().
        Il peut donc s'agir de listes, de tuples ou de tout autres objets répondants a ces critères.
        
        cacheCroupier est un booléen. Si cette argument est vrai, toutes les cartes du croupier seront
        affichées retournées sauf la première.
        
        t est un texte à afficher à destination du joueur.
        """
        
        #réinitialisation du fond
        self.fenetre.blit(self.fond, (0,0))
        
        #affichage de j1
        #offset pour la premiere pièce
        delta = 8
        n = len(j1)
        x0 = self.wTapis//2 - (n*self.xCard + (n-1)*delta)//2
        
        for i in range(n):
            if i == 0 or not cacheCroupier :
                self.fenetre.blit(self.cards[j1[i]], (x0 + i*(self.xCard + delta), self.y0))
            else:
                self.fenetre.blit(self.verso, (x0 + i*(self.xCard + delta), self.y0))
        #affichage de j2
        n = len(j2)
        x0 = self.wTapis//2 - (n*self.xCard + (n-1)*delta)//2
        
        for i in range(n):
            self.fenetre.blit(self.cards[j2[i]], (x0 + i*(self.xCard + delta), self.y1))            

        #zone de texte
        #Une police
        police = pygame.font.SysFont("Arial Black",28)
        #un texte
        texte = police.render(t, True, pygame.Color("#FFFF00"))
        #Une surface pour centrer le texte sur le bandeau du haut
        surfText = pygame.Rect(0, self.hTapis - 100, self.wTapis, 100)
        #pour centrer le texte
        rectTexte = texte.get_rect()
        rectTexte.center = surfText.center
        self.fenetre.blit(texte, rectTexte)
        
        #Rafraîchissement de l'écran
        pygame.display.update()

    def affJetons(self, nj0, nj1, njp):
        """
        Cette méthode permet d'afficher 3 jetons. Un pour le croupier, un pour le joueur et un au centre pour le pari.
        La valeur de chaque pile de jetons : respectivement njo, nj1, njp est inscrite dessus.
        Si un nombre de jetons est a zéro : la pile n'apparait pas.
        """        
        values = nj0, nj1, njp
        rec = self.recJetonJ0, self.recJetonJ1, self.recJetonPari

        for i in range(3):
            
            if values[i] > 0:
                
                #Une police adaptée au nombre a afficher
                if values[i] < 10 :
                    police = pygame.font.SysFont("Arial Black",28)
                elif values[i] < 100 :
                    police = pygame.font.SysFont("Arial Black",24)
                else:
                    police = pygame.font.SysFont("Arial Black",18)
                
                texte = police.render(str(values[i]), True, pygame.Color("#FFFFFF"))
                #pour centrer le nombre sur le jeton
                rectTexte = texte.get_rect()
                rectTexte.center = rec[i].center
                
                self.fenetre.blit(self.jeton, rec[i])
                self.fenetre.blit(texte, rectTexte)
            
            #Rafraîchissement de l'écran
            pygame.display.update()
        
    def messCentre(self, mess):
        """
        Cette méthode permet d'afficher GAME OVER plein écran.
        """
        police = pygame.font.Font(os.path.join(pathname, "led.ttf"),100)
        texte = police.render(mess, True, pygame.Color("#FFFF00"))
        #pour centrer le texte
        rectTexte = texte.get_rect()
        rectTexte.center = self.fenetre.get_rect().center
        self.fenetre.blit(texte,rectTexte)
        #Rafraîchissement de l'écran
        pygame.display.update()

    def waitClick(self):
        """
        Cette méthode attend l'action d'un joueur. Elle gère trois types d'actions :
            - demande fermeture de la fenètre : fermeture propre de la fenètre pygame et fin du programme python.
            - click sur la fenetre : retourne  0 si click sur les cartes du croupier et 1 si click sur les cartes du joueur.
            - appui sur des touches (uniquement y, n, s, r, c, d, fleche droite : retourne la lettre correspondante et 'R' pour la flèche.
        Une fois exécutée, on ne peut sortir de cette méthode que par l'une de ces trois actions.
        """
        while True:
            #Limitation de vitesse de la boucle
            pygame.time.Clock().tick(30)
            
            for event in pygame.event.get():    #Attente des événements
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                    
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:   #Si clic gauche
                        if event.pos[1] > self.y0 and event.pos[1] < self.y0 + self.yCard:
                            return 'c0'
                        if event.pos[1] > self.y1 and event.pos[1] < self.y1 + self.yCard:
                            return 'c1'
                        if self.recJetonPari.collidepoint(event.pos):
                            return 'jp'
                        if self.recJetonJ0.collidepoint(event.pos):
                            return 'j0'
                        if self.recJetonJ1.collidepoint(event.pos):
                            return 'j1'
                        
                if event.type == KEYDOWN:
                    touches = {K_RIGHT : '_R', K_LEFT : '_L', K_UP : '_U', K_DOWN : '_D', K_RETURN : '_E', K_BACKSPACE : '_B', K_ESCAPE : '_S'}
                    touche = event.key
                    if touche in touches:
                        return touches[touche]
                    return event.unicode  
                    
                         
if __name__ == "__main__":
    import time

    #création d'une grille vierge
    g1 = [(1, '♥'), (11, '♥'), (5, '♦'), (11, '♣'), (6, '♠'), (13, '♠')]
    g2 = [(5, '♥'), (12, '♥'), (10, '♦'), (7, '♣'), (8, '♠')]
    
    GUI = GUIblackjack()
    
    GUI.refresh(g1, g2, "C'est a vous de jouer !!", True)
    time.sleep(2)
    
    GUI.refresh(g1, g2, "", False)
    GUI.messCentre("PERDU !!")
    time.sleep(2)
    
    GUI.refresh([(5, '♥'), (10, '♦'), (13, '♣')], [(13, '♠'), (1, '♥')], "Voulez-vous recommencer ?")
    GUI.messCentre("BLACKJACK !!")
    time.sleep(2)

    GUI.refresh([(5, '♥'), (10, '♦'), (13, '♣')], [(13, '♠'), (1, '♥')], "Voulez-vous recommencer ?")
    GUI.affJetons(56, 120, 0)
    time.sleep(2)    
    GUI.refresh([(5, '♥'), (10, '♦'), (13, '♣')], [(13, '♠'), (1, '♥')], "Avec des jetons ...")
    GUI.affJetons(56, 115, 5)
    
    while True :
        print(GUI.waitClick())

