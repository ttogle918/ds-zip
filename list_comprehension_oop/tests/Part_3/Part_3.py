import pytest


def test_part3_GroundVehicle():
    try:
        from sprint_challenge.Part_3 import GroundVehicle, Motorcycle

        gv = GroundVehicle()
        assert gv.drive() == 'vroong', "'GroudVehicle 클래스'에서 'vroong'을 반환하는 'drive() 메소드'를 추가하세요."
        assert gv.num_wheels == 4, "'GroudVehicle 클래스'에서 'num_wheels 변수'의 기본값이 4가 되도록 기본 생성자 코드를 작성하세요"
    
    except ImportError:
        pytest.fail("코드에서 문제가 발생했습니다. 다시한번 확인해주세요")

    except Exception as e:
        print(e)
        pytest.fail("에러가 발생합니다. 에러를 해결해주세요")

def test_part3_Motorcycle():
    
    try:
        from sprint_challenge.Part_3 import GroundVehicle, Motorcycle

        m = Motorcycle()
    
        assert GroundVehicle in Motorcycle.__mro__, "'GroundVehicle 클래스'의 서브클래스인 'Motocycle 클래스'를 선언해야합니다."
        assert m.num_wheels == 2, "'Motocycle 클래스'를 인스턴스화할 때, 자동으로 'num_wheels 변수'를 수퍼클래스의 생성자에 전달하여 2로 설정해야합니다."
        assert m.drive() == 'Bang', "'GroundVehicle 클래스'의 'drive() 메소드'를 오버라이드하고 'Bang'을 반환하도록 합니다."

    except ImportError:
        pytest.fail("코드에서 문제가 발생했습니다. 다시한번 확인해주세요")

    except Exception as e:
        print(e)
        pytest.fail("에러가 발생합니다. 에러를 해결해주세요")


def test_part3_print_methods(capfd):
    try:
        from sprint_challenge.Part_3 import GroundVehicle, Motorcycle, print_method

        print_method()

        out, err = capfd.readouterr()
        assert out == "vroong\nvroong\nBang\nvroong\nBang\n"
    
    except ImportError:
        pytest.fail("코드에서 문제가 발생했습니다. 다시한번 확인해주세요")

    except Exception as e:
        print(e)
        pytest.fail("에러가 발생합니다. 에러를 해결해주세요")