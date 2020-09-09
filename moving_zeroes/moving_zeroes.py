"""
Input: a List of integers
Returns: a List of integers
"""


def moving_zeroes(arr):
    # Your code here
    newArr = []
    for i in range(len(arr)):
        if arr[i] == 0:
            newArr.append(arr[i])
        else:
            newArr.insert(0, arr[i])
    return newArr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
