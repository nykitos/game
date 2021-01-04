from random import randint as random
from os import system


class npc:
    """Персонажи """


    def __init__(self,hp,name,defs,weap,stre,dex,pout): #Характеристики
        self.name = name #Имя
        self.hp = hp #Очки здоровья
        self.defs = defs #броня
        self.weap = weap #оружие
        self.str = stre #Кость силы
        self.dex = dex #Кость защиты
        self.pout = pout #кол-во зелий
        self.maxhp = hp #макс хп
        self.stat = [0,0]


    def heal (self,hp): #метод лечения
        self.hp += hp
        if self.hp > self.maxhp :
            self.hp = self.maxhp

    def dmg(self,d):
        self.hp -= d
        print(f'{self.name}-у нанесено {d} урона, осталось {self.hp}')

    def statchek(self): # метод проверки статусов и их описание

        if self.stat[0] > 0: # stat[0] - отравление наносит столько урона сколько длится уменьшаясь с каждым ходом
            self.hp -= self.stat[0]
            print(f'{self.name} отравлен, ненесенo {self.stat[0]} уронa, осталось {self.hp}, отравление длится еще {self.stat[0]}ходов')
            self.stat[0] -=1

        if self.stat[1] > 0: # stat[1] - противоположно отравлению восстанавливает столько урона сколько длится уменьшаясь с каждым ходом
            self.stat[1] -= 1
            self.heal(2)
            print(f'{self.name} регенерирует 2 хп, стало {self.hp}, регенерация длится еще {self.stat[1]}ходов')

class plc (npc): #player character

    def  __init__ (self,hp,name,defs,weap,stre,dex,pout,inv,room): #Характеристики
        self.inv = inv #Инвентарь
        self.room = room #Комната в которой находится игрок
        self.wname = 'Голые кулаки'

        super().__init__(hp,name,defs,weap,stre,dex,pout)

    def seeinventory(self):
        print(f'Ваш инвентарь:\n {self.pout} лечебных зелий')
        i = -1
        for item in self.inv:
            i+=1
            print(f'{i}. {item}')
        print('На тебе надето:')
        print(f'Оружие: {self.wname}')

    def inventory (self):

        self.seeinventory()
        while True:
            a = input('Выберите вещь')
            if a.isdigit():
                a = int(a)
                if a >=0 and a <=4:
                    item = self.inv[a]
                    if item == 'Пустой слот':
                        print('Вы выбрали пустой слот, но там нечего нет!')
                        continue
                    elif item == 'Странный мох' :
                        self.stat[0] = 0
                        print('С вас снято отравление')
                        self.inv[a] = 'Пустой слот'
                        break
                    elif item == 'Странный гриб':
                        self.stat[0] = 5
                        print('Кажется это было плохим решением, вы отравлены')
                        self.inv[a] = 'Пустой слот'
                        break
                    elif item == 'Ржавый меч': #Надо будет сделать из этого функцию для любого оружия но пока мне лень
                        print('Сложно назвать это мечем, но в качестве дубинки сойдет')
                        while True:
                            inp = input('Вы хотите экипировать этот меч?\n1.Да\n2.Нет')
                            if inp == '1':
                                if self.weap != 0:
                                    weapon = self.wname #Возвращение другого оружия в инвентарь, если оно там было
                                    self.inv[a] = weapon
                                self.wname = item
                                self.weap = 2


                            elif inp == '2':
                                pass
                            else:
                                print('Неправельная комманда')
                                continue
                            break
                    elif item == 'Ржавый ключ':
                        print('Просто ключ, нечего примечательного')
                    





            elif a == 'зелье':
                player.statchek()

                if self.pout > 0:
                    self.pout -=1
                    self.heal(25)
                    print (f'вы выпили зелье лечения, теперь у вас {self.hp}хп')
                else:
                    print ('отсутствуют зелья')
                    continue

            else :
                print('Неправильный номер')
                continue
            break

    def grab(self,g_item):
        self.seeinventory()
        while True:
            a=input( f'Куда вы хотите положить {g_item}?\n')
            if a.isdigit():
                a = int(a)
                if self.inv[a] != 'Пустой слот':
                    print(f'Тут уже лежит {self.inv[a]} ')
                    while True:
                        q = input(f'Хотите ли вы заменить{self.inv[a]}\n1.да/2.нет\n')
                        if q == '1':
                            self.inv[a] = q_item
                            system('cls||clear')
                            break
                        elif q == '2':
                            break
                        else:
                            print('Неправильная команда')
                            continue
                elif a < 4 and a>-1:
                    self.inv[a] = g_item
                    system('cls||clear')
                    break
            else :
                print('Неправильная команда')
                continue
