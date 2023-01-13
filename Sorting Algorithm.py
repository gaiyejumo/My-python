##########################################################
# The following codes below shows some sorting algorithm written in python programming language.

def bubble_sort(nums):
      swapped = True
      while swapped:

            swapped = False
            for i in range(len(nums)-1):
                  if nums[i] > nums[i + 1]:

                        nums[i], nums[i + 1] = nums[i + 1]. nums[i]
                        swapped = True


#########################################################
def  selection_sort(nums):
      for i in range(len(nums)):
            lowest_value_index = i

            for j in range (i + 1, len(nums)):
                  if nums[j] < nums[lowest_value_index]:
                        lowest_value_index = j

            nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


#########################################################
def merge(left_list, right_list):
      sorted_list = []
      left_list_index = right_list_index = 0

      left_list_length, right_list_length  = len(left_list), len(right_list)

      for _ in range(left_list_length + right_list_length):
            if left_list_index < left_list_length and right_list_index < right_list_length:
                  if left_list[left_list_index] <= right_list[right_list_index]:
                        sorted_list.append(left_list[left_list_index])
                        left_list_index += 1

                  else:
                        sorted_list.apend(right_list[right_list_index])
                        right_list_index += 1

                  elif left_list_index == left_list_length:
                        sorted_list.append(right_list[right_list_index])
                        right_list_index += 1
                  elif right_list_index == right_list_length:
                        sorted_list.append(left_list[left_list_index])
                        left_list_index += 1

      return sorted_list

def merge_sort(nums):
      if  len(nums) <= 1:
            return nums

      mid = len(nums) // 2

      left_list = merge_sort(nums[:mid])
      right_list = merge_sort(nums[mid:])

      return merge(left_list, right_list)

#########################################################

# QUick sort
def partition(nums, low, high):
      pivot = nums[(low + high) // 2]
      i = low - 1
      j = high + 1
      while True:
            i += 1
            while nums[i] < pivot:
                  i += 1

            j -= 1
            while nums[j] > pivot:
                  j -= 1
            if i >= j:
                  return j

            nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
      def _quick_sort(items, low, high):
            if low < high:

                  split_index = partition(items, low, high)
                  _quick_sort(items, low, split_index)
                  _quick_sort(items, split_index + 1, high)
            _quick_sort(nums, 0, len(nums) - 1)
            
