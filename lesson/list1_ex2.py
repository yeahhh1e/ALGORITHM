N = 5
arr = [7, 2, 5, 3, 4, 1]

for i in range(N-1, 0, -1): # 각 구간의 끝 인덱스 i
# 각 구간에서 두 개씩 비교할 때 왼쪽 원소의 인덱스 j
# 왼쪽 원소가 더 크면 교환
