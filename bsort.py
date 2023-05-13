def BubbleSort(A):
    n = len(A) # length of array A

    for i in range(n-1, -1, -1):
        min_idx = i

        for j in range (0, n-i-1, +1):
            if A[j] > A[min_idx]:
                min_idx = j  # Swap only when element is greater than the current minimum index.


data = [-2, 45, 0, 11, -9, 49 ,125 ,48, 205 ,152 ]

print ("My Data z",data)

BubbleSort(data)

print ("Sorted Data ",data)