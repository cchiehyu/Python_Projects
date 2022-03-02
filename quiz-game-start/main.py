from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank =[]
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_questions = Question(question_text , question_answer )
    question_bank.append(new_questions)

#TODO: asking the questions
#TODO:checking if the answer is correct
#TODO: checking if we're the end of the quiz

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("Quiz Completed")
print(f"Your final Score is {quiz.score}/{quiz.question_number}")