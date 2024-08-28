import quiz_data
import random
class Question:
    def __init__(self,text,answer):
        self.text=text
        self.answer=answer

question_bank=[]
for question in quiz_data.question_data:
    text=question['text']
    answer=question['answer']
    question_bank.append(Question(text,answer))

class QuizBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.question_list=question_list
        self.score=0

    def still_has_question(self):
        if self.question_number<len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_ques=self.question_list[self.question_number]
        self.question_number+=1
        ques=input(f"Q.{self.question_number} {current_ques.text} (True/False) : ")
        self.check_answer(ques,current_ques.answer)
    def check_answer(self,ques,correct_answer):
        if ques.lower()==correct_answer.lower():
            print("You got it right !")
            self.score+=1
        else:
            print("You got it wrong !!!")
            print(f"The correct answer was {correct_answer}")
        print(f"your score : {self.score}/{quiz.question_number}")

quiz=QuizBrain(question_bank)
score=0
while quiz.still_has_question():
    quiz.next_question()
    print()
print("You've completed the quiz")
print(f"Final score = {quiz.score}/{quiz.question_number}")
    
                
    

    
