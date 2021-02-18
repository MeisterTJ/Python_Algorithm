# 1406 - 에디터
# 커서를 기준으로 왼쪽 글자는 왼쪽 스택, 오른쪽 글자는 오른쪽 스택에 넣는다는 개념이다.

import sys

left = list(sys.stdin.readline().strip())   # 초기 편집기에 입력되어 있는 문자열
right = list()  # 리스트
input()     # 입력할 명령어의 개수 (의미없으니 저장안함)

for cmd in sys.stdin:   # EOF 될 때까지 계속 입력
    if cmd[0] == 'L' and left:      # 커서를 왼쪽으로 한 칸 옮긴다.
        right.append(left.pop())
    elif cmd[0] == 'D' and right:   # 커서를 오른쪽으로 한 칸 옮긴다.
        left.append(right.pop())
    elif cmd[0] == 'B' and left:    # 커서 왼쪽에 있는 문자를 삭제한다.
        left.pop()
    elif cmd[0] == 'P':
        left.append(cmd[2])         # P x 일경우 cmd[0] = P,  cmd[2] = P 이다.

print(f"{''.join(left)}{''.join(right[::-1])}")