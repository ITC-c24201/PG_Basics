numbers = [0,2,12,6,4]


while True:
    number = input("数字を入力するか、qで終了します")

    if number == "q":
        break

    try:
        number = int(number)
    except ValueError:
        print("数字を入力するか、qで終了します")

    if number in numbers:
        print("正解!")
    else:
        print("不正解!")
