class Solution:
    def merge_sort(self,A):
        self.merge_sort2(A,0,len(A)-1)
    def merge_sort2(self,A,first,last):
        if first < last:
            middle = (first+last) // 2
            self.merge_sort2(A,first,middle)
            self.merge_sort2(A,middle+1,last)
            self.merge(A,first,middle,last)
    def merge(self,A,first,middle,last):
        L = A[first:middle+1]
        R = A[middle+1:last+1]
        L.append(9999999)
        R.append(9999999)
        i=j=0
        for k in range(first,last+1):
            if L[i] <= R[j]:
                A[k] = L[i]
                i +=1
            else:
                A[k] = R[j]
                j += 1
        print("After Sorting !!")
        print(A)
if __name__ == "__main__":
    n=int(input("Enter array size:"))
    A = list(map(int,input().strip().split()))
    print("Before Sorting !!")
    print(A)
    obj = Solution()
    obj.merge_sort(A)
