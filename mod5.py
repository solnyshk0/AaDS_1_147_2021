#задача 2
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def add(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.add(data)
            else:
                self.right = Node(data)


def height(tree):
    if tree is None:
        return 0
    return max(height(tree.left), height(tree.right))+1


def build_tree(elements): 
    root = Node(elements[0]) #создаем элемент класса
    for i in range(1, len(elements)):
        root.add(elements[i]) #добавляем элементы в дерево
    return root


def balance(tree):
    if not tree or ((height(tree.left) == height(tree.right) or height(tree.left)+1 == height(tree.right) or height(tree.left) == height(tree.right)+1) and balance(tree.right) and balance(tree.left)): #условие сущ-ния дерева, чтобы высота левого и правого отличались не больше, чем на 1, возможность выполнения метода для его правой и левой частей
        return True
    return False


numbers = [int(i) for i in input().split()] #вводим массив
numbers.pop()  #удаляем последний 0
tree = build_tree(numbers) #строим дерево
if balance(tree): #если возвращается True
    print("YES")
else:
    print("NO")

#задача 3
from math import gcd #чтобы использовать нод; ну а весь остальной код был написан с вами на занятии, только там мы  максимум искали

def build(v, l, r, it, nums): 
    if r-l == 1:
        it[v] = nums[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, it, nums)
    build(2*v+2, m, r, it, nums)
    it[v] = gcd(it[2*v+1], it[2*v+2])

def get_NOD(v, l, r, it, ql, qr):
    if ql <= l and qr >= r:
        return it[v]
    if ql >= r or qr <= l: #если слева больше, чем справа(или наоборот), то возвращаем 0
        return 0
    m = (r+l)//2
    tl = get_NOD(2*v+1, l, m, it, ql, qr)
    tr = get_NOD(2*v+2, m, r, it, ql, qr)
    return gcd(tl, tr)

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    it = [0]*4*n  
    build(0, 0, n, it, nums)
    q = int(input())
    index = []
    while q != 0:
        l, r = map(int, input().split())
        index.append(get_NOD(0, 0, n, it, l-1, r))
        q -= 1
    print(*index)

main()

#задача 5
from math import gcd 
def build(v, l, r, it, a):
    if r-l == 1: 
        it[v] = a[l]
        return
    m = (l+r)//2
    build(2*v + 1, l, m, it, a)
    build(2*v + 2, m, r, it, a)
    it[v] = gcd(it[2*v + 1], it[2*v + 2])

def getNOD(v, l, r, it, ql, qr):
    if ql <= l and qr >= r: 
        return it[v]
    if ql >= r or qr <= l: 
        return 0
    m = (l+r)//2
    tl = getNOD(2*v + 1, l, m, it, ql, qr)
    tr = getNOD(2*v + 2, m, r, it, ql, qr)
    return gcd(tl, tr)

def update(v, l, r, it, indx, val):
    if r - l == 1:
        it[v] = val
        return
    middle = (r+l)//2
    if indx < middle:
        update(v*2+1, l, middle, it, indx, val)
    else:
        update(v*2+2, middle, r, it, indx, val)
    it[v] = gcd(it[2*v + 1], it[2*v + 2])

def main():
    n = int(input())
    it = [0]*(4*n) 
    a = list(map(int, input().split()))[:n]
    build(0, 0, n, it, a)
    q = int(input())
    res = []
    while q !=0:
        type_q, l, r = map(str, input().split())
        if type_q == "s":
            res.append(getNOD(0, 0, n, it, int(l)-1, int(r)))
        else:
            update(0, 0, n, it, int(l)-1, int(r))
        q-=1
    print(*res)
main()
