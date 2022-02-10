from random import *
import pytest


@pytest.fixture(autouse=True)
def test_part2_import():
    try:
        from sprint_challenge.Part_2 import selectionSort, bubbleSort

    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_part2_selectionSort():
    from sprint_challenge.Part_2 import selectionSort
    from random import shuffle
    from copy import deepcopy

    for _ in range(10):
        num = randint(10,20)
        li = [n for n in range(1, num)]
        li.reverse()

        li_shuff = deepcopy(li)
        shuffle(li_shuff)
        li_shuff_stmp = deepcopy(li_shuff)

        assert selectionSort(li_shuff) == li,\
            f'{li_shuff_stmp}를 입력하였을 때 내림차순으로 정렬이 되어야합니다.'


def test_part2_bubbleSort():
    from sprint_challenge.Part_2 import bubbleSort
    from random import shuffle
    from copy import deepcopy

    for _ in range(10):
        num = randint(10,20)
        li = [n for n in range(1, num)]
        li.reverse()

        li_shuff = deepcopy(li)
        shuffle(li_shuff)
        li_shuff_stmp = deepcopy(li_shuff)

        assert bubbleSort(li_shuff) == li,\
            f'{li_shuff_stmp}를 입력하였을 때 내림차순으로 정렬이 되어야합니다.'


def test_part2_insertionSort():
    from sprint_challenge.Part_2 import insertionSort
    from random import shuffle
    from copy import deepcopy

    for _ in range(10):
        num = randint(10,20)
        li = [n for n in range(1, num)]
        li.reverse()

        li_shuff = deepcopy(li)
        shuffle(li_shuff)
        li_shuff_stmp = deepcopy(li_shuff)

        assert insertionSort(li_shuff) == li,\
            f'{li_shuff_stmp}를 입력하였을 때 내림차순으로 정렬이 되어야합니다.'
