import random
point = 100
game = True
while game:
    counter = int(input("Введите любое число от 2 до 12 - "))
    if counter < 2 or counter > 12:
        print("Введите корректное число!")
        continue
    bet = int(input("Введите ставку - "))
    if bet > point or bet < 1:
        print("Введите корректное число!")
        continue
    counter2 = random.randint(1, 6)
    counter3 = random.randint(1, 6)
    if counter2 + counter2 == counter:
        bet = bet * 4
        point += bet
        print(f"Ты выиграл x4! Твой баланс {point}")
    elif counter2 + counter2 < 7 and counter < 7:
        point += bet
        print(f"Ты выиграл! Твой баланс {point}")
    elif counter2 + counter2 > 7 and counter > 7:
        point += bet
        print(f"Ты выиграл! Твой баланс {point}")
    else:
        point -= bet
        print(f"Ты проиграл! Твой баланс {point}")
    

    if point <= 0:
        print("У тебя закончились очки!")
        game = False
    else:
        answer = input("Продолжаем играть да/нет? ")
        if answer == "нет":
            print("Спасибо за игру!")
            game = False
