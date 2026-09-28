import random

class Hand:
    ROCK = 1
    PAPER = 2
    SISOR = 3
    
    WIN = 4
    LOSE = 5
    DRAW = 6
    
    WIN_DECISION_DICT = {
        ROCK : {
            ROCK : DRAW,
            PAPER : LOSE,
            SISOR : WIN
        },
        PAPER : {
            ROCK : WIN,
            PAPER : DRAW,
            SISOR : LOSE
        },
        SISOR : {
            ROCK : LOSE,
            PAPER : WIN,
            SISOR : DRAW
        }
    }
    
    strDick = {
        ROCK: "주먹",
        SISOR : "가위",
        PAPER: "보"
    }
    
    def __init__(self):
        self.stat = 0
    
    def win_or_lose(self, enemy):
        return Hand.WIN_DECISION_DICT[self.stat][enemy.stat]
        
class Rock(Hand):
    def __init__(self):
        self.stat = Hand.ROCK
        
class Paper(Hand):
    def __init__(self):
        self.stat = Hand.PAPER
        
class Sisor(Hand):
    def __init__(self):
        self.stat = Hand.SISOR
        

def game_play():
    print("-----------------------------------------------")
    print("게임을 시작합니다. 주먹, 보, 가위 중 원하는 것을 선택해 주세요. 예) 1")
    print("1. 주먹")
    print("2. 보")
    print("3. 가위")
    
    myHand = None
    comHand = None
    
    while(True):
        choice =  input()
        myHand = createHand(choice)
        
        if myHand == None:
            print("다시 입력하세요.")
            continue
        else:
            break

    print("컴퓨터 선택중...")

    comHand = createHand(str(random.randint(1,3)))
    
    myStat = Hand.strDick[myHand.stat]
    comStat = Hand.strDick[comHand.stat]
    result = f"나: : {myStat}, 컴퓨터 : {comStat}"
    
    if myHand.win_or_lose(comHand) == Hand.WIN:
        print(f"승리! {result}")
    elif myHand.win_or_lose(comHand) == Hand.LOSE:
        print(f"패배! {result}")
    elif myHand.win_or_lose(comHand) == Hand.DRAW:
        print(f"무승부! {result}")
        
def createHand(choice):
    if choice == "1":
        return Rock()
    elif choice == "2":
        return Paper()
    elif choice == "3":
        return Sisor()
    else:
        return None
    
game_play()