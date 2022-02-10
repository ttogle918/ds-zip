from random import *
import pytest


@pytest.fixture(autouse=True)
def test_part1_import():
    try:
        from sprint_challenge.Part_1 import addNumber, countDown, printStar

    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_part1_addNumber():
    from sprint_challenge.Part_1 import addNumber
    from random import randint

    for _ in range(10):
        num = randint(10,30)
        assert addNumber(num) == sum([n for n in range(0, num+1)]), \
            f'{num}에서는 {sum([n for n in range(0, num+1)])}을 반환해야합니다.'


def test_part1_countDown():
    from sprint_challenge.Part_1 import countDown
    from random import randint

    for _ in range(10):
        num = randint(10,15)
        li = [n for n in range(1, num+1)]
        li.reverse()
        assert countDown(num, []) ==  li + ['발사!!'], \
            f'{num}에서는 결과값이\n{li + ["발사!!"]}로 나와야합니다.'


def test_part1_printStar():
    from sprint_challenge.Part_1 import printStar
    from random import randint

    for _ in range(10):
        num = randint(10,15)
        assert printStar(num, []) == ['*'* n for n in range(1, num + 1)], \
            f'{num}에서는 결과값이\n{["*"* n for n in range(1, num + 1)]}로 나와야합니다.'


def test_part1_func_use_recursion():
    from sprint_challenge.Part_1 import addNumber, countDown, printStar

    assert addNumber.cnt >= 10, 'addNumber 함수는 재귀함수로 구현되어야합니다'
    assert countDown.cnt >= 10, 'countDown 함수는 재귀함수로 구현되어야합니다'
    assert printStar.cnt >= 10, 'printStar 함수는 재귀함수로 구현되어야합니다'