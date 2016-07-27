#!/usr/bin/py
# Head ends here
def pairs(nums, a ,k):
    #a contains array of numbers and k is the value of difference
    total = 0
    for i in range(0, len(b)):
        greater = a[i] + k
        less = a[i] - k
        if nums.has_key(greater):
            total += nums[greater]
        if nums.has_key(less):
            total += nums[less]

    return total / 2

# Tail starts here
if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    nums = {}
    for num in b:
        if nums.has_key(num):
            nums[num] += 1
        else:
            nums[num] = 1
    print pairs(nums, b,_k)
