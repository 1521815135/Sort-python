#choise sort:every time choise the min or max value to a sorted list

def choise(li):
	fli = []
	length = li.__len__()
	print(length)
	for i in range(0,length-1):
		print('i:'+str(i))
		print('len:'+str(length))
		temp = li[i]
		for j in range(i,length-1):
			if temp > li[j]:
				temp = li[j]
				print(li)
			else:
				pass
		li.remove(temp)
		length = length -1
		fli.insert(fli.__len__()+1,temp)
		i = 0
	return fli
	pass

if __name__ == '__main__':
	li = [-1,20,11,1,3,8,56,1000,43,21,-56,43,-9]
	print('orginal:\n\r'+str(li))
	print('choise:'+str(choise(li)))
