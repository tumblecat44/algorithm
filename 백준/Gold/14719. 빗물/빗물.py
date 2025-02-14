h,w = map(int,input().split())
a = list(map(int,input().split()))

left, right = 0, len(a)-1
left_max, right_max = a[left], a[right]
res = 0
while left < right:
    left_max, right_max = max(left_max, a[left]), max(right_max, a[right])
    if left_max <= right_max:
        res += left_max - a[left]
        left += 1
    else:
        res += right_max - a[right]
        right -= 1
print(res)