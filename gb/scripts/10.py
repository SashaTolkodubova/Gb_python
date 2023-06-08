# Задание по лекции
# | Задание 44 |
# | --- |
# | В ячейке ниже представлен код генерирующий DataFrame,
# которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?
#
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head() |
# Статья про one hot вид
#

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
# print(pd.get_dummies(data['whoAmI']))
data.loc[data['whoAmI'] == 'human', 'human'] = True
data.loc[data['whoAmI'] == 'robot', 'robot'] = True
del (data['whoAmI'])
data.loc[data['human'].isnull(), 'human'] = False
data.loc[data['robot'].isnull(), 'robot'] = False


# print(data)


# |Задание на выбор или дополнительное про классы (тема 10ого семинара)|
#
# Напишите класс Dragon (Дракон), экземпляр которого при инициализации
# принимaет аргументы:
# рост, огнеопасность, цвет.
#
# Класс обеспечивает выполнение методов (dr — экземпляр класса)
# экземпляры можно сравнивать: сначала по росту. затем по огнеопасности,
# затем по цвету по алфавиту
#
# экземпляры класса можно складывать: dr2 =dr + dr1. при этом
# возвращается новый экземпляр со значениями атрибутов:
#
# цвет меньший по алфавиту;
# рост - среднее арифметическое из двух округлённое до целого вниз,
# огнеопасность - большее из двух;
#
# из экземпляра класса можно вычесть число: dr -= number, из
# роста вычитается целая честь от деления роста на число, к
# огнеопасности прибавляется остаток от деления огнеопасности на число;

# Экземпляр можно вызвать с аргументом-строкой - возвращается строка-аргумент,
# повторенная количество раз, равное
# значению атрибута огнеопасность;
#
# change_color() - вызывается c аргументом - цветом, на который нужно
# поменять имеющийся цвет
#
# str- возвращает строку:
# Dragon with height «рост», danger <огнеопасность> and color «цвет».
#
# repr- возвращaет строку:
# Dragon(‹рост>, <огнеопасность>, <цвет>)
#
# Пример
#
# dr = Dragon(69, 5, “brown™)
# dr1 = Dragon(69, 5, “gray")
# print (dr > dr1, dr != dr1, dr <= dr1)
# print(dr, dr1, sep="\n")
# print()
#
# dr.change_color("white")
# dr -= 23
# dr1 -= 2
# dr2 = dr+dr1
# print(dr, dr1, dr2, sep="\n")
#
# print(dr("Welcome")
#
# Вывод
#
# False True True
# Dragon with height 69, danger 5 and color brown.
# Dragon with height 69, danger 5 and color gray.
#
# Dragon with height 66, danger 10 and color white.
# Dragon with height 35, danger 6 and color gray.
# Dragon with height 50, danger 10 and color brown.
# WelcomeWelcomeWelcomeWelcomeWelcome

class Dragon:
    def __init__(self, height=0, flammability=0, color=''):
        if type(height) != int:
            raise ValueError('height must be int')
        if type(flammability) != int:
            raise ValueError('flammability must be int')
        if type(color) != str:
            raise ValueError('color must be str')
        self.height = height
        self.flammability = flammability
        self.color = color

    # ==
    def __eq__(self, other):
        return (type(self) == type(other)) and \
            (self.height == other.height) and \
            (self.flammability == other.flammability) and \
            (self.color == other.color)

    # !=
    def __ne__(self, other):
        return (type(self) != type(other)) or \
            (self.height != other.height) or \
            (self.flammability != other.flammability) or \
            (self.color != other.color)

    # >=
    def __ge__(self, other):
        if type(self) != type(other):
            raise ValueError('They must be dragons!')
        if self.height > other.height:
            return True
        elif self.height == other.height:
            if self.flammability > other.flammability:
                return True
            elif self.flammability == other.flammability:
                if self.color >= other.color:
                    return True
        return False

    # <=
    def __le__(self, other):
        if type(self) != type(other):
            raise ValueError('They must be dragons!')
        if self.height < other.height:
            return True
        elif self.height == other.height:
            if self.flammability < other.flammability:
                return True
            elif self.flammability == other.flammability:
                if self.color <= other.color:
                    return True
        return False

    # >
    def __gt__(self, other):
        if type(self) != type(other):
            raise ValueError('They must be dragons!')
        if self.height > other.height:
            return True
        elif self.height == other.height:
            if self.flammability > other.flammability:
                return True
            elif self.flammability == other.flammability:
                if self.color > other.color:
                    return True
        return False

    # <
    def __lt__(self, other):
        if type(self) != type(other):
            raise ValueError('They must be dragons!')
        if self.height < other.height:
            return True
        elif self.height == other.height:
            if self.flammability < other.flammability:
                return True
            elif self.flammability == other.flammability:
                if self.color < other.color:
                    return True
        return False

    # +
    def __add__(self, other):
        if type(self) != type(other):
            raise ValueError('They must be dragons!')

        new_instance = Dragon()
        new_instance.height = int(((self.height + other.height) / 2) // 1)

        new_instance.flammability = \
            self.flammability if \
            self.flammability > other.flammability \
            else other.flammability

        new_instance.color = \
            self.color if self.color < other.color else other.color

        return new_instance

    def __isub__(self, other):
        self.height -= int(self.height // other)
        self.flammability += int(self.flammability % other)
        return self

    def __call__(self, other):
        return other * self.flammability

    def change_color(self, color):
        self.color = color

    def __str__(self):
        return f'Dragon with height {self.height}, ' \
               f'danger {self.flammability} and color {self.color}.'

    def __repr__(self):
        return f'Dragon({self.height}, {self.flammability}, {self.color})'
