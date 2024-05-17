import question_model
import data
import quiz_brain

question_bank = []

for data_set in data.question_data:
    question_text = data_set["question"]
    question_answer = data_set["correct_answer"]
    question = question_model.Question(question_text, question_answer)
    question_bank.append(question)

quiz = quiz_brain.QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
