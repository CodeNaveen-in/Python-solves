#import csv #can also do it to operate more precisely

with open ("./weather_data.csv") as file:
    #content = csv.reader(file)
    content = file.readlines()
    temperature = []
    for i in content:
        print (i)
        s = i.split(",")
        temperature.append(s[1])
print(temperature)