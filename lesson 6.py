books = ["хлеб", "книга", "человек", "рыба", "стол"]
##print(books[0])
##books[3] = "фильм"
##print(books)
##books.append("друг")
##print(books)
##books.remove("друг")
##print(books)
##print(books)
##man = books.index("человек")
##print(man)
##film = books.pop(man)
##print(film)
##print(len(books))
for i in range(len(books)):
    print(f"{i + 1}.{books[i]}")
##
##if "книга" in books:
##    print("У меня есть книга")
##books.append("телефон")
##if "телефон" not in books:
##    print("У меня нет телефона")
##
##else:
##    print("У меня есть телефон")
##
##book = input("Какой предмет вы хотите добавить?")
##if book in books:
##    print(f"Элемент {book} уже есть в списке")
##else:
##    books.append(book)
##    print(f"Элемент {book} добавлен в список")
##
import random
character = ["мудрый", "жизнерадостный", "дерзкий", "умный", "трусливый", "красивый", "высокий", "храмой", "сильный", "бешеный"]
animals = ["тигр", "лев", "сова", "орел", "слон", "страус", "голубь", "медведь", "лиса", "собака", "кот"]
first_name = random.choice(character)
second_name = random.choice(animals)
print(f"В древнем племяни тебя бы звали {first_name} {second_name}")

import random
your_question = input("Привет. Это магический шар. Задавай волнующий тебя вопрос, на который можно ответить 'да' или 'нет' - ")
answers = ("да", "нет", "не могу сейчас сказать")
reply = random.choice(answers)
answers2 = ("Возможно,", "Наверное,", "", "Думаю", "Вероятно,", "К удивлению," "Точно")
reply2 = random.choice(answers2)
##print(f"{reply2} {reply}")
if reply == "не могу сейчас сказать" and reply2 == "Возможно" or reply2 == "Вероятно":
    reply3 = random.choice(answers)
    print(f"{reply2} {reply3}")
else:
    print(f"{reply2} {reply}")











