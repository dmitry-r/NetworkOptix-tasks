rest-api-task
==========
### Задача 2 - REST API

Написать консольный скрипт, сравнивающий скорость выполнения параллельных и последовательных

запросов к серверу.

- На вход принимается число N - количество запросов

- Скрипт отправляет N запросов последовательно (следующий запрос отправляется сразу после получения ответа на предудыщий) и замеряет суммарное время

- После этого скрипт отправляет N запросов параллельно из разных потоков, дожидается получения всех ответов и замеряет суммарное время

- Нужно вывести оба полученных результата и разницу по времени между ними

Бонус 1

- Разобрать ответ сервера (json)