class Solution(object):
    def wiggleMaxLength(self, nums,a):
        n = a
        if n <= 1:
            return n
        inc, dec = [1] * n, [1] * n
        for x in range(n):
            for y in range(x):
                if nums[x] > nums[y]:
                    inc[x] = max(inc[x], dec[y] + 1)
                elif nums[x] < nums[y]:
                    dec[x] = max(dec[x], inc[y] + 1)
        return max(inc[-1], dec[-1])
val=Solution()
a=int(input())
nums=list(map(int,input().split()))
print(val.wiggleMaxLength(nums,a))
