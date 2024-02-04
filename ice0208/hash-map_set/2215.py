class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        # set을 이용하여 중복을 제거후, 차집합으로 정답 구하기

        answer = [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]
        return answer


if __name__ == "__main__":
    print(Solution().findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6]))
    print(Solution().findDifference(nums1=[1, 2, 3, 3], nums2=[1, 1, 2, 2]))
