from collections import namedtuple
from random import sample


Output_dates = namedtuple('output_dates', 'numeric_date words_date')

all_right_answers = {
    "Иосифа Сталина":            Output_dates('06.12.1878', 'шестое декабря 1878 года'),
    "Владимира Высоцкиого":      Output_dates('25.01.1938', 'двадцать пятое января 1938 года'),
    "Виктора Цоя":               Output_dates('21.06.1962', 'двадцать первое июня 1962 года'),
    "Андрея Сахарова":           Output_dates('21.05.1921', 'двадцать первое июля 1921 года'),
    "Юрия Гагарина":             Output_dates('09.03.1934', 'девятое марта 1934 года'),
    "Владимира Жириновского":    Output_dates('25.04.1946', 'двадцать пятое апреля 1946 года'),
    "Сергея Королёва":           Output_dates('12.01.1907', 'двенадцатое января 1907 года'),
    "Андрея Туполева":           Output_dates('10.11.1888', 'десятое ноября 1888 года'),
    "Константина Циолковского":  Output_dates('17.09.1857', 'семнадцатое сентября 1857 года'),
    "Аллы Пугачёвой":            Output_dates('15.04.1949', 'пятнадцатое 1949 года'),
}


def start_quiz():
    done = False
    while not done:

        chosen_right_answers = sample(list(all_right_answers.items()), 5)
        right_answers = {k: v for (k, v) in chosen_right_answers}
        user_answers = {k: None for k in right_answers.keys()}

        names_num = len(right_answers)

        for name in right_answers.keys():
            user_answers[name] = input(f"Введите дату рождения {name} в формате \"dd.mm.yyyy\": ")

            if user_answers[name] != right_answers[name].numeric_date:
                print(f'Неверно!\nПравильный ответ: {right_answers[name].words_date}')

        right_answers_num = 0
        for (right_answer, user_answer) in zip(right_answers.values(), user_answers.values()):
            right_answers_num += int(user_answer == right_answer.numeric_date)

        wrong_answers_num = names_num - right_answers_num
        print(f'Верных ответов: {right_answers_num}')
        print(f'Неверных ответов: {wrong_answers_num}')
        print(f'% верных ответов: {(right_answers_num * 100) / names_num:.1f}%')
        print(f'% неверных ответов: {(wrong_answers_num * 100) / names_num:.1f}%')

        user_input = input("Начать с начала?\n")
        done = True if not user_input.lower() == "да" else False
