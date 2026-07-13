from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        buckets = [[] for _ in range(len(nums)+1)]

        for key, freq in count.items():
            buckets[freq].append(key)
        
        print(buckets)

        res = []

        for freq in range(len(buckets)-1, 0, -1):
            for bucket in buckets[freq]:
                res.append(bucket)
                if len(res) == k:
                    return res
        