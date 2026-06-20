n = [11, 32, 33, 15, 1]

while True:
    a = input("1~10の数字を入力してください")
    if a == "q":
        break
    try:
        a = int(a)
    except ValueError:
        print("数字を入力するか、qで終了します")
    if a in numbers:
        print("正解")
    else:
        print("不正解")
