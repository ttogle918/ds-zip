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


def part1_q1():
    a = 10
    b = 30
    return(a + b)


def part1_q1_answer():
    time_complexity = ANSWER
    reason = "이유를 작성해주세요"

    return (time_complexity, reason)


def part1_q2(li):
    sum = 0
    for i in li:
        sum += li
    return sum


def part1_q2_answer():
    time_complexity = ANSWER
    reason = "이유를 작성해주세요"

    return (time_complexity, reason)


def part1_q3(li):
    res = []
    for i in li:
        for j in li:
            res.append(i * j)

    return res


def part1_q3_answer():
    time_complexity = ANSWER
    reason = "이유를 작성해주세요"

    return (time_complexity, reason)
