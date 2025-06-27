#TODO 1. Set up the data in dictionary. {Name: [followers, description, country ]}
#TODO 2. Fetch the data to show comparison - present name , description and country and compare choice
#TODO 3. If choice is correct increase score and continue else complete the game and present the score

import random 
print(r"""
      ▲
     ▲ ▲      HIGH OR LOW 🎯
   ▲     ▲    
  ▼     ▼
   ▼   ▼
    ▼ ▼
     ▼
 Guess if the next is ↑ or ↓!
""")
internet_personalities = {
    "MrBeast": [250_000_000, "YouTuber known for philanthropy", "United States"],
    "Khaby Lame": [160_000_000, "Silent comedy TikTok creator", "Italy"],
    "Charli D'Amelio": [150_000_000, "TikTok dance sensation", "United States"],
    "Zach King": [100_000_000, "Magic video illusionist", "United States"],
    "CarryMinati": [40_000_000, "Indian roasting comedian", "India"],
    "Addison Rae": [90_000_000, "TikTok dancer and actress", "United States"],
    "Lilly Singh": [38_000_000, "Comedian and talk show host", "Canada"],
    "PewDiePie": [110_000_000, "Gaming and meme YouTuber", "Sweden"],
    "NikkieTutorials": [20_000_000, "Beauty and makeup vlogger", "Netherlands"],
    "Bhuvan Bam": [25_000_000, "Comedy singer from India", "India"],
    "Emma Chamberlain": [30_000_000, "Vlogger and podcast host", "United States"],
    "Dude Perfect": [60_000_000, "Trick-shot sports crew", "United States"],
    "Dixie D'Amelio": [60_000_000, "Singer and TikTok star", "United States"],
    "Gaurav Taneja": [10_000_000, "Flying Beast fitness vlogger", "India"],
    "IShowSpeed": [35_000_000, "Energetic gaming livestreamer", "United States"],
    "LaurenZside": [7_000_000, "Funny gaming content", "United States"],
    "Wengie": [13_000_000, "DIY and pop music creator", "Australia"],
    "KSI": [40_000_000, "YouTuber and boxer from Sidemen", "United Kingdom"],
    "Saloni Gaur": [2_000_000, "Satirical Indian comedian", "India"],
    "Jay Shetty": [25_000_000, "Spiritual coach and author", "United Kingdom"]
}

def person(dicti):
    person = random.choice(list(dicti.keys()))
    return person

def print_person(person):
    print(f"We have {person} as the person, who do {internet_personalities[person][1]} and belongs from {internet_personalities[person][2]}")

def followers(person, ditci):
    fol = ditci[person][0]
    return fol

def compare(p1, p2):
    p1_fol = followers(p1, internet_personalities)
    p2_fol = followers(p2, internet_personalities)
    if (p2_fol > p1_fol):
        return "higher"
    elif (p2_fol == p1_fol):
        return "same"
    elif (p2_fol < p1_fol):
        return "lower"


print("Welcome to the game of HIGHER or LOWER.. \n Rule: The aim is to keep getting more points\n")
p1 = person(internet_personalities)
chance = 1
final_score = 0

while (chance == 1):
    p2 = person(internet_personalities)
    print_person(p1)
    print_person(p2)
    ask = input(f"So now for the one named {p2} : Higher, lower or same? \t:").lower()
    if (compare(p1, p2) == ask):
        final_score += 1
        p1 = p2
        print(f"Wooho you're right, {ask} was correct answer. Your score has increased by 1 making it {final_score}\n")
    else:
        print("Your answer was wrong and you lost..")
        chance = 0

print("\nHope you enjoyed the game!!!")
print(f"Your score was {final_score} ")
