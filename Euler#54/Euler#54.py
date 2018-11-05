#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 17:01:57 2018

@author: toddbilsborough
"""

import time

print ("Running!")
start_time = time.time()

def royal_flush(hand):
    flush = ["A", "K", "Q", "J", "T"]
    for card in flush:
        if card not in hand:
            return False
    suite = hand[1]
    if hand.count(suite) != 5:
        return False
    return True

def straight_flush(hand):
    flush = ["A", "K", "Q", "J", "T"]
    for card in flush:
        if card not in hand:
            return False
    return True

def four_of_a_kind(hand):
    for i in range(0, 4, 3):
        if hand.count(hand[i]) == 4: return int_value(hand[i])
    return 0

def full_house(hand):
    if three_of_a_kind(hand) > 0 and one_pair(hand) > 0:
        return max(int_value(three_of_a_kind(hand)), 
                   int_value(one_pair(hand)))
    
def flush(hand):
    suits = ["C", "D", "H", "S"]
    for suit in suits:
        if hand.count(suit) == 5:
            return int_value(hand[0])
    return 0

def straight(hand):
    values = [int_value(hand[i]) for i in [0, 3, 6, 9, 12]]
    values.sort()
    match_value = values[0]
    for value in values:
        if value != match_value:
            return 0
        match_value += 1
    return values[4]
    
def three_of_a_kind(hand):
    for i in range(0, 7, 3):
        if hand.count(hand[i]) == 3: return int_value(hand[i])
    return 0

def two_pair(hand):
    if one_pair(hand) > 0:
        matched = one_pair(hand)
    for i in range(0, 10, 3):
        if hand.count(hand[i]) == 2: 
            if int_value(hand[i]) != matched:
                return max(int_value(hand[i]), matched)
    return 0    

def one_pair(hand):
    for i in range(0, 10, 3):
        if hand.count(hand[i]) == 2: return int_value(hand[i])
    return 0

def int_value(value):
    cards = {
            "A": 14,
            "K": 13,
            "Q": 12,
            "J": 11,
            "T": 10}
    if value in cards: return cards[value]
    else: return int(value)

def tiebreaker(hand_one, hand_two):
    cards = ["A", "K", "Q", "J", "T", 
             "9", "8", "7", "6", "5", 
             "4", "3", "2", "1"]
    for card in cards:
        if card in hand_one and card not in hand_two:
            return 1
        if card in hand_two and card not in hand_one:
            return 2

hands = []
pokertxt = open("poker.txt")
for line in pokertxt: hands.append(line)
pokertxt.close()

player_one_wins = 0
for hand in hands:
    hand_one = [hand[i] for i in range(0, 14)]
    hand_two = [hand[i] for i in range(15, 29)]
    if royal_flush(hand_one): 
        player_one_wins += 1
        continue
    if royal_flush(hand_two):
        continue
    if straight_flush(hand_one): 
        player_one_wins += 1
        continue
    if straight_flush(hand_two):
        continue
    if four_of_a_kind(hand_one) >= four_of_a_kind(hand_two) \
            and four_of_a_kind(hand_one) > 0:
        if four_of_a_kind(hand_one) == four_of_a_kind(hand_two):
            if tiebreaker(hand_one, hand_two) == 1:
                player_one_wins += 1
                continue
        else:
            player_one_wins += 1
            continue
    if four_of_a_kind(hand_two) > four_of_a_kind(hand_one):
        continue
    if three_of_a_kind(hand_one) > 0 and one_pair(hand_one) > 0:
        if three_of_a_kind(hand_one) >= three_of_a_kind(hand_two) \
                and three_of_a_kind(hand_one) > 0:
            if three_of_a_kind(hand_one) == three_of_a_kind(hand_two):
                if one_pair(hand_one) > one_pair(hand_two):
                    player_one_wins += 1
                    continue
                if tiebreaker(hand_one, hand_two) == 1:
                    player_one_wins += 1
                    continue
            else:
                player_one_wins += 1
                continue
    if three_of_a_kind(hand_two) > 0 and one_pair(hand_two) > 0:
        if three_of_a_kind(hand_two) > three_of_a_kind(hand_one) \
                and three_of_a_kind(hand_two) > 0:
            continue
    # Only hands below this line are actually expected to match
    if flush(hand_one) > flush(hand_two):
        player_one_wins += 1
        continue
    if flush(hand_two) > flush(hand_one):
        continue
    if straight(hand_one) > straight(hand_two):
        player_one_wins += 1
        continue
    if straight(hand_two) > straight(hand_one):
        continue
    if three_of_a_kind(hand_one) >= three_of_a_kind(hand_two) \
            and three_of_a_kind(hand_one) > 0:
        if three_of_a_kind(hand_one) == three_of_a_kind(hand_two):
            if tiebreaker(hand_one, hand_two) == 1:
                player_one_wins += 1
                continue
        else:
            player_one_wins += 1
            continue
    if three_of_a_kind(hand_two) > three_of_a_kind(hand_one):
        continue
    if two_pair(hand_one) >= two_pair(hand_two) \
                and two_pair(hand_one) > 0:
            if two_pair(hand_one) == two_pair(hand_two):
                if tiebreaker(hand_one, hand_two) == 1:
                    player_one_wins += 1
                    continue
            else:
                player_one_wins += 1
                continue 
    if two_pair(hand_two) > two_pair(hand_one):
        continue
    if one_pair(hand_one) >= one_pair(hand_two) \
            and one_pair(hand_one) > 0:
        if one_pair(hand_one) == one_pair(hand_two):
            if tiebreaker(hand_one, hand_two) == 1:
                player_one_wins += 1
                continue
        else:
            player_one_wins += 1
            continue
    if one_pair(hand_two) > one_pair(hand_one):
        continue
    if tiebreaker(hand_one, hand_two) == 1:
        player_one_wins += 1
        continue
        
end_time = time.time()
run_time = end_time - start_time
print ("%s found in %s seconds" % (player_one_wins, 
                                   "{0:.4f}".format(run_time)))