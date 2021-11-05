#! /usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import os
import datetime
import time

SLEEP = .33

# Функция расчета факториала
def factorial(num):
    f = 1
    print(f"Выполняется вычисление факториала {num}! ...")
    for i in range(2, num + 1):
        f *= i
        time.sleep(SLEEP)
    print(f"Факториал {num}! = {f}")

# Последованиельный расчет факториалов
def calc_factorial(num):
    print('\033[36mСтартовал последовательный расчет факториалов...')
    startedAt = datetime.datetime.now()
    iter = 2
    while iter <= num:
        factorial(iter)
        iter += 1
    finishedAt = datetime.datetime.now()
    duration = (finishedAt - startedAt).total_seconds()
    print('Последовательные расчеты факториалов завершены. \
    \nПродолжительность расчетов {0} cек.'.format(duration))


# Асинхронная корутина расчета факториала
async def factorial_async(name, num):
    f = 1
    print(f"Выполняется {name}: Вычисление факториала {num}! ...")
    for i in range(2, num + 1):
        f *= i
        await asyncio.sleep(SLEEP)
    print(f"Завершена {name}: факториал {num}! = {f}")


# Асинхронная корутина пларирования конкурентых задач
async def task_factory(num):
    print('\033[92mСтартовал асинхронный расчет факториалов...')
    startedAt = datetime.datetime.now()
    tasks = list()
    iter = 2
    # Запланировать конкурентные задачи:
    while iter <= num:
        task_name = 'Задача {0}'.format(iter-1)
        task = asyncio.create_task(factorial_async(task_name, iter), name=task_name)
        tasks.append(task)
        iter += 1
    await asyncio.gather(*tasks)
    finishedAt = datetime.datetime.now()
    duration = (finishedAt - startedAt).total_seconds()
    print('Асинхронные расчеты факториалов завершены. \
    \nПродолжительность расчетов {0} cек.'.format(duration))

# Основная программа
if __name__ == '__main__':
    # Очистка консоли
    os.system('clear')
    num = 0
    while num < 2:
        num = input("Введите число >= 2: ")
        try:
            num = int(num)
        except ValueError:
            num = 0
    # Последовательный расчет факториалов
    calc_factorial(num)
    # Вызов асинхронной "фабрики" конкурентных задач
    asyncio.run(task_factory(num))
