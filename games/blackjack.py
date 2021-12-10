import os

from random import shuffle
from time import sleep
from math import floor

from colorama import init
from colorama import Fore, Back

start_money = 1000
min_bet = start_money // 10


init(autoreset=True)


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def card_value(self):
        """ Возращает количество очков которое дает карта """
        if self.rank in "TJQK":
            return 10
        return " A23456789".index(self.rank)

    def get_rank(self):
        return self.rank

    def __str__(self):
        return f"{self.rank}{self.suit}"


class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        """ Добавляет карту на руку """
        self.cards.append(card)

    def get_value(self):
        """ Метод получения числа очков на руке """
        result = 0
        aces = 0
        for card in self.cards:
            result += card.card_value()
            if card.get_rank() == "A":
                aces += 1
        if result + aces * 10 <= 21:
            result += aces * 10
        return result

    def __str__(self):
        text = f"Карты {self.name}:\n"
        for card in self.cards:
            text += str(card) + " "
        text += "\nОчки: " + str(self.get_value())
        return text


class Deck:
    def __init__(self):
        ranks = "23456789TJQKA"
        suits = "DCHS"
        self.cards = [Card(r, s) for r in ranks for s in suits]
        shuffle(self.cards)

    def deal_card(self):
        """ Функция сдачи карты """
        return self.cards.pop()


class Game:
    def __init__(self):
        self.clear()
        self.money = start_money

    @staticmethod
    def clear():
        os.system(("clear", "cls")[os.name == "nt"])

    def get_bet(self):
        print('Ваши деньги:', self.money, 'руб.', end="\n")
        bet = input('Ставка <Q - min> <W - 0.5> <E - max>: ').lower()
        if bet == 'q' or bet == 'й':
            bet = min_bet
        elif bet == 'w' or bet == 'ц':
            bet = floor(self.money / 2)

        elif bet == 'e' or bet == 'у':
            bet = self.money
        else:
            try:
                bet = int(bet)
            except ValueError:
                bet = min_bet
        if bet < min_bet:
            print('Минимальная ставка ' + str(min_bet) + '\n')
            return
        if bet > self.money:
            print('У вас нет столько!\n')
            return

        d = Deck()  # создаем колоду

        player_hand = Hand("Игрок")  # задаем "руки" для игрока и дилера
        dealer_hand = Hand("Диллер")

        player_hand.add_card(d.deal_card())  # сдаем две карты игроку
        player_hand.add_card(d.deal_card())

        dealer_hand.add_card(d.deal_card())  # сдаем одну карту дилеру
        print(Fore.YELLOW + str(dealer_hand))
        print("=" * 20)
        print(Fore.CYAN + str(player_hand))
        # Флаг проверки необходимости продолжать игру
        in_game = True
        # набирать карты игроку имеет смысл только если у него на руке меньше 21 очка
        i = 0
        if player_hand.get_value() == 21:
            print(Fore.GREEN + "БЛЕКДЖЕК!\n")
            self.money += floor(bet * 1.5)
            in_game = False
        while player_hand.get_value() < 21:

            ans = input("Add or Stand? (a/s) ").lower()
            if ans == "a" or ans == 'ф':
                player_hand.add_card(d.deal_card())
                print(Fore.CYAN + str(player_hand))

                # Если у игрока перебор - дилеру нет смысла набирать карты
                if player_hand.get_value() > 21:
                    print(Fore.RED + "Ты проиграл, перебор\n")
                    in_game = False
                    self.money -= bet
                else:
                    i += 1
            else:
                print("Ты остаешься!")
                break
        print("=" * 20)
        if in_game:
            # По правилам дилер обязан набирать карты пока его счет меньше 17
            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(d.deal_card())
                print(Fore.YELLOW + str(dealer_hand))
                sleep(0.7)
                # Если у дилера перебор играть дальше нет смысла - игрок выиграл
                if dealer_hand.get_value() > 21:
                    print(Fore.GREEN + "Ты выиграл, у диллера перебор\n")
                    self.money += bet
                    in_game = False
        if in_game:
            # Ни у кого не было перебора - сравниваем количество очков у игрока и дилера.

            if player_hand.get_value() > dealer_hand.get_value():
                print(Fore.GREEN + "Ты выиграл\n")
                self.money += bet

            elif player_hand.get_value() == dealer_hand.get_value():
                print(Fore.MAGENTA + "Ничья\n")

            else:
                print(Fore.RED + "Ты проиграл\n")
                self.money -= bet

    def cycle(self):
        while True:
            self.clear()
            if self.money < min_bet:
                print(Back.WHITE + Fore.RED + 'ТЫ БАНКРОТ!')
                self.money = start_money
                sleep(1)
                continue
            self.get_bet()
            sleep(1)


if __name__ == '__main__':
    game = Game()
    game.cycle()
