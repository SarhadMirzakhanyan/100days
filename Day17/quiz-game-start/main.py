from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
#print(question_data)

for elem in question_data:
    question_text = elem["question"]
    question_answer = elem["correct_answer"]
    question_bank.append(Question(question_text,question_answer))

#print(question_bank)
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_qustion()