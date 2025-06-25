def calculate_love_score(name1, name2):
    d1_list= ["t", "r", "u", "e"]
    d2_list= ["l", "o", "v", "e"]
    name = name1.lower()+name2.lower()
    d1 = 0
    d2 = 0
    for i in name:
        if (i in d1_list):
            d1+=1
    for j in name:
        if (j in d2_list):
            d2+=1
    print(str(d1) + str(d2) , "% is the love score of you guys .")

calculate_love_score("true", "love")