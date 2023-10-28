# f(x) = 3x + 5

def tmFunction(x):
    return 3 * x + 5

print(tmpFunction(5))

def menuPrint():
    print("=======GAME=======")
    print("1. 행맨")
    print("2. 업다운")
    print("0. 종료")
    print("==================")

def getRandomWord():
    words = ["hang", "pretty", "apple", "ant", "water", "samsung", "MCdonalds", "fluent", "voca", "galaxy"]
    return words[random.randarge(0, len(words))]

hangman_input_history = []

def getHangmanInput():
    while True:
        user_input = input("Input alphabet ::: ")
        if(user_input.isalpha()):
            alphabet = user_input[0].lower()
            if(alphabet in hangman_input_history ):
                print("이미 입력한 값입니다. 새로운 알파벳을 입력해주세요.")
            else:
                return alphabet

def runHangMan():
    hangman_input_history = [] # 코드 초기화용
    chance = 7

    word = getRandomWord()


    while chance > 0:
        alphabet = gethangmanInput()

        hangman_input history.append(alphabet)

        if word.find(alphabet) != -1;
            print("corret!")
        else:
            chance = chance -1
            print("left chance : ", chance)
    #1. 모든 정답을 맞췄을때 게임이 끝나지 않음 -> 맞추면 alive  출력해주고 그만하기.
    # -> 맞추면 alive  출력해주고 그만하기  (break문용 사용)

    #2. 내가 맞춘 정답들이 어디에 위치해 있는지 알수없음
    # -> s _ _ s _ _ _ 출력
    # printCorrectWords() 합수를 선언(선택)해서 그 안에서 입력되었던 맞는 항목을 위치에 맞게 선택

def runUpDown():
    answer = random.randrange(0, 10)
    chance = 3

    # 사용자가 answer 맞출때까지 반복
    # 1. 사용자에게 기회주기(3번)
    # 2. 틀렸을때 updown 출력해주기

    while chance > 0:
        user_input = int(input("값을 입력하세요 >>"))

        if user_input == answer:
            print("정답입니다!")
            break
        else:
            chance = chance - 1
            if user_input > answer:
                print("down")
            else:
                print("up")
userInput = -1


while userInput !=  0;
    menuPrint()
    userInput = int(input("select menu ::: "))

    if userInput == 1:
        runHangMan()
    elif userInput == 2:
        runHangMan()
