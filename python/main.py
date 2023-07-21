from index import question_data
from example import *
from process import *
import os


increment = 0
new_list = []
for data in question_data:
    Text = data["text"]
    Answer = data["answer"]
    q = Question(Text, Answer)
    new_list.append(q)
p = Process(new_list)
while increment < len(new_list):
    p.get_input(increment)
    # p.execute(increment)

    increment += 1
os.system("clear")
p.total_score()
