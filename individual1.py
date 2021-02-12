# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 14. Создать класс Payment (зарплата). В классе должны быть представлены поля: фамилия-
# имя-отчество, оклад, год поступления на работу, процент надбавки, подоходный налог,
# количество отработанных дней в месяце, количество рабочих дней в месяце, начисленная и
# удержанная суммы. Реализовать методы:
# вычисления начисленной суммы,
# вычисления удержанной суммы,
# вычисления суммы, выдаваемой на руки,
# вычисления стажа. Стаж вычисляется как полное количество лет, прошедших от года
# поступления на работу, до текущего года.
# Начисления представляют собой сумму, начисленную за отработанные дни, и
# надбавки, то есть доли от первой суммы. Удержания представляют собой отчисления в
# пенсионный фонд (1% от начисленной суммы) и подоходный налог. Подоходный налог
# составляет 13% от начисленной суммы без отчислений в пенсионный фонд.


class Payment:

    def __init__(self, full_name=' ', salary=0, year=0, percent=0, days_worked=0, working_days=1):
        self.full_name = str(full_name)
        self.salary = int(salary)
        self.year = int(year)
        self.percent = float(percent)
        self.days_worked = int(days_worked)
        self.working_days = int(working_days)

    def read(self):
        full_name = input('Введите свое полное имя: ')
        salary = input('Введите зарплату: ')
        year = input('Введите год присоединения: ')
        percent = input('Введите процент премии: ')
        days_worked = input('Введите количество отработанных дней в месяце: ')
        working_days = input('Введите количество рабочих дней в месяце: ')

        self.full_name = full_name
        self.salary = int(salary)
        self.year = int(year)
        self.percent = float(percent)
        self.days_worked = int(days_worked)
        self.working_days = int(working_days)

    def display(self):
        print(f"{self.full_name}")
        print(f"{self.salary}")
        print(f"{self.year}")
        print(f"{self.percent}")
        print(f"{self.days_worked}")
        print(f"{self.working_days}")

    def accrued_amount(self):
        a = self.salary / self.working_days
        b = a * self.days_worked
        percent = self.percent / 100 + 1
        return b * percent

    def withheld_amount(self):
        b = (self.salary / self.working_days) * self.days_worked
        return b * (0.13 + 0.01)

    def handed_amount(self):
        a = self.salary / self.working_days
        b = a * self.days_worked
        percent = self.percent / 100 + 1
        return b * percent - (self.salary / self.working_days) * self.days_worked

    def experience(self):
        return 2020 - self.year


if __name__ == '__main__':
    r1 = Payment()
    r1.read()
    r1.display()
    print(r1.accrued_amount())
    print(r1.withheld_amount())
    print(r1.handed_amount())
    print(r1.experience())