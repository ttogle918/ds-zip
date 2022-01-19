"""
Extra Requirements
이미 작성되어있는 코드들을 바탕으로 문제를 해결해주세요.
아래 문제는 점수에 들어가지 않습니다.
여러분들이 실행해보면서 에러가 발생하지 않는 코드로 만들어주세요.
자유롭게 도전해주세요.

요구사항:
    아래 요구사항에서 중점적으로 봐야할 부분은 예외사항이 추가되었을 뿐만 아니라 형식이 바뀌었다는 것입니다.
    추가되는 문제에 대한 해결도 중요하지만, 문제의 종류가 모호하게 변경되는 경우에 대한 대처도 생각해야합니다.
    1,2,3,9와 같은 정수형태가 아닌 '가위,바위,보', '게임종료'와 같이 텍스트 형태로 입력한 경우 정상적으로 동작되도록 변경해주세요.
        이 부분을 예외처리하기위해서는 변경해야될 부분이 많을 것입니다.
    
    Part 2의 2가지 예외사항을 한 번에 처리할 수 있도록 해주세요.
        한 번에 처리할 수 있는 방법은 여러가지가 있을 수 있으니 다양한 방법을 검색해보세요.
        Part 2를 import하는 것이 아닌, 해당 함수 내에서 조건문을 활용하여 해결하세요.
    문제를 해결했다면 기존 기능에서 추가적인 기능을 설계하고 기능에 따른 클래스와 함수, 변수를 생성하면서 문제를 확장해봅니다.
    pass 안에는 값이 들어가지 않을 수 있고 들어가야될 수도 있습니다.
    상황에 적절하게 수정해주세요.
"""
# 1. 입력값 가위, 바위, 보, 1, 2, 3, 9, 게임종료 가능
# 2. score 저장

import random

def rock_sciss_paper():
    def show_welcome_message():
        print(welcome_message)


    def get_choice(choice):
       ###[1] 가위   [2] 바위   [3] 보    [9] 게임종료###
      return choice_options[choice] 


    def quit_game(score):
        print(quit_message)
        print("게임결과")
        print("-----")
        print(score)


    def compare_choices_and_get_result(user, computer):
      if user == computer:
        print("사용자 : ", user, ", ", "컴퓨터 : ", computer_choice)
        return "무승부"
      elif (user == get_choice("바위") and computer == get_choice("가위")) or (user == get_choice("보") and computer == get_choice("바위")) or (user == get_choice("가위") and computer == get_choice("보")):
        print("사용자 : ", user, ", ", "컴퓨터 : ", computer_choice)
        return "사용자승"
      else:
        print("사용자 : ", user, ", ", "컴퓨터 : ", computer_choice)
        return "사용자패"


    def set_score(s) :
      score[s] += 1
    
    def display_result_message_and_update_score(result):
        if result == "무승부":
            print(tie_message)
        elif result == "사용자승":
            print(win_message)
        else:
            print(loss_message)
        set_score(result)

    score =  {
      "사용자승": 0,
      "무승부": 0,
      "사용자패": 0
    }

    welcome_message = "가위바위보 게임을 시작합니다."
    win_message = "사용자가 이겼습니다."
    loss_message = "사용자가 졌습니다."
    tie_message = "무승부입니다."
    quit_message = "게임을 종료합니다."

    choice_options = {
      '1': 1, 
      "가위" : 1,
      '2': 2, 
      "바위" : 2,
      '3': 3, 
      "보" : 3,
      '9': 9, 
      "게임종료" : 9
    }


    show_welcome_message()

    while True :
      try : 
        user_choice = input()
        user_choice = get_choice(user_choice)
        
        if user_choice == 9 :
          break
      except KeyError as e:
        print("범위 내로 입력해주세요!!!")
        continue
      
      keys = ['1', '2', '3']  # list 내 랜덤값
      computer_choice = get_choice(random.choice(keys))
      result = compare_choices_and_get_result(user_choice, computer_choice)
      display_result_message_and_update_score(result)
      
    print('')
    quit_game(score)


if __name__ == "__main__":
    rock_sciss_paper()