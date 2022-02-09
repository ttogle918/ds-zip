# 아래 코드는 변경하지 마세요!
class counter:
    def __init__(self, function):
        self.function = function
        self.cnt = 0

    def __call__(self, *args, **kwargs):
        self.cnt += 1
        return self.function(*args, **kwargs)


@counter
def coin_exchange(piece_price, piece_price_len, total_price): 
  
    way_of_number = [0 for temp in range(total_price + 1)] 
  
    way_of_number[0] = 1
    ##### 소스코드 작성 #####
    
    return 

