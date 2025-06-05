my_input = input("好きなスポーツは？")

with open("SportsQuestion_Answer.txt","w") as f:
    f.write(f"{my_input}")
