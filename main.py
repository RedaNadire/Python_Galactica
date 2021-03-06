import pygame
from pygame.locals import *
from credits_func import *
from options_func import *
from mode_func import *
from deckBuilder import *

###### Main Function ######
#(1) Initialize Game Menu #
def main(): 
    pygame.init()

    fenetre = pygame.display.set_mode((960, 720))
    pygame.display.set_caption("Galactica")
    continuer = 1
     
    fond = pygame.image.load("images/background.jpg").convert()
    title = pygame.image.load("images/title.png").convert()
    button_play = pygame.image.load("images/play_no_highlight.jpg").convert()
    button_play_h = pygame.image.load("images/play_highlight.jpg").convert()
    button_deck = pygame.image.load("images/deck_no_highlight.jpg").convert()
    button_deck_h = pygame.image.load("images/deck_highlight.jpg").convert()
    button_options = pygame.image.load("images/options_no_highlight.jpg").convert()
    button_options_h = pygame.image.load("images/options_highlight.jpg").convert()
    button_credits = pygame.image.load("images/credits_no_highlight.jpg").convert()
    button_credits_h = pygame.image.load("images/credits_highlight.jpg").convert()
    button_quit = pygame.image.load("images/quit_no_highlight.jpg").convert()
    button_quit_h = pygame.image.load("images/quit_highlight.jpg").convert()
    fenetre.blit(fond, (0,0))
    fenetre.blit(title, (325,0))
    fenetre.blit(button_play, (418,173))
    fenetre.blit(button_deck, (418,222))
    fenetre.blit(button_options, (418,271))
    fenetre.blit(button_credits, (418,320))
    fenetre.blit(button_quit, (418,369))
    pygame.display.flip()
    play_r = button_play.get_rect()
    play_r.x, play_r.y = 418, 173
    deck_r = button_deck.get_rect()
    deck_r.x, deck_r.y = 418, 222
    options_r = button_options.get_rect()
    options_r.x, options_r.y = 418, 271
    credits_r = button_credits.get_rect()
    credits_r.x, credits_r.y = 418, 320
    quit_r = button_quit.get_rect()
    quit_r.x, quit_r.y = 418, 369
    list_image_maps = []
    while continuer:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                #Bouton QUIT
                if ( x in range(418,543)) and (y in range(369,398)):
                    continuer = 0
                #Bouton PLAY
                elif ( x in range(418,543)) and (y in range (173,202)):
                    mode_choice(fenetre)
                #Bouton DECK BUILDER
                elif ( x in range(418,543)) and (y in range (222,251)):
                    deckBuilder_main(fenetre)
                #Bouton CREDITS
                elif ( x in range(418,543)) and (y in range (320,349)):
                    credits_print(fenetre)
                #Bouton OPTIONS
                elif ( x in range(418,543)) and (y in range (271,300)):
                    options_print(fenetre)
                        
        if quit_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_quit_h, (418,369))
            pygame.display.flip()
        elif play_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_play_h, (418,173))
            pygame.display.flip()
        elif deck_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_deck_h, (418,222))
            pygame.display.flip()
        elif options_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_options_h, (418,271))
            pygame.display.flip()
        elif credits_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_credits_h, (418,320))
            pygame.display.flip()
        else:
            menu_routine(fenetre)
    pygame.quit()

def menu_routine(fenetre):
    pygame.display.set_caption("Galactica")
    fond = pygame.image.load("images/background.jpg").convert()
    title = pygame.image.load("images/title.png").convert()
    button_play = pygame.image.load("images/play_no_highlight.jpg").convert()
    button_deck = pygame.image.load("images/deck_no_highlight.jpg").convert()
    button_options = pygame.image.load("images/options_no_highlight.jpg").convert()
    button_credits = pygame.image.load("images/credits_no_highlight.jpg").convert()
    button_quit = pygame.image.load("images/quit_no_highlight.jpg").convert()
    fenetre.blit(fond, (0,0))
    fenetre.blit(title, (325,0))
    fenetre.blit(button_play, (418,173))
    fenetre.blit(button_deck, (418,222))
    fenetre.blit(button_options, (418,271))
    fenetre.blit(button_credits, (418,320))
    fenetre.blit(button_quit, (418,369))
    pygame.display.flip()
    
if __name__ == "__main__":
    main()
