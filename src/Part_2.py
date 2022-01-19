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
        pass



def oop_explain():
    """
    문제 2. OOP에 대해서 공부하신 내용들을 최대한 많이 작성해주세요.
    OOP의 구성에 대해서도 설명을 작성해주세요
    """

    answer = """
    
    """

    return answer