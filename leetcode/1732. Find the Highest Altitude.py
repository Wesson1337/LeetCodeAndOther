class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        max_altitude = 0
        curr_altitude = 0

        for curr_gain in gain:
            curr_altitude += curr_gain
            max_altitude = max(curr_altitude, max_altitude)

        return max_altitude


print(Solution().largestAltitude([-4,-3,-2,-1,4,3,2]))