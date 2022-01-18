"""
Advanced Requirements

내장함수를 다양하게 활용할 줄 알아야 합니다.

요구사항:
    도전과제에서 주로 바라볼 부분은 예외사항입니다.
    우리가 실제로 마주할 문제들도 대부분 복합적인 문제이므로 계속해서 스스로 문제를 만들고 해결해보는 과정을 겪어보도록 합니다.
    문제를 해결하는 방법과 문제에서 요구하는 개념 간의 연관성을 찾아보면서 문제를 해결합니다.

    Part 3의 요구사항은 기본적으로 충족하고, 추가적인 예외사항을 해결해주세요.
    다양한 내장함수를 활용해봅니다.
    소문자는 대문자로, 대문자는 소문자로 변경해주세요.

    아래 예시입력값과 출력값을 참조하며 문제를 해결해봅니다.

    *예시 1* 
        입력값:
            'c t A'
        출력값:
            'a C T'
    
    *예시 2* 
        입력값:
            'z X y W v U t S'
        출력값:
            's u w x T V Y Z'
"""

from functools import reduce
def part4(s):
  answer = []
  # ASCII : 97 == a, 122 == z, 65 == A, 90 == Z
  
  # s를 ' '단위로 split -> 중복 제거 -> list로 변환 -> 정렬
  s = sorted(list(set(s.split(' '))))

  answer = list(map(lambda x : ord(x), s))  # ascii code(숫자)로 변환

  answer = list(map(lambda x : chr(x - 32) if x > 96 else chr(x + 32), answer)) # Lower -> Upper, Upper -> lower
  
  answer = reduce(lambda i1, i2 : i1 + ' ' + i2, answer)  # 이어붙이기 ( list to string )
  return answer

print(part4('c t A'))
print(part4('z X y W v U t S'))
