Итак, добро пожаловать, кто бы ты нибыл, сверху в зеленой панельке можно скачать проект, никаких библиотек кроме стандартных я не использовал так что тебе понадобится только python 3;
По поводу управления:
В комнатах работает команда 'инвентарь' чтобы его посмотреть;
в бою:
атака - атака расчитывается по формуле урон = сила оружия + бросок силы - броня - бросок ловкости, сила и ловкость определяют верх рандома;
броня - удваивает броню, но так как пока нет возможности получить хоть сколько-нибудь брони нечего не делает;
инвентарь - просмотр инвенторя, но просто просмотр пропускает ход;
зелье - принять зелье лечения, но так как пока их получить невозможно нечего не делает;
основной работающий билд в потоке dungeon_master;
