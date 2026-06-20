n = [5]

while True:
    a = input("数字を入力するか、qで終了します")
    if a == "q":
        break
    try:
        a = int(a)
    except ValueError:
        print("数字を入力してください")
    if a in n:
        print("正解")
    else:
        print("不正解")
