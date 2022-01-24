"""
Advanced Requirements
새로운 자료구조를 찾아보고 공부해보세요.

요구사항:
    Deque가 무엇인지 구글링을 통해 공부해주세요.
    아래는 위키백과에 있는 Deque의 설명입니다. 
    https://ko.wikipedia.org/wiki/%EB%8D%B1_(%EC%9E%90%EB%A3%8C_%EA%B5%AC%EC%A1%B0)

    Deque에 대해서 공부가 끝났다면 이제 구현해볼 차례입니다. 
    오늘 공부한 LinkedList를 사용하여 Deque를 구현해주세요.
    collection 라이브러리는 사용하지 마세요.
"""

class Node:
    """
    Deque 클래스에서 사용할 Node 클래스입니다.
    작성된 코드를 수정하거나 삭제하지 마세요.
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Deque:
    def __init__(self):
        """
        아래 코드는 수정하지 마세요.
        작성된 코드의 의도를 생각해보며 문제를 풀어주세요.
        """
        self.top = None
        self.bottom = None


    def append(self, item):
        """
        #. 문제 1.
        Deque에 item 매개변수로 들어온 값을 제일 마지막 노드로 집어넣는 메소드를 구현해주세요.

        input: item
            Deque로 들어갈 값입니다.
        output: 
            반환값은 없습니다.
        아래 pass를 지워주시고 코드를 작성해주시면 됩니다. 
        """
        pass


    def appendleft(self, item):
        """
        #. 문제 2.
        Deque에 item 매개변수로 들어온 값을 제일 앞 노드로 집어넣는 메소드를 구현해주세요.

        input: item
            Deque로 들어갈 값입니다.
        output: 
            반환값은 없습니다.
        아래 pass를 지워주시고 코드를 작성해주시면 됩니다. 
        """
        pass


    def pop(self):
        """
        #. 문제 3.
        Deque에 가장 뒤에 있는 값을 삭제하는 메소드를 구현해주세요.

        input: 
            input은 없습니다.
        output: 
            Deque에서 삭제된 값을 반환해주세요.
            만약 삭제한 값이 없다면 None을 반환해주세요.
        아래 pass를 지워주시고 코드를 작성해주시면 됩니다. 
        """
        pass


    def popleft(self):
        """
        #. 문제 4.
        Deque에 가장 앞에 있는 값을 삭제하는 메소드를 구현해주세요.

        input: 
            input은 없습니다.
        output: 
            Deque에서 삭제된 값을 반환해주세요.
            만약 삭제한 값이 없다면 None을 반환해주세요.
        아래 pass를 지워주시고 코드를 작성해주시면 됩니다. 
        """
        pass


    def ord_desc(self):
        """
        #. 문제 5.
        queue내부에 있는 값을 반환하는 메소드를 구현해주세요.

        input: 
            input은 없습니다.
        output: 
            queue내부에 있는 값을 리스트 형태로 반환해주세요.
        아래 pass를 지워주시고 코드를 작성해주시면 됩니다. 
        """
        pass
