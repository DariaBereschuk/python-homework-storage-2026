

#В зависимости от задания, которое хотите посмотреть меняйте номер таска

if __name__ == "__main__":
    task1()



#1.
def task1():
    users_input = input("Введите вашу последовательность через запятую \n")
    users_list = users_input.split(",")
    users_set = set(users_list)
    if len(users_list) == len(users_set):
        print("Элементы различны")
    else:
        print("Элементы не уникальны")

#2.
def task2():
    classes = ["физика","структуры данных","вышмат","ботаника","физхим"]
    students = []
    quantity_students = int(input("Сколько студентов вы введете? \n"))
    for i in range(quantity_students):
        name = input("Введите фамилию студента \n")
        grades = []
        for c in classes:
            while True:
                try:
                    g = int(input(f"Оценка по курсу {c} студента {name}: \n"))
                    grades.append(g)
                except ValueError:
                    print("Введите целое число")
                    continue
                if 3 <= g <= 5:
                    break
                else:
                    print("Оценки от 3 до 5")
        student = (name, grades)
        students.append(student)
    grades_by_classes = {c: [] for c in classes}
    for name, grades in students:
        for i, g in enumerate(grades):
            grades_by_classes[classes[i]].append(g)
    for c, g in grades_by_classes.items():
        avg = sum(g) / len(g)
        print(f'Для курса "{c}"":\n '
              f'среднее значение {avg}\n '
              f'минимальное значение {min(g)}\n '
              f'максимальное значение {max(g)}')

#3.
def task3():
    users_tuple = tuple(input("Введите строку слов, разделенных пробелами \n").split())
    unique_el = len(set(users_tuple))
    vowels = set("аеёиоуыэюя")
    consonants = set("бвгджзйклмнпрстфхцчшщ")
    punctuation_marks = set(".,;:?\"!-'")
    vowels_count = 0
    consonants_count = 0
    punct_count = 0
    for word in users_tuple:
        for letter in word:
            if letter.lower() in vowels:
                vowels_count += 1
            elif letter.lower() in consonants:
                consonants_count += 1
            elif letter.lower() in punctuation_marks:
                punct_count += 1
            else:
                continue
    print(f"Уникаальных слов {unique_el}\n"
          f"Всего {vowels_count} гласных, {consonants_count} согласных, {punct_count} знаков пунктуации")

#4. Две функции, для шифровки и расшифровки. В зависимости от пользовательского ввода task4 выбирает какую из них использовать

letters_to_num = {"а": "01", "б": "02", "в": "03", "г": "04", "д": "05",
    "е": "06", "ё": "07", "ж": "08", "з": "09", "и": "10",
    "й": "11", "к": "12", "л": "13", "м": "14", "н": "15",
    "о": "16", "п": "17", "р": "18", "с": "19", "т": "20",
    "у": "21", "ф": "22", "х": "23", "ц": "24", "ч": "25",
    "ш": "26", "щ": "27", "ъ": "28", "ы": "29", "ь": "30",
    "э": "31", "ю": "32", "я": "33", ".":"34", ",":"35", "!":"36", "?":"37", ":":"38", "-":"39", " ":"40"}

num_to_letters = {"01": "а", "02": "б", "03": "в", "04": "г", "05": "д",
    "06": "е", "07": "ё", "08": "ж", "09": "з", "10": "и",
    "11": "й", "12": "к", "13": "л", "14": "м", "15": "н",
    "16": "о", "17": "п", "18": "р", "19": "с", "20": "т",
    "21": "у", "22": "ф", "23": "х", "24": "ц", "25": "ч",
    "26": "ш", "27": "щ", "28": "ъ", "29": "ы", "30": "ь",
    "31": "э", "32": "ю", "33": "я","34": ".","35": ",","36": "!","37": "?","38": ":","39": "-","40": " "}

def encode(users_input):
    text = users_input.lower()
    result = []
    for el in text:
        if el in letters_to_num:
            new_el = letters_to_num[el]
            result.append(new_el)
        else:
            continue
    filal_result=str("".join(result))
    print(f"{filal_result}")

def decode(users_input):
    text = users_input.lower()
    result = []
    for i in range(0, len(text), 2):
        couple_el = text[i:i+2]
        if couple_el in num_to_letters:
            result.append(num_to_letters[couple_el])
        else:
            continue
    filal_result = str("".join(result))
    print(f"{filal_result}")

def task4():
    users_input = input("Введите свой текст\n")
    if users_input.isdigit():
        return decode(users_input)

    for el in users_input:
        if el.lower() not in letters_to_num:
            print("Буквы и цифры мешать нельзя")
            return None
    else:
        return encode(users_input)

#5. Структура как в 4. отделно написаны 2 сценария, в зависимости от ввода пользователья выбирается один из них

def legs(): #В случае, если ищем гипотенузу по двум катетам
    a = int(input("Введите числом длину первого катета\n"))
    b = int(input("Введите числом длину второго катета\n"))
    if a <= 0 or b <= 0:
        print("Сторона не может быть отрицательной или нулевой")
        return None
    c = (a ** 2 + b ** 2) ** 0.5
    print(f"Третья сторона (гипотенуза) равна {c:.2f}")

def not_legs(): #Второй сценарий, если ищем по катету и гипотенузе
    a = int(input("Введите числом длину катета\n"))
    c = int(input("Введите числом длину гипотенузы\n"))
    if a <= 0 or b <= 0:
        print("Сторона не может быть отрицательной или нулевой")
        return None
    b = (c**2 - a**2) ** 0.5
    print(f"Третья сторона (катет) равна {b:.2f}")

def task5():
    ask1 = input("Ваши стороны это катеты? Введите да/нет\n")
    if ask1.lower() == "да":
        return legs()
    else:
        ask2 = input("Ваши стороны это катет и гипотинуза? Введите да/нет\n")
        if ask2.lower() == "да":
            return not_legs()
        else:
            print("Предполагаю, что катеты и отказываюсь от ответственности за неверный результат\n")
            return legs()

