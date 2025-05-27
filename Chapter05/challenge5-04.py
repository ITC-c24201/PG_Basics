
my_dict = {"身長":"170",
           "好きな色":"白"}

n = input("キーを入力してください:")


if n in my_dict:
    print(my_dict[n])
else:
    print("キーが間違っています。")
