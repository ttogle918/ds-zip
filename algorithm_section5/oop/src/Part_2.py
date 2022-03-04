"""
Bare Minimum Requirements

요구사항:
    아래 문제들을 확인하며 하나씩 문제를 풀어주세요.    
"""

class Computer:
    """
    ## Computer 클래스의 코드는 수정하지 마세요 ##
    이미 완성된 코드입니다.
    아래 코드를 활용하여 문제를 해결해주세요.
    """
    def __init__(self, cpu, ram):
        self.CPU = cpu
        self.RAM = ram
        
    def browse(self):
        return('browse')

    def work(self):
        return('work')
        

class Laptop(Computer):
    """
    위에 작성된 Computer 클래스를 상속받는 Laptop 클래스를 완성해주세요. 
    """
    def __init__(self, cpu, ram, battery):
        """
        문제 1.
            Laptop 클래스의 생성자 함수를 완성해주세요.
            Laptop은 컴퓨터에 기본적으로 들어가는 부품 이외에 배터리도 추가됩니다.
            Computer 클래스에서 사용하는 변수에 battery를 추가해주세요.

            super키워드를 사용하여 상속받는 클래스에서 부모 클래스의 생성자를 사용하는 방법에 대해 익혀주세요.
        """
        Computer.__init__(self, cpu, ram)
        self.battery = battery



def oop_explain():
    """
    문제 2. OOP에 대해서 공부하신 내용들을 최대한 많이 작성해주세요.
    OOP의 구성에 대해서도 설명을 작성해주세요
    """

    answer = """
    OOP는 Object Oriental Programing으로 객체 지향 프로그래밍 방법론이다.
    객체끼리의 대화로 보면 된다.\n
    '상속'의 개념은 부모클래스의 기능을 자식클래스가 받아올 수 있는 것을 의미하는데, 자식클래스는 추가로 수정하여 본인의 입맛에 맞게 사용할 수 있다.
    '캡슐화'를 통해 특정 정보(변수, 메소드)를 바로 접근할 수 없도록 '은닉화'하여 데이터를 보호할 수 있다.\n
    '모듈화'로 기능이 분리되었기 때문에 재사용이 가능하다.( 함수, 메소드, 클래스 )\n
    '추상화'를 통해 객체들의 공통적 요소를 묶어주어 해당 요소는 추상클래스에서 받고, 다른 특성은 각자의 클래스를 통해 지정해주는 것이다.\n
    '다형성'은 상속을 통해 기능을 확장하거나 변경하는 것을 가능하게 하는 것으로 각 클래스가 같은 메소드이지만 다양한 형태를 띄고 있음을 의미한다.
    \n\noverriding과 overloading도 다형성의 개념을 통해 만들어진 메소드이다.
    overriding은 자식클래스에서 부모클래스의 메소드를 수정하여 재창조한 것을 의미한다.
    
    \noverloading은 하나의 클래스에서 같은 이름의 메소드를 사용하지만 다른 용도로 사용되는 것을 의미한다.
    overloading을 통해 해당 메소드를 부를 때 매개변수의 개수와 데이터타입을 다양하게 사용할 수 있다. 
    """

    return answer