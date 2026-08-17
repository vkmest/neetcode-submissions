class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        
        def oneBinary(row, target):
            x, y = 0, len(row)-1
            while x<=y:
                m = (x+y) // 2
                if row[m] == target:
                    return True
                elif row[m] < target:
                    x = m+1
                elif row[m] > target:
                    y = m-1
            return False
        
        i,j = 0,n-1
        while i<=j:
            mid=(i+j)//2
            if matrix[mid][0]<=target<=matrix[mid][m-1]:
                return oneBinary(matrix[mid],target)
            elif target<matrix[mid][0]:
                j=mid-1
            elif matrix[mid][m-1]<target:
                i=mid+1
        return False









