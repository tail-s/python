from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
# q_num = len(question_data) 굳이 이렇게 안해도 됨

# for i in range(q_num):
#     q = question_data[i]["text"]
#     a = question_data[i]["answer"]
#     data_i = Question(q, a)
#     question_bank.append(data_i)

for question in question_data: # 그냥 하나씩 넣어서
    q_text = question["text"]
    q_answer = question["answer"]
    q_set = Question(q_text, q_answer)
    question_bank.append(q_set)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()