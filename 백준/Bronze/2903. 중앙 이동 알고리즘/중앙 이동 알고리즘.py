def find_total_points(N):
    # 한 변에 있는 점의 수 계산
    points_per_side = 2**N + 1
    # 전체 점의 수 계산
    total_points = points_per_side**2
    return total_points

# 입력
N = int(input())
# 결과 출력
print(find_total_points(N))
