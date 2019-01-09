from random import randint

# 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기
def generate_numbers():
    # 숫자 6개를 보관할 리스트 생성
    # 6개의 요소가 있을 때까지 반복
    numbers = []
    while len(numbers) < 6:
        # 새로 뽑은 수가 numbers에 없을 경우에만 추가
        new_number = randint(1, 45)
        if new_number not in numbers:
            numbers.append(new_number)
    numbers = sorted(numbers)
    # 리스트 리턴
    return numbers
numbers = generate_numbers()

# 보너스까지 포함해 7개 숫자 뽑기
# 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
def draw_winning_numbers():
    winning_numbers = generate_numbers()
    while len(winning_numbers) < 7:
        new_number = randint(1, 45)
        if new_number not in generate_numbers():
            winning_numbers.append(new_number)
    return winning_numbers
winning_numbers = draw_winning_numbers()

# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(list1, list2):
    count = 0
    i = 0
    while i < len(list2) - 1:
        j = 0
        while j < len(list1):
            if list2[i] == list1[j]:
                count += 1
            j += 1
        i = i + 1
    return count
count = count_matching_numbers(numbers, winning_numbers)
# 로또 등수 확인하기

def check(numbers, winning_numbers):
    if count_matching_numbers(numbers, winning_numbers) == 6:
        return 1000000000
    elif count_matching_numbers(numbers, winning_numbers) == 5:
        i = 0
        while i < len(numbers):
            if numbers[i] == winning_numbers[-1]:
                return 50000000
            else:
                return 1000000
            i += 1
    elif count_matching_numbers(numbers, winning_numbers) == 4:
        return 50000
    elif count_matching_numbers(numbers, winning_numbers) == 3:
        return 5000
    else:
        return 0


