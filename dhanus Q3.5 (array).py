def minjumps(arr,n):
    if (n<=2):
        return 0
    if (arr[0]==0):
        return -1
    maxreach=arr[0]
    step=arr[0]
    jump=1
    for i in range (1,n):
        if (1==n-1):
            return jump
        maxreach=max(maxreach,1+arr[i])
        step=1
        if (step==0):
                jump+=1
        if (i>=maxreach):
                return-1
        step=maxreach-i
    return-1
arr=[1,3,5,8,9,2,6,7,6,8,9]
size=len(arr)
print("minimum number of jumps to reach end is %d" % minjumps(arr,size))
