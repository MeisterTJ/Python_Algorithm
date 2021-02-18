# 2747 - 피보나치 수

# 피보나치를 for문으로 푸는 방법
# n = int(input())
# arr = [0 for i in range(n + 1)]
# arr[1] = 1
#
# for i in range(2, n + 1):
#     arr[i] = arr[i-1] + arr[i-2]
#
# print(arr[n])


# 피보나치를 재귀, 메모로 푸는 방법
def fibonacci(n):
    if n <= 1:
        return n
    else:
        if memo[n] > 0:     # 메모 되어있으면 리턴한다.
            return memo[n]
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
        return memo[n]


if __name__ == "__main__":
    n = int(input())
    memo = [0 for i in range(n + 1)]
    print(fibonacci(n))
