import pygame
import copy

from pygame.locals import *
from card_loading import *

#Methode pour savoir si une carte est jouable
def is_card_playable(card_cost, stats, board):
    isTherePlace = False
    for i in range(0,5):
        if board['player'+str(i)] == 'empty':
            isTherePlace = True

    if isTherePlace:
        if int(stats['player_pool']) >= card_cost:
            return True
    return False

#Intelligence Artificielle - IA
def play_turn_ia(stats, board, hand_enemy):
    #Attaque toujours - board en priorite 
    for i in range(0,5):
        if board['enemy'+str(i)] != 'empty':
            if board['enemy'+str(i)]['can_attack'] == 1:
                for y in range(0,5):
                    if board['player'+str(y)] != 'empty':
                        board['enemy'+str(i)]['can_attack'] = 0
                        attack_combat(board, y, i)
                        break
    #Attaque heros si une creature peut encore attaquer apres verifification du board
    for i in range(0,5):
        if board['enemy'+str(i)] != 'empty':
            if board['enemy'+str(i)]['can_attack'] == 1:
                board['enemy'+str(i)]['can_attack'] = 0
                attack_player_hero(stats, board, i)
    #FIFO - Premiere carte jouable Premiere carte jouee
    for i in range(len(hand_enemy) - 1):
        print(hand_enemy[i])
        if is_card_playable_ia(hand_enemy[i]['Cost'], stats, board):
             x = get_empty_slot(board,'enemy')
             board['enemy'+str(x)] = copy.deepcopy(hand_enemy[i])
             board['enemy'+str(x)]['can_attack'] = 0
             stats['enemy_pool'] = str(int(stats['enemy_pool']) - int(board['enemy'+str(x)]['Cost']))
             del(hand_enemy[i])
             return
            
def call_capacity(stats, board, hand_player, deck_player, index):
    if board['player'+str(index)]['Capacity'] == 1:
        draw_card(stats, hand_player, deck_player, "player")
    if board['player'+str(index)]['Capacity'] == 3:
        for i in range(0,5):
            if board['enemy'+str(i)] != 'empty':
                board['enemy'+str(i)]['Health'] -= 1
                board['enemy'+str(i)]['Wounded'] = True
            if board['player'+str(i)] != 'empty':
                board['player'+str(i)]['Health'] -= 1
                board['player'+str(i)]['Wounded'] = True
        for i in range(0,5):
            if board['enemy'+str(i)] != 'empty':
                if board['enemy'+str(i)]['Health'] <= 0:
                    board['cimetery_enemy'].append(board['enemy'+str(i)])
                    board['enemy'+str(i)] = 'empty'
            if board['player'+str(i)] != 'empty':
                if board['player'+str(i)]['Health'] <= 0:
                    board['cimetery_player'].append(board['player'+str(i)])
                    board['player'+str(i)] = 'empty'
            
def is_taunt_on_board(board):
    for i in range(0,5):
        if board['enemy'+str(i)] != 'empty':
            if is_taunt_existing(board, i):
                return i
    return -1
def is_taunt_existing(board, index):
    if board['enemy'+str(index)]['Capacity'] == 2:
        return True;
    else:
        return False;
def get_empty_slot(board, target):
    place = -1
    if target == 'enemy':
        for i in range(0,5):
            if board['enemy'+str(i)] == 'empty':
                return i
    elif target == 'player':
        for i in range(0,5):
            if board['player'+str(i)] == 'empty':
                return i
    return place
            
#Methode pour savoir si une carte est jouable
def is_card_playable_ia(card_cost, stats, board):
    isTherePlace = False
    for i in range(0,5):
        if board['enemy'+str(i)] == 'empty':
            isTherePlace = True

    if isTherePlace:
        if int(stats['enemy_pool']) >= card_cost:
            return True
    return False

#Methode qui gere l'attack entre deux cartes
def attack_combat(board, index_p, index_e):
    initial_hp_p = board['player'+str(index_p)]['Health']
    initial_hp_e = board['enemy'+str(index_e)]['Health']
    
    board['enemy'+str(index_e)]['Health'] -= board['player'+str(index_p)]['Attack']
    board['player'+str(index_p)]['Health'] -= board['enemy'+str(index_e)]['Attack']
    
    if int(board['enemy'+str(index_e)]['Health']) < initial_hp_e:
        board['enemy'+str(index_e)]['Wounded'] = True
    if int(board['player'+str(index_p)]['Health']) < initial_hp_p:
        board['player'+str(index_p)]['Wounded'] = True

        
    if int(board['enemy'+str(index_e)]['Health']) <= 0:
        board['cimetery_enemy'].append(board['enemy'+str(index_e)])
        board['enemy'+str(index_e)] = 'empty'
    if int(board['player'+str(index_p)]['Health']) <= 0:
        board['cimetery_player'].append(board['player'+str(index_p)])
        board['player'+str(index_p)] = 'empty'

def attack_enemy_hero(stats, board, index_p):
    hp_enemy = int(stats['hp_enemy'])
    hp_enemy -= board['player'+str(index_p)]['Attack']
    stats['hp_enemy'] = str(hp_enemy)

def attack_player_hero(stats, board, index_e):
    hp_player = int(stats['hp_player'])
    hp_player -= board['enemy'+str(index_e)]['Attack']
    stats['hp_player'] = str(hp_player)
        
