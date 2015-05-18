#
#the sort named bubble
#
def bubble(listA):
	for t in range(0, listA.__len__()-1):
		for i in range(0, listA.__len__()-t):
			if i != listA.__len__()-1 and listA[i]>listA[i+1]:
				temp = listA[i]
				listA[i] = listA[i+1]
				listA[i+1] = temp
			else:
				continue
		print(listA)
	return listA
if __name__=='__main__':
	listA = [1,100,30,43,21,10,23,11,21,16,23]
	print('orginal:'+str(listA))
	print('rest:'+str(bubble(listA)))
	pass
