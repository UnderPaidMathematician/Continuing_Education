from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questionBank = []
for q in question_data:
    questionBank.append(Question(q['question'], q['correct_answer']))

quizBrain = QuizBrain(questionBank)

for i in quizBrain.question_list:
    response = quizBrain.getCurrentQuestion()
    quizBrain.checkAnswer(response)

print(f"Your final score was {quizBrain.finalScore()} out of {quizBrain.questionNumber}")

