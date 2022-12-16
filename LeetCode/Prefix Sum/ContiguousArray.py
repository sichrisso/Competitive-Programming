def findMaxLength(nums):
    # c = Counter(nums)
    # print(len(nums))
    # print(c)
    # limit = min(c.values())
    limit = 3
    dict = {0:0, 1:0}
    l, r, output = 0, 0, 0
    while r < len(nums):
        if dict[nums[r]] <= limit:
            if nums[r] == 1:
                dict[1] += 1
            else:
                dict[0] += 1
            r += 1
        else:
            dict[nums[l]] -= 1
            l += 1
        if dict[0] == dict[1]:
            output = max(output, dict[0] + dict[1])
    return output

def main():
    nums = [0,0,1,0,0,0,1,1]
    findMaxLength(nums)

main()