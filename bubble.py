class Solution:
    def bubble_sort(self,A):
        for i in range(0,len(A)):
            for j in range(0,len(A)-1-i):
                if A[j] > A[j+1]:
                    A[j],A[j+1]=A[j+1],A[j]
        print("After Sorting !!")
        print(A)
if __name__ == "__main__":
    n=int(input("Enter array size:"))
    A = list(map(int,input().strip().split()))
    print("Before Sorting !!")
    print(A)
    obj = Solution()
    obj.bubble_sort(A)
