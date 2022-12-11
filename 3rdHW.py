# 시간 복잡도
# Delete       : O(log(n))
# Union        : o(len(m)+len(n))
# Intersection : o(len(m)+len(n))

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class bstSet:
    def __init__(self):
        self.items = []
        self.root = None

    def create(self): # 생성
        self.items = []
        self.root = None

    def display(self, msg):
        print(msg, self.items)

    def Add(self, elem):
        if elem not in self.items:
            self.items.append(elem)
        self.root = self._Add_value(self.root, elem)
        return self.root is not None

    def _Add_value(self, node, data): # 원소 추가
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._Add_value(node.left, data)
            else:
                node.right = self._Add_value(node.right, data)
        return node

    def Search(self, key):
        return self._Search_value(self.root, key)

    def _Search_value(self, root, key): # 원소 찾기
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._Search_value(root.left, key)
        else:
            return self._Search_value(root.right, key)

    def Delete(self, elem):
        if elem in self.items:
            self.items.remove(elem)
        self.root, Deleted = self._Delete_value(self.root, elem)
        return Deleted

    def _Delete_value(self, node, key): # 원소 삭제
        if node is None:
            return node, "False"
        Deleted = False
        if key == node.data:
            Deleted = True
            if node.left and node.right:
                # 노드의 맨 왼쪽에 있는 노드를 바꿈
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, Deleted = self._Delete_value(node.left, key)
        else:
            node.right, Deleted = self._Delete_value(node.right, key)
        return node, Deleted

    def Union(self, setB): # 합집합
        setC = bstSet()
        setC.items = list(self.items)
        for elem in setB.items:
            if elem not in self.items:
                setC.items.append(elem)
        return setC

    def Intersection (self, setB): # 교집합
        setC = bstSet()
        for elem in setB.items:
            if elem in self.items:
                setC.items.append(elem)
        return setC

    def __add__(self,setB): # 연산자 오버로딩 합집합 (재사용)
        setC = bstSet()
        setC.items = list(self.items)
        for elem in setB.items:
            if elem not in self.items:
                setC.items.append(elem)
        return setC

# RUN
array_A = [2, -6, 14, 3, -1, 2, 5]
A=bstSet()
A.create()
for x in array_A:
    A.Add(x)

array_B = [14, -3, -5, 9, 5, 9]
B = bstSet()
B.create()
for x in array_B:
    B.Add(x)

# Result
# 합집합 : 2, -6, 14, 3, -1, 5, -3, -5, 9
# 교집합 : 14, 5
A.Union(B).display("합집합:")
A.Intersection(B).display("교집합:")

# Search
print(A.Search(2)) # 집합에 2가 존재하므로 True 반환
print(A.Search(17)) # 집합에 17이 존재하지 않으므로 False 반환

# Delete
print(A.Delete(14)) # 집합에 14가 존재하므로 True 반환하고 삭제
print(A.Delete(3)) # 집합에 3이 존재하므로 True 반환하고 삭제
print(A.Delete(8)) # 집합에 8이 존재하지 않으므로 False 반환 -> 존재하지 않음

# 합집합 : 2, -6, -1, 5, 14, -3, -5, 9
# 교집합 : 5
A.Union(B).display("합집합:")
A.Intersection(B).display("교집합:")

# 연산자 오버로딩 합집합 연산
(A+B).display("연산자 오버로딩 합집합:")