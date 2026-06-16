from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        cloned_nums = nums.copy()
        self.merge_sort(cloned_nums)
        return cloned_nums
    
    def merge_sort(self, nums: List[int]):
        n = len(nums)

        # An array with a single element is always sorted
        if n == 1:
            return nums

        # Left half of the array
        left_array = nums[:n//2]
        # Right half of the array
        right_array = nums[n//2:]

        # Performs merge sort on the left half array
        self.merge_sort(left_array)
        # Performs merge sort on the right half array
        self.merge_sort(right_array)

        # Performs the actual merge sort algorithm
        i = 0 # Tracks the left most element on the left array
        j = 0 # Tracks the right most element on the right array
        k = 0 # Tracks the index of the merged array
        while i < len(left_array) and j < len(right_array):
            # Compares the left most element on the left array with the left most element on the right array
            if left_array[i] < right_array[j]:
                # Places the smaller element in the correct position
                nums[k] = left_array[i]
                i += 1 # Updates the left array pointer
            else:
                # Places the smaller element in the correct position
                nums[k] = right_array[j]
                j += 1 # Updates the right array pointer
            k += 1 # Updates the merged array pointer
        
        # Add any remaining elements from the left array to the merged array
        while i < len(left_array):
            nums[k] = left_array[i] # Places the remaining elements from the left array into the merged array
            i += 1 # Updates the left array pointer
            k += 1 # Updates the merged array pointer
        
        # Add any remaining elements from the right array to the merged array
        while j < len(right_array):
            nums[k] = right_array[j] # Places the remaining elements from the right array into the merged array
            j += 1 # Updates the right array pointer
            k += 1 # Updates the merged array pointer
