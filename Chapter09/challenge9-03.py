import csv

my_list = [["Top Gun","Risky Business","Minority Report"],
           ["Titanic","The Revenant","Inception"],
           ["Training Day","Man on Fire","Flight"]]

with open("Title1.csv","w") as f:

    w = csv.writer(f, delimiter = ",")

    for i in my_list:
        w.writerow(i)
