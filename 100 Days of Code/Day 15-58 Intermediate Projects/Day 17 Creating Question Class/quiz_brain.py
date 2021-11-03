class QuizBrain:
    def __init__(self, q_list) -> None:
        self.questionNumber = 0
        self.correctAnswer = 0
        self.question_list = q_list
    
    def getCurrentQuestion(self):
        currentQuestion = self.question_list[self.questionNumber]
        return input(f"Q{self.questionNumber}: {currentQuestion.text} Please enter True or False: ")[0].lower()
    
    def checkAnswer(self, userResponce):
        if userResponce == self.question_list[self.questionNumber].answer[0].lower():
            self.correctAnswer += 1
            print("You got it right!")
        else:
            print("Sorry you got it wrong.")
        print(f"Current score {self.correctAnswer}/{self.questionNumber + 1}\n")    
        self.questionNumber += 1
    
    def finalScore(self):
        return self.correctAnswer

    

    
