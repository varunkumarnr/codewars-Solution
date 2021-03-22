def isValidSubsequence(arr, sequence):
    seqIdx = 0
    for val in arr:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == val:
            seqIdx+=1
    if seqIdx == len(sequence):
        print("the two arrays is subsequential")
    else:
        print("they are not sub sequential")


isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],[1, 22, -1, 10])





