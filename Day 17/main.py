from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question = i['text']
    answer = i['answer']
    new_question = Question(question, answer)
    question_bank.append(new_question)
print(question_bank)

quiz = QuizBrain(question_bank)
quiz.next_question()
question_end = False

while quiz.still_has_questions():
    quiz.next_question()

print("Congratulations, You have completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_num}")