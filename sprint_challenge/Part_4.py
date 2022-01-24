ANSWER = 'wrong answer'
CONSTANT = 'O(1)'
LOGARITHMIC = 'O(logn)'
LINEAR = 'O(n)'
LINEARITHMIC = 'O(nlogn)'
QUADRATIC = 'O(n^2)'
EXPONENTIAL = 'O(c^n)' 

def first_test(): # 해당 함수의 코드를 수정하지 마세요
    test_list = {}
    for first_index in range(0, 10):
        test_list[first_index] = first_index

    for first_index in range(0, 10):
        for second_index in range(0, 10):
            test_list[first_index] * test_list[second_index]

def first_test_time_complexity():
    return QUADRATIC


def second_test(): # 해당 함수의 코드를 수정하지 마세요
    test_list = [1,2,3,6,4,9,10,12]
    test_target = 12
    for index in range(0, len(test_list)):
        print(test_list[index], test_target)
        if test_list[index] == test_target:
            print("Yes")
            break
        else:
            print("No")

def second_test_time_complexity():
    return LINEAR  # 답안을 작성해주세요.


def third_test(): # 해당 함수의 코드를 수정하지 마세요
    first_list = [1,2,3]
    second_list = [12,13,14]    

    for first_index in first_list:
        for second_index in second_list:
            if (first_index + second_index) % 2 == 0:
                print("짝수")

            else:
                print("홀수")

def third_test_complexity():
    return QUADRATIC # 답안을 작성해주세요.


def fourth_test(n): # 해당 함수의 코드를 수정하지 마세요
    if n <= 0:
        return 1
    else:
        return 1 + fourth_test(n-1)

def fourth_test_time_complexity():
    return LINEAR # 답안을 작성해주세요.


def fifth_test(n): # 해당 함수의 코드를 수정하지 마세요
    if n <= 0:
        return 1
    else:
        return 1 + fifth_test(n-5)

def fifth_test_time_complexity():
    return LINEAR # 답안을 작성해주세요.


def sixth_test(n): # 해당 함수의 코드를 수정하지 마세요
    for i in range(0,n,2):      
        pass

    if n <= 0:
        return 1
    else:
        return 1 + sixth_test(n-5)

def sixth_test_time_complexity():
    return QUADRATIC # 답안을 작성해주세요.
    