def change(string):
    try:
        return float(string)
    except ValueError:
        print("小数点にできない")
"""
関数名: change
:引数: string :型: str
:戻り値: string :型: str
"""
c = change("55.0")
print(c)

