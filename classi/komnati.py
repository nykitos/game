from os import system
from random import randint as random

class room():
    """Комнаты"""

    def __init__(self):
        self.ent = 0 #Была ли эта комната посещена хоть раз 0 - нет 1 - да
class firstroom(room):
    """Пробуждение, первая комната"""

    def __init__(self):
        self.ent = 0

    def enter(self,player):
        if self.ent == 0:
            self.ent = 1
            self.try1 = 1

            print("Ты просыпаешься, голова раскалывается а последнее что ты помнишь это то как ты взял простенький квест на поиск какой то вещицы что украли гоблины у старого мага")
            print('Окончательно придя в сознание ты понимаешь что на тебе нет нечего кроме штанов от поддоспешника а твои сверкающие латы, на зачарку которых ты потратил целое состояние, кудато безследно исчезли')
            print('Когда зрение сфокусировалось ты увидел что стоишь посреди пустой комнаты типичного подземелья каких ты повидал не мало, а в нос ударил привычный запах сырости с легким привкусом плесени ')
            print('В комнате нечего нет кроме двери, ты в который раз уже задаешься вопросом о необходимости этой комнаты, но вспоминания о паре которотких разговоров с группой архитекторов сразу отбивает любое желание искать здесь какую либо логику')

            while True:

                inp = input('И что же ты будешь делать?\n1.Подойти и открыть дверь\n2.Не ну а что ты еще хотел, здесь больше нечего нет\n')
                if inp == '1':
                    print('Дверь,что удивительно, легко открылась с небольшим скрипом и ты попадаешь в следующую комнату')
                    i = input()
                    system('cls||clear')
                    player.room = 2
                    break
                if inp == '2':
                    system('cls||clear')
                    if self.try1 == 1:
                        print('Тут серьезно больше нечего нет')
                    elif self.try1 == 2:
                        print('Голые стены, прекраснейший запах подземелья и ДВЕРЬ,хмммм что же делать.... ')
                    elif self.try1 == 3:
                        print('Я уверяю тебя, тут больше нечего нет')
                    elif self.try1 == 4:
                        print('На, так уж и быть, на потолке свисал гриб, который свалился прямо тебе на голову. Надеюсь теперь ты пойдешь дальше')
                        player.grab('Странный гриб')
                    elif self.try1 == 5 :
                        print('Ну все, теперь точно надоел')
                        print('Из-за твоей спины открылся портал кудато в тундру, подул сильный ветер и ты уносимый потоками ветра на высокой скорости влетаешь головой в дверь и попадаешь в следующую комнату')
                        player.dmg(5)
                        player.room = 2
                        break
                    self.try1 += 1
            if self.ent ==2:
                print('Все те же голые стены и нечего интересного')
                while True:
                    imp = input('Что ты будешь делать?\n1.Покинуть эту комнату\n')
                    if imp == '1':
                        player.room= 2
                        break
                    else:
                        print('Неправельная команда')


class secondroom (room):

    def __init__(self):
        super().__init__()
        self.save = [0]*3 # 0 облутанный труп 1 цельность зеркала 2 открытие двери

    def enter(self,player):
        if self.ent==0:
            self.ent += 1
            print('')
