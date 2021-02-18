# 1158 - 요세푸스 문제

n, m = map(int, input().split())
q = list(range(1, n + 1))       # 리스트를 range로 초기화
r = []                          # 빈 리스트
index = 0

while q:
    index = (index + m - 1) % len(q)
    r.append(str(q.pop(index)))

print('<', ', '.join(r), '>', sep='')   # <3, 6, 2, 7>
