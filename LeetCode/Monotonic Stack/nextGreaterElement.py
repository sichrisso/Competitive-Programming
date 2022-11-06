def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    z = j + 1
                    while z <= len(nums2) - 1 and nums2[z] < nums2[j]:
                        z += 1
                    if z > len(nums2) - 1:
                        output.append(-1)
                    elif nums2[z] > nums2[j]:
                        output.append(nums2[z])
                    else:
                        output.append(-1)
                else:
                    pass
        return output