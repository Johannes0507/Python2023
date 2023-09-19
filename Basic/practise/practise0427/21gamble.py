# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 23:47:32 2023

@author: 李旻恩
"""

import random

Card = list()

def washCards(Cards):
    for i in range(200):
        first = random.randint(0,len(Cards)-1)
        end = random.randint(0,len(Cards)-1)
        Cards[first],Card[end] = Cards[end],Card[first]

def giveCards():
    point = Card.pop(0)
    if point >= 10:
        point = 10
    return point
    

for i in range(1,14):
    for x in range(1,5):
        Card.append(i)

washCards(Card)
print(Card)

print('歡迎來到21點')
print('-'*30)

myMoney = 100

while myMoney > 0:
    gamep = myMoney
    
    while True:
        gamep = int(input('押注代幣金額：'))
    
        if gamep > myMoney:
            print('代幣不足,目前代幣有：',myMoney)
        else:
            break
        
    print()
    print()
    print('你下注代幣：',gamep)
    
    NPC = list()
    player = list()
    
    # 莊家與玩家發第一次牌
    NPC.append(giveCards())
    print('莊家？點')
    player.append(giveCards())
    print('玩家：',player[0],'點') 
    
    print('-'*30)
    
    # 莊家與玩家發第二次牌
    NPC.append(giveCards())
    print('莊家：',NPC[1])
    player.append(giveCards())
    print('玩家：',player[1])
    
    print('目前玩家總點數',sum(player))
    print('-'*30)
    
    # 判斷玩家是否要加牌
    q = 'y'
    i = 2
    
    while q == 'y':
        q = input('請問玩家要加牌y/n：')
        
        if q != 'y' :
            break
        
        player.append(giveCards())
        print('玩家：',player[i],'點')
        print('玩家總點數：',sum(player))
        i += 1
        
        if sum(player) > 21:
            break
        
        if sum(player) == 21:
            myMoney += gamep
            print('完家贏了！')
            break
    
    # 判斷莊家如果小於19就加牌
    print('莊家總點數：',sum(NPC))
    
    if sum(player) < 21:    
        i = 2
        while sum(NPC) <= 19:
            NPC.append(giveCards())
            print('莊家：',NPC[2],'點')
            print('莊家總點數',sum(NPC),'點')
            i += 1
    
    if sum(player) < 21:
        
        if sum(NPC) > 21 or sum(NPC) < sum(player):
            myMoney += gamep
            print('莊家輸了')
        
        elif sum(NPC) == 21 or sum(NPC) > sum(player):
            myMoney -= gamep
            print('莊家贏了')
    
    elif sum(NPC) == sum(player):
        myMoney -= gamep
        print('莊家贏了')
        
    elif len(NPC) == 5 and sum(player): 
        myMoney -= gamep*2
        print('莊家過五關')
        
    elif sum(player) > 21:
        myMoney -= gamep 
        print('玩家爆了')
        
    print()
    print('-'*30)
    
    print('目前剩餘：',myMoney,'元')
    
    q = input('繼續請按y：')
    
    if q != 'y':
        break
    
    
    
    
    
    
    
        
        








