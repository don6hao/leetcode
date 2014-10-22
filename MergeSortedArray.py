class Solution:
    # @param A  a list of integers
    # @param m  an integer, size of A
    # @param B  a list of integers
    # @param n  an integer, size of B
    # @return nothing
    def merge(self, A, m, B, n):
        i = m-1
        j = n-1
        size = m+n-1

        while i >= 0 and j >= 0:
            if A[i] < B[j]:
                A[size] = B[j]
                j -= 1
            else:
                A[size] = A[i]
                i -= 1
            size -= 1

        while j >= 0:
            A[size] = B[j]
            size -= 1
            j -= 1
        return


a = []
b = []
p = Solution()
print p.merge(a, len(a), b, len(b))

print a
