# -*- coding: utf-8 -*-
import sys
import os
import shutil
from quiz import start_quiz
from bank_account import start_operations


def get_files(folder):
    return [file for file in os.listdir() if os.path.isfile(os.path.join(folder, file))]


def get_folders(folder):
    return [file for file in os.listdir() if not os.path.isfile(os.path.join(folder, file))]


if __name__ == '__main__':
    done = False
    while not done:
        print("1 - создать папку")
        print("2 - удалить (файл/папку)")
        print("3 - копировать (файл/папку)")
        print("4 - просмотр содержимого рабочей директории")
        print("5 - посмотреть только папки")
        print("6 - посмотреть только файлы")
        print("7 - просмотр информации об операционной системе")
        print("8 - создатель программы")
        print("9 - играть в викторину")
        print("10 - мой банковский счет")
        print("11 - смена рабочей директории")
        print("12 - выход")

        choice = int(input())

        if choice == 1:
            name = input("Имя папки: ")
            os.mkdir(name)

        elif choice == 2:
            name = input("Имя папки/файла для удаления: ")
            if name == 'venv':
                raise ValueError("Это системная папка!")
            os.rmdir(name)

        elif choice == 3:
            old = input("Имя папки/файла для копирования: ")
            new = input("Новое имя: ")
            shutil.copy(old, new)

        elif choice == 4:
            [print(element) for element in os.listdir()]

        elif choice == 5:
            print(get_folders(os.getcwd()))

        elif choice == 6:
            print(get_files(os.getcwd()))

        elif choice == 7:
            print(f'System: {sys.platform}')

        elif choice == 8:
            print("Создатель программы - Великий и Ужасный Гриценко Илия!")

        elif choice == 9:
            start_quiz()

        elif choice == 10:
            start_operations()

        elif choice == 11:
            get_folders(os.getcwd())
            name = input("Введите имя новой рабочей директории: ")
            if os.path.exists(name):
                os.chdir(name)
                print(os.getcwd())
            else:
                print("Директория не найдена")

        elif choice == 12:
            done = True

        else:
            print("Нет действия для введенного значения")