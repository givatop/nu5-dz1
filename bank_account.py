from typing import List
from collections import namedtuple


Purchase = namedtuple('Purchase', 'name amount')


def start_operations():
    history = []  # type: List[Purchase]
    account = 0

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        new_purchase = None
        if choice == '1':
            amount = int(input("На какую сумму Вы хотите пополнить счет: "))
            account += amount
            print()

        elif choice == '2':
            amount = int(input("Введите сумму покупки: "))
            if amount > account:
                print("Недостаточно средств\n")
                continue
            name = input("Введите название покупки: ")
            account -= amount
            history.append(Purchase(name, amount))
            print()

        elif choice == '3':
            [print(f'{name} {amount}') for (name, amount) in history]
            print()

        elif choice == '4':
            break
        else:
            print('Неверный пункт меню\n')
