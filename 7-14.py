from random import randint # 랜덤 함수 추출
# 랜덤 숫자 뽑아서 리스트로 만들기
x = randint(0, 9)
y = randint(0, 9)
z = randint(0, 9)
while x == y:
    y = randint(0, 9)
while z == x or z == y:
    z = randint(0, 9)
trial = 0
numbers = [x, y, z]
strike = 0

# 숫자 야구 만들기
# Intro
print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
while strike < 3:
    print()
    print("세 수를 하나씩 차례대로 입력하세요.")

    # 숫자 선택
    # 첫 번째 숫자
    guess1 = input("1 번째 수를 입력하세요: ")
    while int(guess1) > 9 or int(guess1) < 0:
        print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
        guess1 = input("1 번째 수를 입력하세요: ")

    # 두 번째 숫자
    guess2 = input("2 번째 수를 입력하세요: ")
    while int(guess2) > 9 or int(guess2) < 0:
        print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
        guess2 = input("2 번째 수를 입력하세요: ")
    while guess1 == guess2:
        print("중복되는 수 입니다. 다시 입력해주세요.")
        guess2 = input("2 번째 수를 입력하세요: ")
        while int(guess2) > 9 or int(guess2) < 0:
            print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
            guess2 = input("2 번째 수를 입력하세요: ")


    # 세 번째 숫자
    guess3 = input("3 번째 수를 입력하세요: ")
    while int(guess3) > 9 or int(guess3) < 0:
        print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
        guess3 = input("3 번째 수를 입력하세요: ")
    while guess3 == guess1 or guess3 == guess2:
        print("중복되는 수 입니다. 다시 입력해주세요.")
        guess3 = input("3 번째 수를 입력하세요: ")
        while int(guess3) > 9 or int(guess3) < 0:
            print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
            guess3 = input("3 번째 수를 입력하세요: ")
    trial = trial + 1

    #게임하기


    guess = [int(guess1), int(guess2), int(guess3)]
    strike = 0
    ball = 0
    i = 0
    while i <= 2:
        if numbers[i] == guess[i]:
            strike = strike + 1
        elif numbers[i] != guess[i] and numbers[i] == guess[i-1] or numbers[i] == guess[i-2]:
            ball = ball + 1
        i = i + 1

    print("%dS %dB" % (strike, ball))
    print()
    if strike == 3:
        print("축하합니다. %d번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % (trial))