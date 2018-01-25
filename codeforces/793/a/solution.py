def answer(k, nums):
    r = nums[0] % k

    for i in range(1, len(nums)):
        if nums[i] % k != r:
            return -1

    m = min(nums)
    sec = 0
    for n in nums:
        sec += (n - m) // k

    return sec
    

if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(answer(k, nums))
