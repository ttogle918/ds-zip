"""
Advanced Requirements
추상적 문제에 대해서 다양한 알고리즘을 활용하여 문제를 해결하기

요구사항:
    어렵고 불편한 추상화된 상황을 느껴보도록 합니다.
    아래 문제에서는 단순한 정답맞추기가 아닌 내부로직을 어떻게 구성해야할지 다방면으로 생각해봅니다.

    입력된 숫자를 특정 문자열 형태로 변환하는 문제입니다.
    아래 예상 입출력을 보면서 어떤 식으로 배열과 반복문, 조건문을 구성해야 할지 생각해봅니다.

    Case 1
        입력
        0
        출력 
        Zero.

    Case 2
        입력
        11
        출력 
        Eleven.

    Case 3
        입력
        1043283
        출력 
        One million, forty-three thousand, two hundred and eighty-three.
"""
# import inflect
def word_logic(num, word_dic):  # num : 100단위 값
    print(num)
    if num in word_dic :
      return word_dic[num]

    word_result = ''
    
    # 큰 수부터 구해야 예외글자를 구할 수 있다.
    d_100, m = divmod(num, 100)   # 100의 자리
    if d_100 > 0 :
      word_result = word_dic[d_100] + ' ' + word_dic[100] + ' and'

    if m < 21 :   # 예외 글자
      return (word_result + ' ' + word_dic[m]).strip()
    
    d_10, m = divmod(m, 10)   # d : 10의 자리, m : 1의자리

    return (word_result + ' ' + word_dic[d_10*10] + '-' + word_dic[m]).strip()
    

def number_logic(num):
    word_dic = {0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten', 
                11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', 15: 'fifteen', 16: 'sisteen', 17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen', 20 : 'twenty',
                30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty', 70 : 'seventy', 80 : 'eighty', 90 : 'ninety', 
                100 : 'hundred', 1000 : 'thousand', 1000000 : 'million'}
    answer = ''
    i = 1000
    # 1000단위씩 나누기
    d, m = 1, num
    while d > 0 :
      d, m = divmod(num, i)   # m : 1000 미만 값
      m = m // (i / 1000)

      if d == 0 : 
        answer = word_logic(m, word_dic) + ' ' + answer
      else : 
        answer = word_dic[i] + ', ' + word_logic(m, word_dic) +' '+ answer
      i *= 1000
    answer = answer.capitalize().rstrip() + '.'
    return answer
