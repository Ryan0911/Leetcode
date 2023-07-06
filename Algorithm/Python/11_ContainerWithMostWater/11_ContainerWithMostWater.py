height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
ans = 0
left_point = 0
right_point = len(height) - 1
while left_point < right_point:
    ans = max(ans, min(height[left_point],
                       height[right_point]) * (right_point - left_point))
    if(height[left_point] < height[right_point]):
        left_point = left_point+1
    else:
        right_point = right_point-1
print(ans)
