import csv

my_list = [["トップガン","リスキービジネス","マイノリティレポート"],
           ["タイタニック","ザ・レヴナント","インセプション"],
           ["トレーニングデイ","マン・オン・ファイア","フライト"]]


with open("Title2.csv","w", newline = "") as f:
    
    w = csv.writer(f, delimiter = ",")

    for i in my_list:
        w.writerow(i)
