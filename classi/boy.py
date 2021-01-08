from os import system
from random import randint as random


def fight(player,enemy):
    system('cls||clear')
    print(f'На вас напал {enemy.name}')
    while (player.hp > 0) and (enemy.hp > 0):
        com = input('Ваши действия\n')
        system('cls||clear')
        if com == 'атака':
            player.statchek()
            if player.hp <=0:
                break
            atack(player,enemy)
            if enemy.hp <= 0:
                break
            turn(enemy,player)
            if player.hp <= 0 or enemy.hp <= 0:
                break
        elif com == 'зелье':
            player.statchek()
            if player.hp <=0:
                break
            if player.pout > 0:
                player.pout -=1
                player.heal(25)
                print (f'вы выпили зелье лечения, теперь у вас {player.hp}хп')
            else:
                print ('отсутствуют зелья')
                continue
            turn(enemy,player)
            if player.hp <= 0 or enemy.hp <= 0:
                break
        elif com == 'защита':
            player.statchek()
            if player.hp <=0:
                break
            player.defs *= 2
            print(f'Ваша защита увеличилась в двое, теперь она равна {player.defs}')
            turn(enemy,player)
            if player.hp <= 0 or enemy.hp <= 0:
                break
            player.defs //= 2
        elif com == 'инвентарь':
            player.statchek()
            if player.hp <=0:
                break
            player.inventory()
            turn(enemy,player)
            if player.hp <= 0 or enemy.hp <= 0:
                break
        else:
            print('неправильная комманда')
            continue
    if player.hp <= 0:
        print('Поражение')
    else:
        print(f'Вы победили {enemy.name}')

def atack(ofence, defence): #Бросок урона
    dmg = defence.defs + random(1,defence.dex) - random(1,ofence.str) - ofence.weap
    if dmg >= 0:
        print(f'{ofence.name} не попал по {defence.name}')
    else:
        defence.hp += dmg
        print(f'{ofence.name} нанес {-dmg} урона, у {defence.name} осталось {defence.hp}хп')

def turn(npc, player):
    npc.statchek()
    if npc.hp < (npc.maxhp // 3) and npc.pout > 0:
        npc.heal(25)
        npc.pout -= 1
        print(f'{npc.name} принял лечебное зелье, теперь его здоровье = {npc.hp} ')
    else:
        atack(npc,player)
