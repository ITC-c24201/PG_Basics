def f(str):
    """
    引数で受け取った文字列をfloatに変換して返す
    """
    return float(str)

try:
    print(f("Hello"))
except ValueError:
    print("str is not number")
