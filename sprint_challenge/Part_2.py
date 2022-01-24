# 조건1 : 아래 클래스 계층형태에 따라 클래스를 생성하는 코드를 작성하세요.
# 조건2 : 아래 코드에서는 개별적으로 기능이 존재하지 않는 클래스이므로 별도의 코드는 작성할 필요없습니다.

# 클래스 계층구조:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]

###### 클래스 생성 ######

class Vehicle:
    def __init__(self):
      pass

class GroundVehicle(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)

class Car(GroundVehicle):
    def __init__(self):
        GroundVehicle.__init__(self)


class Motorcycle(GroundVehicle):
    def __init__(self):
        GroundVehicle.__init__(self)



class FlightVehicle(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)


class Starship(FlightVehicle):
    def __init__(self):
        FlightVehicle.__init__(self)

class Airplane(FlightVehicle):
    def __init__(self):
        FlightVehicle.__init__(self)
