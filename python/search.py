class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1
        while start <= end:
            midd = (start + end) // 2
            if self.isBetween(matrix[midd], target):
                return self.findInd(matrix[midd], target)  
            elif target < matrix[midd][0]:
                end = midd - 1
            else:
                start = midd + 1
        return False  

    def findInd(self, arr, target): 
        st = 0
        en = len(arr) - 1  
        while st <= en:
            midd = (st + en) // 2
            if arr[midd] == target:
                return True
            elif target < arr[midd]:
                en = midd - 1
            else:
                st = midd + 1
        return False

    def isBetween(self, arr, target):  
        return arr[0] <= target <= arr[-1]  