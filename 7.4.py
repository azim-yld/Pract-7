import random

group1 = ['Петров', 'Сидоров', 'Иванов', 'Кузнецов', 'Смирнов', 
            'Васильев', 'Попов', 'Новиков', 'Федоров', 'Морозов']
group2 = ['Иванов', 'Соколов', 'Лебедев', 'Козлов', 'Волков', 
               'Зайцев', 'Павлов', 'Семенов', 'Голубев', 'Виноградов']

#a
team1 = random.sample(group1, 5)
team2 = random.sample(group2, 5)
teams = tuple(team1 + team2)

#b
print("Группа 1: ", group1)
print("Группа 2: ", group2)
print("Спортивная команда: ", teams)

#c
print("Численность команды: ", len(teams), " человек")

#d
sort_team = tuple(sorted(teams))
print("Отсортированная команда:", sort_team)

#e
ivanov = teams.count('Иванов')
if 'Иванов' in teams:
    print("Студент Иванов входит в команду (встречается ", ivanov, " раза)")
else:
    print("Студент Иванов не входит в команду")