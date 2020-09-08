"""
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
"""


def sliding_window_max(nums, k):
    # Your code here
    maxi = []
    tempi = []
    if len(nums) < k:
        return False
    for i in range(k):
        tempi.append(nums[i])
    maxi.append(max(tempi))
    for j in range(k, len(nums)):
        tempi.pop(0)
        tempi.append(nums[j])
        maxi.append(max(tempi))
    return maxi


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
