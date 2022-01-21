import pytest


@pytest.fixture(autouse=True)
def test_part1_import():
    try:
        from sprint_challenge.Part_2 import Vehicle, FlightVehicle, GroundVehicle, Starship, Car, Motorcycle, Airplane
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_quesion2_part2_1():
    from sprint_challenge.Part_2 import Vehicle, FlightVehicle, GroundVehicle, Starship, Car, Motorcycle, Airplane
    
    assert Vehicle in FlightVehicle.__mro__, 'FlightVehicle은 Vehicle로부터 상속받아야합니다.'
    assert Vehicle in GroundVehicle.__mro__, 'GroundVehicle은 Vehicle로부터 상속받아야합니다.'
    assert FlightVehicle in Starship.__mro__, 'Starship은 FlightVehicle로부터 상속받아야합니다.'
    assert GroundVehicle in Car.__mro__, 'Car은 GroundVehicle로부터 상속받아야합니다.'
    assert GroundVehicle in Motorcycle.__mro__, 'Motorcycle은 GroundVehicle로부터 상속받아야합니다.'
    assert FlightVehicle in Airplane.__mro__, 'Airplane은 FlightVehicle로부터 상속받아야합니다.'