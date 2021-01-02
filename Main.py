from random import randint as random
from os import system
from classi import personaji as p
from classi import komnati as k
from classi import boy as b

inventory = ['Пустой слот'] * 5
player = p.plc(50,'игрок',0, 0,4,4,0, inventory,1234567890) #Хп,Имя,Защита,Оружие,Кость силы,кость защиты,кол-во зелий
gob = p.npc(10,'гоблин', 0, 2, 2, 2,1)

first = k.firstroom()
second  = k.secondroom()
while True:
    if player.room == 1:
        first.enter(player)
    elif player.room == 2:
        second.enter(player)
    else:
        print("кажется что здесь кончился сюжет, или произошла ошибка при переходе в другие комнаты, а по сему вот тебе гоблин")
        i =input()
        break
b.fight(player,gob)
