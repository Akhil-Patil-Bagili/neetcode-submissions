from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque()  # Stores indexes, not values

        left = 0

        for right in range(len(nums)):

            # 1. Remove smaller values from the back
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            # 2. Add the current index
            q.append(right)

            # 3. Remove the index that is outside the window
            if q[0] < left:
                q.popleft()

            # 4. Once the window reaches size k, record the maximum
            if right - left + 1 == k:
                result.append(nums[q[0]])
                left += 1

        return result