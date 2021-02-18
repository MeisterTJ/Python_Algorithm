# 9093 - 단어 뒤집기
from sys import stdin
t = int(input())
name = stdin.read().splitlines()    # eof 될때까지 여러줄을 읽는다. name에 리스트로 저장된다.
res = []
for idx in range(t):
    res.append(" ".join([i[::-1] for i in name[idx].split()]))
print("\n".join(res))