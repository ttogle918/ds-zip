# 아래 코드는 변경하지 마세요!
class counter:
    def __init__(self, function):
        self.function = function
        self.cnt = 0

    def __call__(self, *args, **kwargs):
        self.cnt += 1
        return self.function(*args, **kwargs)

@counter
def addNumber(num) :
    if num <= 1 :
      return 1
    return num + addNumber(num-1)

@counter
def countDown(num, li) :
    if num <= 0 :
      return li + ['발사!!']
    return [num] + countDown(num-1, li)
@counter
def printStar(num, li) :
    if num <= 1 :
      return ['*']
    return printStar(num-1, li) + ['*'*num]
