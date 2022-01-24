"""
Bare Minimum Requirements
연결리스트의 개념은 변수의 인덱스에 직접접근하는 배열개념과는 다릅니다.
참조의 개념을 활용하여 변수에 접근하는 방법을 익혀봅니다.

요구사항:
    주어진 문제는 연결리스트지만 독립적으로 개념이 운용되는 것은 아닙니다.

    연결리스트를 구현해주세요.
    각 메소드에 작성되어있는 문제를 확인하여 코드를 작성해주세요.

    단 collections 라이브러리는 사용하지 마세요.
    메소드 이름은 변경하지 마세요.
    메소드의 매개변수를 추가하거나 삭제하지 마세요.
"""

class Node:
    def __init__(self,value,next=None):
        """
        # 문제 1.
        Linkedlist에서 사용할 Node의 생성자 함수를 구현해주세요.
        
        input: value, next
            value: Node의 값
            next: 생성될 Node의 다음 Node, 기본값은 None
        output:
            반환값은 없습니다.
        아래 pass를 지워주시고 코드를 작성해주시면 됩니다. 
        """
        pass


class linked_list:
    def __init__(self, value):
        """
        # 문제 2.
        Linkedlist의 생성자 함수를 구현해주세요.
        
        input: value
            value: Linkedlist의 Head Value
        output:
            반환값은 없습니다.
        아래 pass를 지워주시고 코드를 작성해주시면 됩니다. 
        """
        pass


    def add_node(self, value):
        """
        # 문제 3.
        Linkedlist에 새로운 Node를 추가하는 메소드를 작성해주세요.
        
        input: value
            value: Linkedlist에 들어올 새로운 Node Value
        output:
            반환값은 없습니다.
        아래 pass를 지워주시고 코드를 작성해주시면 됩니다. 
        """
        pass


    def del_node(self,value):
        """
        # 문제 4.
        Linkedlist에 value값을 가지고 있는 Node를 삭제하는 메소드를 작성해주세요.
        
        input: value
            value: Linkedlist에서 삭제할 Node Value
        output:
            값을 삭제하였다면 삭제한 Node의 value를 반환
            만약 LinkedList에 값이 없다면 None 반환
        아래 pass를 지워주시고 코드를 작성해주시면 됩니다. 
        """
        pass


    def ord_desc(self):
        """
        # 문제 4.
        Linkedlist에 저장된 값들을 리스트 형태로 반환하는 메소드를 작성해주세요.
        
        input: 
            input값은 없습니다.
        output:
            Linkedlist의 Head부터 시작하여 저장된 모든 Node의 Value들을
            리스트 형태로 반환해주세요.
        아래 pass를 지워주시고 코드를 작성해주시면 됩니다. 
        """
        pass


    def search_node(self,value):
        """
        # 문제 5.
        Linkedlist에 value값이 어디에 위치하는지 찾는 메소드를 작성해주세요.
        
        input: value
            value: Linkedlist내부에서 찾고자 하는 값
        output:
            연결리스트에서 value를 가진 노드를 찾아 노드를 반환
            아래 pass를 지워주시고 코드를 작성해주시면 됩니다.
        """
        pass

