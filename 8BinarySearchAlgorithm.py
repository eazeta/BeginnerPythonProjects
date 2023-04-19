# This purpose of this project is to play around with Binary searches

array = [2, 5, 7, 8, 12, 15, 16, 20, 22, 23, 25, 27, 30, 32, 35, 37, 40, 45, 50, 55]

def binarySearch(arr, value):
  left = 0
  right = len(arr)
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == value:
      return mid
    else:
      if arr[mid] > value:
        right = mid - 1
      elif arr[mid] < value:
        left = mid + 1
  return -1

print(binarySearch(array, 8))