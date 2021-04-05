def binarySearch(arr:list[int])->int:
    if len(arr)<2:
        return 0

    l, r = 0,len(arr)
    while l<r:
        m = int((r+l)/2)
        if arr[m]==1:
            l=m
        else:
            if arr[m-1]==1:
                return m
            else:
                r=m
    return -1

print(binarySearch([1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
