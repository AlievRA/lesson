import random
point = 100
game = True
while game:
    counter = int(input("Введите любое число от 2 до 12"))
    bet = int(input("Введите ставку"))
    counter2 = random.randint(1, 6)
    counter3 = random.randint(1, 6)
    if counter2 + counter2 < 7 and counter < 7:
        point += bet
        print(f"Ты выиграл! Твой баланс {point}")
    elif counter2 + counter2 > 7 and counter > 7:
        point += bet
        print(f"Ты выиграл! Твой баланс {point}")
    elif counter2 + counter2 == 7:
        stavka = bet * 4
        point += bet
        print(f"Ты выиграл x4! Твой баланс {point}")
    else:
        point -= bet
        print(f"Ты проиграл! Твой баланс {point}")
    

    if point <= 0:
        print("У тебя закончились очки!")
        game = False
    else:
        answer = input("Продолжаем играть да/нет?")
        if answer == "нет":
            print("Спасибо, что поиграл!")
            game = False

