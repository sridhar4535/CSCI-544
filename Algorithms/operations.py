def minOps(A, B):
    m = len(A)
    n = len(B)

    # This part checks whether conversion is possible or not
    if n != m:
        return -1

    count = [0] * 256

    for i in A:        # count characters in A
        count[ord(i)] += 1
    for i in B:        # subtract count for every char in B
        count[ord(i)] -= 1
    for i in range(256):    # Check if all counts become 0
        if count[i] != 0:
            return -1

    # This part calculates the number of operations required
    res = 0
    i = n-1
    j = n-1
    while i >= 0:

        # if there is a mismatch, then keep incrementing
        # result 'res' until B[j] is not found in A[0..i]
        while i >= 0 and A[i] != B[j]:
            i -= 1
            res += 1

        # if A[i] and B[j] match
        if i >= 0:
            i -= 1
            j -= 1

    return res
A = "ABC"
B = "CBA"
print ("Minimum number of operations required is " + str(minOps(A,B)))