import dis
from pytest import fail


def list_func_calls(fn, s):
    cnt = 0
    bytecode = dis.Bytecode(fn)
    instrs = list(reversed([instr for instr in bytecode]))
    for (ix, instr) in enumerate(instrs):
        # print(ix, instr)
        if instr.opname==s:
            cnt += 1
    return cnt

def test_part5_run_normally1(capfd):
    try:
        from sprint_challenge.Part_5 import part5

        part5([ 75, 25, 6, 73, 43, 46, 31, 13, 60, 90, 5, 43, 35, 65, 100, 28, 83, 95, 35, 45, -1 ])
        out, err = capfd.readouterr()

        assert out == """0 점대 - : 2 명
10 점대 - : 1 명
20 점대 - : 2 명
30 점대 - : 3 명
40 점대 - : 4 명
50 점대 - : 0 명
60 점대 - : 2 명
70 점대 - : 2 명
80 점대 - : 1 명
90 점대 - : 2 명
100 점대 - : 1 명
"""
    
    except ImportError:
        fail("코드에서 문제가 발생했습니다. 다시한번 확인해주세요")

    except Exception as e:
        print(e)
        fail("에러가 발생합니다. 에러를 해결해주세요")

    

def test_part5_run_normally2(capfd):
    try:
        from sprint_challenge.Part_5 import part5

        part5([64, 68, 83, 21, 89, 53, 38, 31, 81, 12, 75, 7, 55, -1 ])
        out, err = capfd.readouterr()

        # assert out == '0 점대 - : 1 명\n10 점대 - : 1 명\n20 점대 - : 1 명\n30 점대 - : 2 명\n40 점대 - : 0 명\n50 점대 - : 2 명\n60 점대 - : 2 명\n70 점대 - : 1 명\n80 점대 - : 3 명\n90 점대 - : 0 명\n100 점대 - : 0 명\n'
        assert out == """0 점대 - : 1 명
10 점대 - : 1 명
20 점대 - : 1 명
30 점대 - : 2 명
40 점대 - : 0 명
50 점대 - : 2 명
60 점대 - : 2 명
70 점대 - : 1 명
80 점대 - : 3 명
90 점대 - : 0 명
100 점대 - : 0 명
"""
    
    except ImportError:
        fail("코드에서 문제가 발생했습니다. 다시한번 확인해주세요")

    except Exception as e:
        print(e)
        fail("에러가 발생합니다. 에러를 해결해주세요")


def test_part5_run_normally3(capfd):
    try:
        from sprint_challenge.Part_5 import part5

        part5([1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 100, -1 ])
        out, err = capfd.readouterr()

        assert out == """0 점대 - : 1 명
10 점대 - : 1 명
20 점대 - : 1 명
30 점대 - : 1 명
40 점대 - : 1 명
50 점대 - : 1 명
60 점대 - : 1 명
70 점대 - : 1 명
80 점대 - : 1 명
90 점대 - : 1 명
100 점대 - : 1 명
"""
    
    except ImportError:
        fail("코드에서 문제가 발생했습니다. 다시한번 확인해주세요")

    except Exception as e:
        print(e)
        fail("에러가 발생합니다. 에러를 해결해주세요")



def test_part5_statements():
    
    try:
        from sprint_challenge.Part_5 import part5
        assert list_func_calls(part5,"POP_JUMP_IF_FALSE") <= 3, '조건문 사용은 3번 이하입니다!'
        assert list_func_calls(part5,"FOR_ITER") <= 3, '반복문 사용은 3번 이하입니다!'
    
    except ImportError:
        fail("코드에서 문제가 발생했습니다. 다시한번 확인해주세요")

    except Exception as e:
        print(e)
        fail("에러가 발생합니다. 에러를 해결해주세요")