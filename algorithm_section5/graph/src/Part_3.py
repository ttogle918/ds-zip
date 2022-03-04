"""
Advanced Requirements
대표적으로 활용할 수 있는 순회를 구현합니다.

요구사항:
    노드가 움직일 수 있는 경로는 다양합니다.
    순회라는 개념또한 일반적으로 많이 쓰이는 용어이지만 컴퓨터는 순회를 직관적으로 받아들이지 못합니다.
    컴퓨터가 받아들일 수 있는 순회를 구현합니다.

    중위순회를 구현하도록 합니다.
    강의노트에서 배웠던 재귀를 활용하지 않고 주어진 클래스와 함수 내에 구현을 완료하도록 합니다.

    트리를 따로 구현하지 않으셔도 됩니다.
    트리를 구성하는 노드의 형태는 다음과 같습니다
        class node:
            def __init__(self, data):
                self.data = data
                self.left = None
                self.right = None
"""
def in_order_traversal(root_node):  #  -> L M R
    if root_node is None :
      return None

    stack = [root_node]    # stack
    left_node = root_node.left
    
    while left_node :   # left_node가 존재한다면 가장 아래 가장 왼쪽 node까지 찾기 
      stack.append(left_node)
      left_node = left_node.left

    answer = []

    # stack에서 하나씩 꺼내서 그 node의 right까지 확인
    while stack :
      node = stack.pop()  # 마지막 삽입한 node를 꺼내오기
      answer.append(node.data)

      if node.right :   # node.right가 존재한다면
        left_node = node.right.left   # 그 node의 left가 존재하는가?
        stack.append(node.right)

        while left_node :   # left_node가 존재한다면
          stack.append(left_node)
          left_node = left_node.left
  
    return answer