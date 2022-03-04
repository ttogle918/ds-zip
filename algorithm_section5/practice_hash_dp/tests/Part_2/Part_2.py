from random import *
import pytest
import pickle

@pytest.fixture(autouse=True)
def test_part2_import():
    try:
        from sprint_challenge.Part_2 import part2_tab, part2_memo

    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_part2_tab_return_correct_answer():
    from sprint_challenge.Part_2 import part2_tab

    filename = 'results'

    infile = open(filename,'rb')
    results = pickle.load(infile)
    infile.close()

    for key in results.keys():
        assert results[key] == part2_tab(key), \
            f'{key} 값을 연산을 통해 1로 만들기 위해서는 {results[key]}번의 연산이 필요합니다.'


def test_part2_tab_counter():
    from sprint_challenge.Part_2 import part2_tab

    assert part2_tab.cnt == 99, 'part2_tab 함수는 재귀로 구현하면 안됩니다.'


def test_part2_memo_return_correct_answer():
    from sprint_challenge.Part_2 import part2_memo

    filename = 'results'

    infile = open(filename,'rb')
    results = pickle.load(infile)
    infile.close()

    for key in results.keys():
        assert results[key] == part2_memo(key), \
            f'{key} 값을 연산을 통해 1로 만들기 위해서는 {results[key]}번의 연산이 필요합니다.'


def test_part2_memo_counter():
    from sprint_challenge.Part_2 import part2_memo

    assert part2_memo.cnt >= 99, 'part2_memo 함수는 재귀로 구현해야합니다.'