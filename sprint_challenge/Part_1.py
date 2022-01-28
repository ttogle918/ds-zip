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
    pass


@counter
def countDown(num, li) :
    pass

@counter
def printStar(num, li) :
    pass
