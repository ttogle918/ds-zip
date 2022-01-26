"""
Bare Minimum Requirements
재귀를 반복적으로 보면서 익숙해집니다.

요구사항:
    재귀야말로 우리들의 머리 속을 헤집어 놓는 복잡한 개념입니다.
    재귀의 복잡성을 깨닫기위해 10분 머리쓰고 5분 그림그리기를 실천하도록 합니다.

    아래 코드에 작성된 요구사항을 확인하여 문제를 해결해주세요.
    각 문제 코드 위에 작성된 '@counter'는 변경하지 마세요.
"""


class counter:
    """
    해당 코드를 수정하지 마세요! 
    """
    def __init__(self, function):
        self.function = function
        self.cnt = 0

    def __call__(self, *args, **kwargs):
        self.cnt += 1
        return self.function(*args, **kwargs)


@counter    # 삭제하거나 변경하지 마세요!
def oneto100(num):
    """
    # 문제1
        다음 문제는 1 ~ num 까지 합을 구하는 문제입니다.
        결과값이 제대로 구해지도록 코드를 완성하세요.

        아래 예시입력값과 출력값을 참조하며 문제를 해결해봅니다.

        예시 1
            입력값:
                10
            출력값:
                55

        예시 2
            입력값:
                100
            출력값:
                5050
    """
    if num == 1 :
      return 1
    return num + oneto100(num-1)

# from sympy import *
@counter    # 삭제하거나 변경하지 마세요!
def factor(num1, num2):
    """
    # 문제2
        테스트코드에서 조건을 확인하고 최대공약수를 구하는 재귀코드를 작성해주세요.
        아래 예시입력값과 출력값을 참조하며 문제를 해결해봅니다.

        예시 1
            입력값:
                7, 19
            출력값:
                1

        예시 1
            입력값:
                40, 60
            출력값:
                20
    """
    # 둘 중 하나가 소수라면?   -> 그 배수가 아니라면 1이 최대공약수
    # 소수인지 매번 판별하면.. 시간복잡도가 너무 커질 것 같은데..

    # 둘 다 소수가 아니라면?   -> 최대공약수를 구하자.
    if num1 == 1 :
      return 1
    if num1 > num2 :    # num2가 더 큼
      t = num1
      num1 = num2
      num2 = t
    # divisor = 2
    # while divisor < num1 :
      
    # i = 2   # 무한루프
    # while num1 > 1 :
    #   if num1 % i == 0 and num2 % i == 0 :
    #     return i * factor(num1/i, num2/i)
    #   else :
    #     i += 1
