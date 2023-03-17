##def savehall(name):
##    print(f"Hello {name}")
##savehall("Вася")
##savehall("Евгений")
##
##def pl(name, side):
##    abc = name * side
##    print(f"Площадь квадрата = {abc}")
##pl(5, 8)
##pl(4, 9)
##pl(6, 1)
##
##
##def years(name)
##    print("Это список с месяцами года")
##
##years = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
##for k in range(len(years)):
##    print(f"{k + 1}.{years[k]}")
##
##
##import random
##your_question = input("Привет. Это магический шар. Задавай волнующий тебя вопрос, на который можно ответить 'да' или 'нет' - ")
##answers = ("да", "нет", "не могу сейчас сказать")
##reply = random.choice(answers)
##answers2 = ("Возможно,", "Наверное,", "", "Думаю", "Вероятно,", "К удивлению," "Точно")
##reply2 = random.choice(answers2)
####print(f"{reply2} {reply}")
##if reply == "не могу сейчас сказать" and reply2 == "Возможно" or reply2 == "Вероятно":
##    reply3 = random.choice(answers)
##    print(f"{reply2} {reply3}")
##else:
##    print(f"{reply2} {reply}")
import random
def lat():
    tikkets = [1, 2, 3, 100, 555]
    tikket = random.choice(tikkets)
    return tikket
winner = lat()
print(winner)
