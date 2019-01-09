voca = open('vocabulary.txt', 'w', encoding="utf-8")

english_word = ()
korean_meaning = ()

while english_word != "q":
    english_word = input("영어 단어를 입력하세요: ")
    if english_word != "q":
        korean_meaning = input("한국어 뜻을 입력하세요: ")
        voca.write(english_word)
        voca.write(": ")
        voca.write(korean_meaning)
        voca.write("\n")

voca.close()