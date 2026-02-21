nums1 = [1,2,2,1]
nums2 = [2,2]

# seen1 = []
# # seen2 = set()


# for n1 in nums1:
#         if n1 in nums2:
#             seen1.append(n1)
# seen1 = set(seen1)
# seen1 = list(seen1)
# print(seen1)

# the above approach works, but is still inefficient as it has a high runtime because of loops
# we can use '&' i.e the intersection operator to find the common element

seen1 = set(nums1)
seen2 = set(nums2)

res = list(seen1 & seen2)

print(res)