"""
Bare Minimum Requirements

요구사항:
    작성되어있는 함수의 시간복잡도가 어떻게 되는지 판별할 수 있어야합니다. 

    문제로 작성된 함수를 확인하여, 해당 함수의 시간복잡도와 그 이유를 작성해주세요.
    문제로 작성된 함수 (part1_q1, part1_q2, part1_q3)는 수정하시면 안됩니다. 

    정답을 작성하는 함수내부에 답을 작성해주세요 
    (part1_q1_answer, part1_q2_answer, part1_q3_answer)

    time_complexity에는 전역으로 선언된 시간복잡도 변수를 사용해주세요.
    reason에는 그렇게 생각한 이유를 문자열로 작성해주세요.
    
"""

ANSWER = 'wrong answer'
CONSTANT = 'O(1)'
LOGARITHMIC = 'O(logn)'
LINEAR = 'O(n)'
LINEARITHMIC = 'O(nlogn)'
QUADRATIC = 'O(n^2)'
EXPONENTIAL = 'O(c^n)' 


def part2_q1(li):
    for i in li:
        print(i)

    res = []
    for i in li:
        for j in li:
            res.append(i * j)

    return res
    

def part2_q1_answer():
    time_complexity = QUADRATIC
    reason = "O(n) + O(n^2) = O(n^2)이다."

    return (time_complexity, reason)


def part2_q2(li):
    for i in li:
        break


def part2_q2_answer():
    time_complexity = CONSTANT
    reason = "range(li)만큼 loop를 실행해야하지만, 첫번째 실행문에서 break가 나왔으니 바로 빠져나오게된다."

    return (time_complexity, reason)


def part2_q3(num):
    res = 0
    cur = 1
    while (cur < num):
        res += 1
        cur = cur * 2
    return res


def part2_q3_answer():
    time_complexity = LOGARITHMIC
    reason = "cur이 num보다 작을 동안 loop를 돈다. 그런데 cur이 매번 2배수로 높아지기 때문에 2의 지수승만큼 높아지기 때문에, 실행횟수는 그의 역함수인 log2만큼 늘어나게 된다(n < log n < n^2)"

    return (time_complexity, reason)
