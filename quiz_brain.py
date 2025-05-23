class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):

        return self.q_number < len(self.q_list)
        
    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        return f"Q.{self.q_number}: {current_question.q_text}"

    

    def check_answer(self, user_answer):
        correct_answer = self.q_list[self.q_number - 1].q_answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        return False

