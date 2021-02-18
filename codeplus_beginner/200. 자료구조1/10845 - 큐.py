# 10845 - 큐

import sys
t = int(input())
q = []
res = []
L = sys.stdin.read().splitlines()
# for idx in range(t):
#     # b는 가변인자로서 push 뒤의 값들을 리스트로 받는다.
#     a, *b = L[idx].split()
#     if "push" in a:
#         q.append(b[0])  # b[0]으로 push 뒤의 한 값만 받는다.
#     elif a == "front":  # 큐의 가장 앞에 있는 정수 출력 한다.
#         res.append(q[0] if q else "-1")
#     elif a == "back":   # 큐의 가장 뒤에 있는 정수 출력 한다.
#         res.append(q[-1] if q else "-1")
#     elif a == "size":   # 큐에 들어있는 정수의 개수를 출력한다.
#         res.append(str(len(q)))
#     elif a == "empty":  # 큐가 비어있으면 1, 아니면 0을 출력한다.
#         res.append('0' if q else "1")
#     elif a == "pop":    # 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다.
#         res.append(q.pop(0) if q else "-1")
# print("\n".join(res))


# q.pop(0)은 가장 앞을 삭제후 뒤의 모든 원소를 앞으로 끌어당기기 때문에 성능이 안좋다
# CPython으로 구현된 덱을 사용해본다.
from collections import deque
q = deque()
for idx in range(t):
    # b는 가변인자로서 push 뒤의 값들을 리스트로 받는다.
    a, *b = L[idx].split()
    if "push" in a:
        q.append(b[0])  # b[0]으로 push 뒤의 한 값만 받는다.
    elif a == "front":  # 큐의 가장 앞에 있는 정수 출력 한다.
        res.append(q[0] if q else "-1")
    elif a == "back":   # 큐의 가장 뒤에 있는 정수 출력 한다.
        res.append(q[-1] if q else "-1")
    elif a == "size":   # 큐에 들어있는 정수의 개수를 출력한다.
        res.append(str(len(q)))
    elif a == "empty":  # 큐가 비어있으면 1, 아니면 0을 출력한다.
        res.append('0' if q else "1")
    elif a == "pop":    # 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다.
        res.append(q.popleft() if q else "-1")
print("\n".join(res))
