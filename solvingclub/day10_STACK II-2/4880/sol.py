import sys
sys.stdin = open("input.txt", "r")




# # 리스트 나누는 함수
# def f(i, j, lst):
#     n = (i + j)//2
#     left_lst = lst[0:n]
#     right_lst = lst[n:]
#     while l_win:
#         l_win = win(left_lst[0], left_lst[-1], left_lst)
#         r_win = win(right_lst[0], right_lst[-1], right_lst)
#         win(l_win)
#         win(r_win)
#     return l_win
#
#
#

#
T = int(input())
for tc in range(1, T+1):

    def f(i, j):  # i~j번까지의 승자를 찾는 함수
        if i == j:  # 한 명만 남은 경우
            return i  # i가 이김
        else:  # 두 명 이상인 경우 두 그룹의 승자를 찾아 최종 승자를 가림
            left = f(i, (i + j) // 2)  # 왼쪽 그룹의 승자
            right = f((i + j) // 2 + 1, j)  # 오른쪽 그룹의 승자
            return win(left, right)  # 두 그룹의 승자를 찾는 함수 구현


    def win(left, right):
        lft = card_list[left-1] # 인덱스 0번은 i번째, 인덱스 j-1번은 j번째 사람임
        rht = card_list[right-1] # 따라서 left, right는 순번이므로 인덱스로 취급하기 위해 1을 빼줌
        if lft - rht == 1:
            return left
        elif lft - rht == -1:
            return right
        elif lft - rht == -2:  # x가 가위고 y가 보인 경우
            return left
        elif lft - rht == 2:  # x가 보고, y가 가위인 경우
            return right
        elif lft - rht == 0:  # 비기는 경우
            return left

    N = int(input())
    card_list = list(map(int, input().split()))
    # print(card_list)
    i = 1   # 첫번째 사람
    j = N   # N번째 사람
    print(f'#{tc} {f(i, j)}')

