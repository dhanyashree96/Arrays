def getMinmax(l,h,arr):
    a_max=a[l]
    a_min=a[l]
    if l==h:
        a_max=a[l]
        a_min=a[l]
        return(a_max[l],a_min[l])
    elif h==l+1:
        if h>l:
            a_max=a[h]
            a_min=a[l]
        else:
            a_max=a[l]
            a_min=a[h]
            return (a_max,a_min)
    else:
        mid=int(l+h)/2
        a_max1,a_min1=getMinmax(l,mid,a)
        a_max2,a_min2=getMinmax(mid+1,h,a)
        return (max(a_max2,a_min2),min(a_max1,a_min1))
if __name__=='__main__':
    print('enter the size of array')
    n=int(input())    
    print('enter the array')
    a=list(map(int,input().strip().split()))
    h=len(a)-1
    l=0
    a_max,a_min=getMinmax(l,h,a)
    print('Maximum element in the array',a_max)
    print('Minimum element in the array',a_min)
