class Process:
    def __init__(self, get_list):
        self.get_list = get_list
        self.question_number = 0
        self.score = 0

    def get_input(self, increment):
        self.question_number += 1

        select_option = input(
            f"Q.{self.question_number}: {self.get_list[increment]. new_text} (True/False)? : "
        ).capitalize()
        if select_option == self.get_list[increment].new_answer:
            print("You got it right!")
            print(f"The correct answer was : {self.get_list[increment].new_answer}")
            self.score += 1
            print(f"Your current score : {self.score}/{self.question_number}")
        elif select_option != self.get_list[increment].new_answer:
            print("That's wrong.")
            print(f"The correct answer was : {self.get_list[increment].new_answer}")
            print(f"Your current score : {self.score}/{self.question_number}")
        #     self.score += 1

    def total_score(self):
        print(f"Your total score is {self.score}")

    # def execute(self,score):
