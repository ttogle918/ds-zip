# 아래 코드는 변경하지 마세요!
class counter:
    def __init__(self, function):
        self.function = function
        self.cnt = 0

    def __call__(self, *args, **kwargs):
        self.cnt += 1
        return self.function(*args, **kwargs)

def gcd(n,m):
    if m % n == 0:  # 0일 때, n이 최대공약수
	    return n
    return gcd(n, m % n)

@counter
def coin_exchange(piece_price, piece_price_len, total_price): 
    mdiv = piece_price[0]
    for i in range(1, piece_price_len) :
      mdiv = gcd(mdiv, piece_price[i])

    piece_price = [p // mdiv for p in piece_price]
    total_price = total_price // mdiv

    way_of_number = [0 for temp in range(total_price + 1)] 
    piece_price.sort()
    way_of_number[0] = 1

    if total_price < piece_price[0] :
      return 0

    # for i in range(piece_price[0], total_price+1) : 
    #   way_of_number[total_price] = min([i-j for j in piece_price])+1
    # return way_of_number[total_price]