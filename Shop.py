x = input("Введите 'Start': ")
b = 200
c = 150
y = 100
n = 150
Balance = 500

if x=="Start" or x=="start":
    print(f"Ваш баланс: {Balance}")
    print(f"1)Цветы - {y}",
          f"2)Игрушка - {b}",
          f"3)Фрукты - {c}",
          f"4)Конфеты - {n}"
          )
while Balance !=0:
    m = int(input("Введите номер товара: "))
    if m == 1:
        Balance = Balance - y
        if Balance<0:
            Balance = Balance + y
            print("Недостаточно средств")
        else:
            print("Вы купили Цветы")
            print(f"Ваш баланс: {Balance}")
            print(f"1)Цветы - {y}",
                  f"2)Игрушка - {b}",
                  f"3)Фрукты - {c}",
                  f"4)Конфеты - {n}"
                 )
    elif m == 2:
        Balance = Balance - b
        if Balance<0:
            Balance = Balance + b
            print("Недостаточно средств")
        else:
            print("Вы купили Игрушку")
            print(f"Ваш баланс: {Balance}")
            print(f"1)Цветы - {y}",
                  f"2)Игрушка - {b}",
                  f"3)Фрукты - {c}",
                  f"4)Конфеты - {n}"
                 )
    elif m == 3:
            Balance = Balance - c
            if Balance<0:
                Balance = Balance + c
                print("Недостаточно средств")

            else:
                print("Вы купили Фрукты")
                print(f"Ваш баланс: {Balance}")
                print(f"1)Цветы - {y}",
                      f"2)Игрушка - {b}",
                      f"3)Фрукты - {c}",
                      f"4)Конфеты - {n}"
                     )
    elif m == 4:
            Balance = Balance - n
            if Balance<0:
                Balance = Balance + n
                print("Недостаточно средств")
            else:
                print("Вы купили Конфеты")
                print(f"Ваш баланс: {Balance}")
                print(f"1)Цветы - {y}",
                      f"2)Игрушка - {b}",
                      f"3)Фрукты - {c}",
                      f"4)Конфеты - {n}"
                     )
print("У вас на балансе 0")
