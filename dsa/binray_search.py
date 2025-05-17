def binary_search(list, target):
  first = 0
  last = len(list) - 1
  while first <= last:
    mid = (first + last) // 2
    if list[mid] == target:
      return mid
    elif list[mid] < target:
      first = mid + 1
    else:
      last = mid - 1

  return None

print(binary_search([3,5, 8, 9, 13, 34, 38], 34))