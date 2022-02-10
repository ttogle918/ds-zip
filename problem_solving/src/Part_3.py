"""
Advanced Requirements
반복문과 조건문을 활용한 문제를 해결은 계속됩니다.

요구사항:
    복합적으로 엮여있는 조건을 하나씩 풀어봅니다.
    추상도가 높고 프로그래밍에 대한 언급이 없을 수록 문제해결은 어려워집니다.
    머신러닝과 딥러닝에서 봤었던 복잡한 수식이 어떻게 코드화되었는지 함께 생각해보면서 아래 문제를 해결합니다.

    1부터 1이상의 입력받은 숫자까지 모든 숫자에 대해 소수가 몇 개 있는지 반환하세요.
    0이하의 경우 ValueError를 발생시켜 주세요.
"""
def checkPrime(num) :
  n = 2

  while n < num :     # num==2일 때는 실행하지 않고 바로 True 반환
    if num % n == 0 :   # 나눠진다면 prime number가 아니다.
      return False
    n += 1
  return True

# primenumber은 2 이상이다.
def part3(N):
  if N <= 0 :
    raise ValueError('a must be N <= 0')
  num = 2
  mysum = 0
  
  while num <= N :
    if checkPrime(num) :
      mysum += 1
    num += 1

  if mysum <= 0 :
    raise ValueError('a must be sum <= 0')
  return mysum