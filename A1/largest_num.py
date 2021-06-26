"""
Divide and Conquer helper function to search for largest number
"""
def search(S: list[float], start: int, end: int, ret: float) -> float:
    # size of arr is 0
    if start == end:
        return S[start] # O(1)
    # size of arr is 2
    if start+1 == end:
        return max(S[start], S[end]) # O(1)

    mid = (start + end) // 2
    cur = S[mid]
    # both subarrays sorted or size of arr is 3
    if S[mid+1] <= S[end] and S[start] <= S[mid-1]:
        return max(S[mid], S[mid-1], S[end], ret) # O(1)
    # right subarray sorted
    if S[mid+1] < S[end] and S[start] > S[mid-1]:
        ret = S[end]

"""
Returns the largest number from an incorrectly sorted list.
All elements are unique.
"""
def get_largest_num(S: list[float]) -> float:
    start = 0
    end = len(S) - 1
    ret = float('-inf')
    result = search(S, start, end, ret)

    return result
