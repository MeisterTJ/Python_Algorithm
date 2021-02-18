# 1463 - 1로 만들기

# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면, 2로 나눈다
# 3. 둘다 안되면 1을 뺀다
# 어떤 정수 N에 위와 같은 연산을 선택해서 1을 만드려고 한다. 연산을 사용하는 횟수의 최소값을 구하는 문제

# ex) 8->4->2->1    (3)
# ex) 9->3->1   (2)

# 10의 경우는 두 개의 방법이 있다.
# ex) 10->5->4->2->1 (4),  10->5->3->1 (3)

# d[n] = n을 1로 만드는 최소 연산 횟수
# d[n] = min(d[n/3], d[n/2], d[n-1]) + 1

# 함수의 재귀로 푸는 방법
# import sys
# sys.setrecursionlimit(10**6)    # 재귀의 제한을 1000000으로
# def go(n):
#     if n == 1:
#         return 0
#     if d[n] > 0:    # d[n]에 이미 값이 있다면 return 한다.
#         return d[n]
#
#     # 기본적으로 d[n] 은 n-1의 최소 연산 수로 설정한다.
#     d[n] = go(n-1) + 1
#
#     if n % 2 == 0:
#         temp = go(n//2) + 1  # n/2의 최소 연산 수를 구한다.
#         if d[n] > temp:
#             d[n] = temp
#
#     if n % 3 == 0:
#         temp = go(n//3) + 1  # n/3의 최소 연산 수를 구한다.
#         if d[n] > temp:
#             d[n] = temp
#     return d[n]
#
# if __name__ == "__main__":
#     n = int(input())
#     d = [0] * (n + 1)
#     print(go(n))


# bottom up 방식으로 풀기

if __name__ == "__main__":
    n = int(input())
    d = [0] * (n + 1)

    for i in range(2, n + 1):
        d[i] = d[i-1] + 1
        if i % 2 == 0 and d[i] > d[i//2] + 1:   # d[i-1] + 1 > d[i//2] + 1 일 경우
            d[i] = d[i//2] + 1
        if i % 3 == 0 and d[i] > d[i//3] + 1:   # (d[i-1] or d[i//2]) + 1 > d[i//3] + 1 일 경우
            d[i] = d[i//3] + 1

    print(d[n])


