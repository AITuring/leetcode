'''
思路：
	应该就是先将两个数组合并起来，然后找中间的元素,
	如果总数组长度为奇数,那么就找中间的那个元素输出(如果9个,中间为[9/2]+1=5个)
	偶数的话中间两个（10个，第5和第6个）

'''
def findMedianSortedArrays( nums1, nums2):
    a = []
    for i in nums1:
        a.append(i)
    for i in nums2:
        a.append(i)
    a.sort()
    print(a)
    l = len(a)
    print(l)
    if l % 2 != 0:
        return a[l // 2 ]
    else:
        print(l//2)

        return (a[l // 2 -1] + a[l // 2 ]) / 2


if __name__ == "__main__":
    nums1=[1,2]
    nums2=[3]
    print(findMedianSortedArrays(nums1,nums2))
