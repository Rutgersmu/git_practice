voca = open('vocabulary.txt', 'r', encoding="utf-8")
from random import randint

voca_quiz = {}
voca_answer ={}
i = 0
for word in voca:
    quiz = word.strip().split(": ")[1]
    answer = word.strip().split(": ")[0]
    voca_quiz[i] = quiz
    voca_answer[i] = answer
    i = i + 1

print(voca_answer)
print(voca_quiz)

ask_answer = ()
while ask_answer != 'q':
    j = randint(0, i-1)
    ask_answer = input("%s: " % (voca_quiz[j]))
    if ask_answer == voca_answer[j] and ask_answer != 'q':
        print("맞았습니다!\n")
    elif ask_answer != voca_answer[j] and ask_answer != 'q':
        print("아쉽습니다. 정답은 %s입니다.\n" % (voca_answer[j]))

voca.close()
