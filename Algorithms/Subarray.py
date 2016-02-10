lst = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
left_sum = float('-inf')
low = 0
high = len(lst)
mid = (low + high)/2
sum = 0
for i in range(mid,low,-1):
    sum += lst[i]
    if sum > left_sum:
        left_sum = sum
        max_left = i
right_sum = float('-inf')
sum = 0
for j in range(mid + 1,high):
    sum += lst[j]
    if sum > right_sum:
        right_sum = sum
        max_right = j
print('The maximum subarray ranges from {0} - {1}. The sum is {2}'.format(max_left, max_right, left_sum + right_sum))