from random import *
import pytest


@pytest.fixture(autouse=True)
def test_part3_import():
    try:
        from sprint_challenge.Part_3 import coin_exchange

    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_part3_coin_exchange_dont_use_recursion():
    from sprint_challenge.Part_3 import coin_exchange

    assert coin_exchange([100,200,300], 3, 400) == 4
    assert coin_exchange.cnt == 1, "재귀를 사용하면 안됩니다."


def test_part3_coin_exchange_return_correct_answer():
    from sprint_challenge.Part_3 import coin_exchange

    assert coin_exchange([100,200,300], 3, 400) == 4, "100원 200원 300원으로 400원을 만들 수 있는 방법은 4가지 입니다."
    assert coin_exchange([10,20,30], 3, 50) == 5, "10원 20원 30원으로 50원을 만들 수 있는 방법은 5가지 입니다."
    assert coin_exchange([10,20,30], 3, 1000) == 884, "10원 20원 30원으로 1000원을 만들 수 있는 방법은 884가지 입니다."
    
