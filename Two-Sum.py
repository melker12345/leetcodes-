
# Problem: Two Sum
# Problem Statement: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to the target.
# Constraints:
#   Each input would have exactly one solution.
#   You may not use the same element twice.
#   You can return the answer in any order.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6


for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print([i,j])