# asking the questions
# checking if the answer was correct
# checking if we're the end of the quiz

# question_number, question_list
class QuizBrain:

    def __init__(self, quiz):
        self.question_number = 0
        self.question_list = quiz
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.test} (True/Fasle): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

        # if self.question_number < len(self.question_list): # next_question에서 +1 되니까
        #     return True
        # else:
        #     False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was : {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")

