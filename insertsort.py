# insert sort:two list
# one list is sorted and another is unsort
# get one val from second list and compare with first list from the first
# val. if the val2 bigger smaller than val1 ,val1...valn 
def compare(val,li2):
	for i in range(0,li2.__len__()):
		if val < li2[i]:
			li2.insert(i,val)
			break
		else:
			continue		
	return li2

def insert(li):
	fli = [li[0]] # the base sorted list
	for i in range(1,li.__len__()):
		fli = compare(li[i],fli)
		print(fli)
	return fli

if __name__ == '__main__':
	li = [100,2,12,32,-9,-32,21,-45,45,44,32,330,450,-450]
	print('insert orginal:\n\r'+str(li))
	print('insert sorted:\r\n'+str(insert(li)))
	pass
