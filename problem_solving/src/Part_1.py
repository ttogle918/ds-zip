"""
Bare Minimum Requirements

파이썬의 기본형태를 이해하고 컴프리헨션을 활용할 줄 알아야 합니다.

요구사항:
    반복해서 수학적인 개념이 접목된 프로그래밍 문제를 해결해봅니다.
    프로그래밍에 익숙해지는 과정에는 코드 자체에 대한 맥락을 읽어야 하는 것이 중요합니다.

    리스트 컴프리헨션 개념을 적용하여 '1~100까지 7과 5의 공배수' 를 구하는 코드를 작성하세요.
    아래 예시입력값과 출력값을 참조하며 문제를 해결해봅니다.

    입력값:
        없음
    출력값:
        [35, 70]
"""
def checkPrime(num) :   # 공약수구하기
  li = []
  n = 2

  while n < num/2 :
    if num % n == 0 :
      li.append(n)
    n += 1

  return (True, 0) if len(li) == 0 else (False, li)

def part1():
  num = 7 * 5
  fin = int(100 / num)
  return [i*num for i in range(1, fin+1)]

  # if checkPrime(7)[0] or checkPrime(5)[0] :   # 한가지만 소수면, 서로소 관계이다.
    # num = 7 * 5
    # fin = int(100 / num)
    # return [i*num for i in range(1, fin+1)]
  
  # li = list(set(checkPrime(7)[1] + checkPrime(5)[1]))
  # ...