# 16194 - 카드 구매하기2
# 카드 구매하기 1의 반대버전....
# n개의 카드를 구매하기 위해 지불해야하는 금액의 최소값을 구해야 한다.
# d[i] 의 초기값을 잘 결정해야 한다.

if __name__ == "__main__":
    n = int(input())
    p = [0] + list(map(int, input().split()))   # input.split으로 생성된 리스트의 모든 요소를 int로 변환하는 방법

    d = [-1 for i in range(0, n + 1)]   # -1을 초기값으로 넣어줘서 아직 정답을 구하지 않았음을 알려준다.
    d[0] = 0

    # 시간 복잡도 N x N = O(N^2)
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if d[i] == -1 or d[i] > d[i-j] + p[j]:    # d[i] 값이 정해져지지 않았거나, d[i]가 비교할 값보다 크다면
                d[i] = d[i-j] + p[j]    # 현재의 d[i], 그에 맞는 모든 조합들을 비교해서 제일 작은 값

    print(d[n])