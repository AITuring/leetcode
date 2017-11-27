def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    x=int(x)#12321
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    digits = 1
    while x / digits >= 10:#12321
        digits *= 10#digits=10

    while digits > 1:
        right = x % 10 #right=1
        print('right=',right)
        left = x // digits
        print('left=',left)
        if left != right:
            return False
        x = (x % digits) / 10

        digits /= 100
    return True


if __name__ == '__main__':
    x = input('num\n:')
    print(isPalindrome(x))
