def hasOnlyOneChild(pre):
    n = len(pre)
    for i in range(n-1):
        diff1 = pre[i+1] -pre[i]
        diff2 = pre[n-1] - pre[i]
        if diff1*diff2 < 0:
            return False
    return True

print(hasOnlyOneChild([8, 3, 5, 7, 6]))