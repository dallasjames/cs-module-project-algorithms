"""
Input: a List of integers
Returns: a List of integers
"""


def moving_zeroes(arr):
    # Your code here
    right = []
    left = []
    for i in range(len(arr)):
        if arr[i] == 0:
            right.append(arr[i])
        else:
            left.append(arr[i])
    return left + right


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
