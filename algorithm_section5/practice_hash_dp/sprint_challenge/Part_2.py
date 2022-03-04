# 아래 코드는 변경하지 마세요!
class counter:
    def __init__(self, function):
        self.function = function
        self.cnt = 0

    def __call__(self, *args, **kwargs):
        self.cnt += 1
        return self.function(*args, **kwargs)

@counter
def part2_tab(n):
    count = {0:[n]}
    cnt = 0
    while n > 1 :
      if 1 in count[cnt] :
        print(count)
        return cnt
      cnt += 1
      count[cnt] = []
      for num in count[cnt-1] : 
        count[cnt].append(num-1) 
        if num % 3 == 0 :
          count[cnt].append(num//3)
        if num % 2 == 0 :
          count[cnt].append(num//2)

    return cnt

@counter
def part2_memo(n, memo = {}):
    if n <= 1 :
      return 0
    
    if n in memo :
      return memo[n]

    if n not in memo :
      memo[n] = 0
    
    memo[n] = 1 + part2_memo(n-1, memo)

    if n % 3 == 0 :
      temp = part2_memo(n//3, memo)
      memo[n] = temp + 1

    if n % 2 == 0 :
      temp = part2_memo(n//2, memo)
      if memo[n] > 1 + temp :
        memo[n] = 1 + temp

    return memo[n]