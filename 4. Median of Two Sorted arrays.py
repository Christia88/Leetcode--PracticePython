class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #sorting
        arr3 = [None]*(len(nums1)+len(nums2))
        i, j, k = 0, 0, 0
    
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                arr3[k] = nums1[i]
                k += 1
                i += 1
            else:
                arr3[k] = nums2[j]
                k += 1
                j += 1
            
        while i < len(nums1):
            arr3[k] = nums1[i];
            k += 1
            i += 1
        
        while j < len(nums2):
            arr3[k] = nums2[j];
            k += 1
            j += 1


        #checking
        i=len(arr3)
        if i%2==1:
            g=int(i/2)
            median=arr3[g]
        else:
            g=int(i/2)-1
            median=(arr3[g]+arr3[g+1])/2

        return float(median)
