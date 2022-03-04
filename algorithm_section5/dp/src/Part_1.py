"""
Bare Minimum Requirements
DP의 개념을 이해합니다.

요구사항:
    기본적인 피보나치 수열에 대해 동적계획법(DP) 개념을 적용해봅니다.
    
"""
# 아래 코드는 변경하지 마세요!
class counter:
    def __init__(self, function):
        self.function = function
        self.cnt = 0

    def __call__(self, *args, **kwargs):
        self.cnt += 1
        return self.function(*args, **kwargs)

@counter
def memo_fib(input_value, save_memo={}):
    """
    문제 1.
        메모이제이션 개념을 사용하여 피보나치 수열을 구하는 함수를 작성해주세요
        input_value 번째 피보나치 수열을 구하는 함수를 작성해주세요

        입력값:
            33
        출력값:
            3524578
    """
    if input_value in save_memo :
      return save_memo[input_value]

    if input_value < 2 :
      save_memo[0] = 0
      save_memo[1] = 1
      return input_value
    
    save_memo[input_value] =  memo_fib(input_value-1, save_memo) + memo_fib(input_value-2, save_memo)
    print(input_value, save_memo)

    return save_memo[input_value]

@counter
def tabul_fib(input_value):
    """
    문제 1.
        태뷸레이션 개념을 사용하여 피보나치 수열을 구하는 함수를 작성해주세요
        input_value 번째 피보나치 수열을 구하는 함수를 작성해주세요

        입력값:
            33
        출력값:
            3524578
    """
    arr = [0, 1, 1]
    if input_value < 3 :
      return arr[input_value]
    
    for i in range(3, input_value+1) :
      arr.append(arr[i-1] + arr[i-2])

    return arr[input_value]



