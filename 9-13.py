voca = open('vocabulary.txt', 'r', encoding="utf-8")

for word in voca:
    quiz = word.strip().split(": ")[1]
    answer = word.strip().split(": ")[0]
    ask_answer = input("%s: " % (quiz))
    if ask_answer == answer:
        print("맞았습니다!\n")
    else:
        print("아쉽습니다. 정답은 %s입니다.\n" % (answer))

voca.close()