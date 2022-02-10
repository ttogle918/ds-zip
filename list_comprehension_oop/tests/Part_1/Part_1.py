import dis
import pytest


def list_func_calls(fn, s):
    cnt = 0
    bytecode = dis.Bytecode(fn)
    instrs = list(reversed([instr for instr in bytecode]))
    for (ix, instr) in enumerate(instrs):
        if instr.opname==s:
            cnt += 1
    return cnt


def test_part1_quesion1():
    try:
        from sprint_challenge.Part_1 import quesion1

        assert quesion1() == ['Dolphine', 'David'], "정확한 결과를 반환해야합니다."
        assert list_func_calls(quesion1, "POP_JUMP_IF_FALSE") == 0, '컴프리헨션을 사용하여 문제를 해결해야합니다.'
        assert list_func_calls(quesion1, "GET_ITER") != 0, '연산없이 결과값만 반환하면 안됩니다'

    except ImportError:
        pytest.fail("코드에서 문제가 발생했습니다. 다시한번 확인해주세요")

    except Exception as e:
        print(e)
        pytest.fail("에러가 발생합니다. 에러를 해결해주세요")


def test_part1_quesion2():
    try:
        from sprint_challenge.Part_1 import quesion2

        assert quesion2() == ['Charlse', 'Dolphine'], "정확한 결과를 반환해야합니다."
        assert list_func_calls(quesion2, "POP_JUMP_IF_FALSE") == 0, '컴프리헨션을 사용하여 문제를 해결해야합니다.'
        assert list_func_calls(quesion2, "GET_ITER") != 0, '연산없이 결과값만 반환하면 안됩니다'

    except ImportError:
        pytest.fail("코드에서 문제가 발생했습니다. 다시한번 확인해주세요")

    except Exception as e:
        print(e)
        pytest.fail("에러가 발생합니다. 에러를 해결해주세요")



def test_part1_quesion3():
    try:
        from sprint_challenge.Part_1 import quesion3

        assert quesion3() == ['Charlse', 'Dolphine', 'Eva', 'Frin', 'Gless', 'David'], "정확한 결과를 반환해야합니다."
        assert list_func_calls(quesion3, "POP_JUMP_IF_FALSE") == 0, '컴프리헨션을 사용하여 문제를 해결해야합니다.'
        assert list_func_calls(quesion3, "GET_ITER") != 0, '연산없이 결과값만 반환하면 안됩니다'

    except ImportError:
        pytest.fail("코드에서 문제가 발생했습니다. 다시한번 확인해주세요")

    except Exception as e:
        print(e)
        pytest.fail("에러가 발생합니다. 에러를 해결해주세요")

    
def test_part1_quesion4():
    try:
        from sprint_challenge.Part_1 import quesion4

        assert quesion4() == [39, 42, 47, 40, 36, 28, 52, 22, 51, 41], "정확한 결과를 반환해야합니다."
        assert list_func_calls(quesion4, "POP_JUMP_IF_FALSE") == 0, '컴프리헨션을 사용하여 문제를 해결해야합니다.'
        assert list_func_calls(quesion4, "GET_ITER") != 0, '연산없이 결과값만 반환하면 안됩니다'

    except ImportError:
        pytest.fail("코드에서 문제가 발생했습니다. 다시한번 확인해주세요")

    except Exception as e:
        print(e)
        pytest.fail("에러가 발생합니다. 에러를 해결해주세요")


def test_part1_quesion5():
    try:
        from sprint_challenge.Part_1 import quesion5

        assert quesion5() == ['Abi-29', 'Batista-32', 'Charlse-37', 'Dolphine-30', 'Eva-26', 'Frin-18', 'Gless-42', 'Harby-12', 'Iris-41', 'David-31'], "정확한 결과를 반환해야합니다."
        assert list_func_calls(quesion5, "POP_JUMP_IF_FALSE") == 0, '컴프리헨션을 사용하여 문제를 해결해야합니다.'
        assert list_func_calls(quesion5, "GET_ITER") != 0, '연산없이 결과값만 반환하면 안됩니다'

    except ImportError:
        pytest.fail("코드에서 문제가 발생했습니다. 다시한번 확인해주세요")

    except Exception as e:
        print(e)
        pytest.fail("에러가 발생합니다. 에러를 해결해주세요")


def test_part1_quesion6():
    try:
        from sprint_challenge.Part_1 import quesion6

        assert quesion6() == ['Abi-29', 'Batista-32', 'Dolphine-30', 'David-31'], "정확한 결과를 반환해야합니다."
        assert list_func_calls(quesion6, "POP_JUMP_IF_FALSE") == 0, '컴프리헨션을 사용하여 문제를 해결해야합니다.'
        assert list_func_calls(quesion6, "GET_ITER") != 0, '연산없이 결과값만 반환하면 안됩니다'

    except ImportError:
        pytest.fail("코드에서 문제가 발생했습니다. 다시한번 확인해주세요")

    except Exception as e:
        print(e)
        pytest.fail("에러가 발생합니다. 에러를 해결해주세요")


def test_part1_quesion7():
    try:
        from sprint_challenge.Part_1 import quesion7

        assert quesion7() == [('ABI', 34), ('BATISTA', 37), ('CHARLSE', 42), ('DOLPHINE', 35), ('EVA', 31), ('FRIN', 23), ('GLESS', 47), ('HARBY', 17), ('IRIS', 46), ('DAVID', 36)], "정확한 결과를 반환해야합니다."
        assert list_func_calls(quesion7, "POP_JUMP_IF_FALSE") == 0, '컴프리헨션을 사용하여 문제를 해결해야합니다.'
        assert list_func_calls(quesion7, "GET_ITER") != 0, '연산없이 결과값만 반환하면 안됩니다'

    except ImportError:
        pytest.fail("코드에서 문제가 발생했습니다. 다시한번 확인해주세요")

    except Exception as e:
        print(e)
        pytest.fail("에러가 발생합니다. 에러를 해결해주세요")


def test_part1_quesion8():
    try:
        from sprint_challenge.Part_1 import quesion8

        assert quesion8() == [5.39, 5.66, 6.08, 5.48, 5.1, 4.24, 6.48, 3.46, 6.4, 5.57], "정확한 결과를 반환해야합니다."
        assert list_func_calls(quesion8, "POP_JUMP_IF_FALSE") == 0, '컴프리헨션을 사용하여 문제를 해결해야합니다.'
        assert list_func_calls(quesion8, "GET_ITER") != 0, '연산없이 결과값만 반환하면 안됩니다'

    except ImportError:
        pytest.fail("코드에서 문제가 발생했습니다. 다시한번 확인해주세요")

    except Exception as e:
        print(e)
        pytest.fail("에러가 발생합니다. 에러를 해결해주세요")