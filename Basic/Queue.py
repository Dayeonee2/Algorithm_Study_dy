### 큐 구현
# 큐는 선입선출(FIFO, First In First Out) 자료구조입니다.


from collections import deque

queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5) # deque에서 append는 list와 같음
queue.append(2)
queue.append(3)
queue.append(7)
print(queue)
queue.popleft() # deque에서 popleft를 지원, 왼쪽 원소를 지울 수 있음
print(queue)
queue.append(1)
queue.append(4)
print(queue)
queue.popleft()
print(queue)  # queue의 가장 앞에 있는 원소부터 출력

queue.reverse() # 역순으로 바꾸기
print(queue)
# 역순으로 바꿔야 큐임
# 왼쪽으로 들어오고 오른쪽으로 나간다