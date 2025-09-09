class Solution:
    def insertion_sort(A):
        for i in range(1,len(A)):
            for j in range(i-1,0,-1):
                if A[j] > A[j+1]:
                    A[j],A[j+1] = A[j+1] , A[j]
                else:
                    break
        print("After Sorting !!")
        print(A)
if __name__ == "__main__":
    A = [5,3,7,1]
    print("Before Sorting !!")
    print(A)
    obj = Solution()
    Solution.insertion_sort(A)
