import pytest

@pytest.fixture(autouse=True)
def test_part1_import():
    try:
        from sprint_challenge.Part_4 import first_test_time_complexity, \
            second_test_time_complexity,\
            third_test_complexity,\
            fourth_test_time_complexity,\
            fifth_test_time_complexity,\
            sixth_test_time_complexity
            
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')

def test_part4_first_test():
    from sprint_challenge.Part_4 import first_test_time_complexity

    res_as = 0
    res = first_test_time_complexity()
    for i in res:
        res_as += ord(i)
    assert res_as == 414, "정확한 시간복잡도를 반환해야합니다."


def test_part4_second_test():
    from sprint_challenge.Part_4 import second_test_time_complexity

    res_as = 0
    res =  second_test_time_complexity()
    for i in res:
        res_as += ord(i)
    assert res_as == 270, "정확한 시간복잡도를 반환해야합니다."


def test_part4_third_test():
    from sprint_challenge.Part_4 import third_test_complexity

    res_as = 0
    res =  third_test_complexity()
    for i in res:
        res_as += ord(i)
    assert res_as == 414, "정확한 시간복잡도를 반환해야합니다."


def test_part4_fourth_test():
    from sprint_challenge.Part_4 import fourth_test_time_complexity

    res_as = 0
    res = fourth_test_time_complexity()
    for i in res:
        res_as += ord(i)
    assert res_as == 270, "정확한 시간복잡도를 반환해야합니다."


def test_part4_fifth_test():
    from sprint_challenge.Part_4 import fifth_test_time_complexity

    res_as = 0
    res = fifth_test_time_complexity()
    for i in res:
        res_as += ord(i)
    assert res_as == 270, "정확한 시간복잡도를 반환해야합니다."


def test_part4_sixth_test():
    from sprint_challenge.Part_4 import sixth_test_time_complexity

    res_as = 0
    res = sixth_test_time_complexity()
    for i in res:
        res_as += ord(i)
    assert res_as == 414,"정확한 시간복잡도를 반환해야합니다."