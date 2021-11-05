# asyncio-factorial
Пример синхронного и асинхронного расчета факториалов (Python 3.8+)
## Как это работает
### Планирование конкуретного исполнения корутин
Асинхронная корутина **task_factory(num)** запускает цикл с  количеством итераций от 2 до _num_, и в каждой итерации во-первых генерирует новое имя таски, а во-вторых регистрирует новую таску с только что сгенерированным именем и текущим значением итератора _iter_ в качестве аргумента. Каждая созданная таска добавляется в список **tasks**.
```python
iter = 2
# Запланировать конкурентные задачи:
while iter <= num:
    task_name = 'Задача {0}'.format(iter-1)
    task = asyncio.create_task(
        factorial_async(task_name, iter), name=task_name)
    tasks.append(task)
    iter += 1
```
### Результат выполнения всех запланированных корутин
Далее все добавленные в список **tasks** корутины запускаются _конкурентно_: 
```python
results = await asyncio.gather(*tasks)
```
Все результаты, возвращенные корутинами, содержатся в списке **results**. Например, для поданного на вход task_factory() значения 5 результаты выполнения всех корутин будет следующим:
```json
[{'task': 'Задача 1', 'num': 2, 'f': 2}, 
 {'task': 'Задача 2', 'num': 3, 'f': 6}, 
 {'task': 'Задача 3', 'num': 4, 'f': 24}, 
 {'task': 'Задача 4', 'num': 5, 'f': 120}]
```
 
