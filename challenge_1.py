def longestConsecutive(nums):
    longest = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current = 1

            while current_num + 1 in num_set:
                current_num += 1
                current += 1
            longest = max(longest, current)

    return longest


nums = [6, 8, 3, 5, 4, 7 ,10,11,12]
#print(solve(nums))
print (longestConsecutive(nums))


