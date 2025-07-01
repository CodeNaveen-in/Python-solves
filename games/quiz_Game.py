class Question():
    def __init__(self, ques, ans):
        self.ques = ques
        self.ans = ans

class QuizBrain():
    def __init__(self, question_list):
        self.q_num = 0
        self.q_list = question_list
        self.score = 0
    
    def next_question(self):
        current_question = self.q_list[self.q_num]
        self.q_num += 1
        user_ans = input(f"Q.{self.q_num}: {current_question.ques} True or False: ")
        self.check_answer(user_ans, current_question.ans)
    
    def still_has_questions(self):
        return (self.q_num != len(self.q_list))
    
    def check_answer(self, user_ans, q_ans):
        if (user_ans.lower() == str(q_ans).lower()):
            print("You got it right")
            self.score += 1
        else:
            print("That's a wrong ANSWER")
        print("The correct answer was ", q_ans)
        print(f"{self.score}/ {self.q_num}")


question_bank = [
    {"The capital of Australia is Sydney.": False},
    {"The Great Wall of China is visible from space.": False},
    {"Python is a programming language.": True},
    {"Sharks are mammals.": False},
    {"The sun is a star.": True},
    {"Sound travels faster than light.": False},
    {"There are 365 days in a year.": True},
    {"Lightning never strikes the same place twice.": False},
    {"The chemical symbol for gold is Au.": True},
    {"Humans have more than five senses.": True}
]

q_obj = [] 
#made just to practice new data upload
#can also use openTrivia DB to fetch question via API calls 
for i in question_bank:
    for ques, ans in i.items():
        q=Question(ques, ans)
        q_obj.append(q)

nas = QuizBrain(q_obj)
while nas.still_has_questions():
    nas.next_question()

print("Congrats quiz has been finished")
print(f"Your score was {nas.score} / {nas.q_num}")