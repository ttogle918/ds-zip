import pytest
import dis


def list_method_calls(fn):
    bytecode = dis.Bytecode(fn)
    instrs = list(reversed([instr for instr in bytecode]))
    num = 0
    for (ix, instr) in enumerate(instrs):
        if instr.opname=="CALL_METHOD" or instr.argval=="sha256":
            num += 1

    return num


@pytest.fixture(autouse=True)
def test_part1_import():
    try:
        from sprint_challenge.Part_1 import sha_hash_function

    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_part1_return_correct_answer():
    from sprint_challenge.Part_1 import sha_hash_function

    assert sha_hash_function() == ['b19cfa3a0f7cef07dc1dd1604cee0a49c57d0e1a4f1baa864ba1c7c2229b147f'], 'Test Name을 sha256함수를 통해 암호화한 값을 반환해야합니다.'


def test_part1_use_sha256_method():
    from sprint_challenge.Part_1 import sha_hash_function

    assert list_method_calls(sha_hash_function) > 0, 'sha256 메소드를 사용해야합니다'

