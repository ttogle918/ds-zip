import pytest

@pytest.fixture(autouse=True)
def test_part1_import():
    try:
        from sprint_challenge.Part_3 import added_word

    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')

def test_added_words_working_normally():
    from sprint_challenge.Part_3 import added_word
    
    assert 'is' == added_word('the best', 'the best is')
    assert None == added_word('the best is', 'the best')
    assert 'states' == added_word('code', 'code states')
