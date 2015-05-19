#quick sort like that:
#pick one num as the flag and put the smaller to the left,put the bigger to righ#t.
#quick sort
def quickSort(L, low, high):
    i = low 
    j = high
    if i >= j:
        return L
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j = j-1        
        L[i] = L[j]
        while i < j and L[i] <= key:    
            i = i+1
        L[j] = L[i]
    L[i] = key
    print(L)
    quickSort(L, low, i-1)
    quickSort(L, j+1, high)
    return L

if __name__ == '__main__':
	li = [100,2,23,19,43,33,21,20,45,42,-9,-12]
	print('orginal:\r\n'+str(li))
	print('quick sort:\r\n'+str(quickSort(li,0,li.__len__()-1)))
