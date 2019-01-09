from random import randint
chance = 4
trial = 1
x = randint(1 , 20)

while chance > 0:
    choice = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: " % (chance)))
    if choice > x:
        print("Down")
        trial = trial + 1
        chance = chance - 1

    elif choice < x:
        print("Up")
        trial = trial + 1
        chance = chance - 1

    else:
        print("축하합니다. %d번 만에 숫자를 맞추셨습니다." % (trial))
        chance = chance - 10
if chance == 0:
    print("아쉽습니다. 정답은 %d였습니다." % (x) )
