from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for dic in question_data:
    question_bank.append(Question(dic["text"], dic["answer"]))

#print(question_bank)

quizbrain = QuizBrain(question_bank)
while quizbrain.still_has_questions():
    quizbrain.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quizbrain.score}/{quizbrain.question_number}")