## stack 구현
# 스택은 후입선출(LIFO, Last In First Out) 자료구조입니다.
# 아래로 쌓는 구조를 생각하기

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.append(1)
stack.append(4)
print(stack)
stack.pop()
print(stack[::-1])  # stack의 가장 위에 있는 원소부터 출력
print(stack)