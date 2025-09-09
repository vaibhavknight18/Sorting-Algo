class Solution:
    def selection_sort(self,A):
        for i in range(0,len(A)-1):
            minIdx = i
            for j in range(i+1,len(A)):
                if A[j] < A[minIdx]:
                    minIdx = j
            if minIdx != i:
                A[i],A[minIdx] = A[minIdx],A[i]
        print("After Sorting !!")
        print(A)
if __name__ == "__main__":
    A = [5,3,7,1]
    print("Before Sorting !!")
    print(A)
    obj = Solution()
    obj.selection_sort(A)
