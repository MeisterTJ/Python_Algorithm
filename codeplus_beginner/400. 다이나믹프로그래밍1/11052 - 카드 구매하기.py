# 11052 - 카드 구매하기
# n개의 카드, p1~pn 까지 각각의 가격을 매긴다.
# d[n] = 카드 가격의 덧셈 조합 중에 가장 가격이 큰 조합의 값
# d[n] = max(d[n-1] + p[1], d[n-2] + p[2],,,,, d[1] + p[n-1])
# d[n] = max(p[i] + d[n-i])  # 1 <= i <= n

if __name__ == "__main__":
    n = int(input())
    p = input().split(' ')  # 1 2 3 4 => 문자열 리스트로 저장

    d = [0 for i in range(0, n + 1)]

    # 시간 복잡도 N x N = O(N^2)
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            d[i] = max(d[i], d[i-j] + int(p[j - 1]))    # 현재의 d[i], 그에 맞는 모든 조합들을 비교해서 제일 큰 값 

    print(d[n])
