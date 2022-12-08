# Python3 program to find
# the missing Number
# getMissingNo takes list as argument
def getMissingNo(a, n):
	n_elements_sum=n*(n+1)//2
	return n_elements_sum-sum(a)


# Driver program to test above function
if __name__=='__main__':

	a = [1,2,4,5]
#     # creating an empty list
# lst = []

# # number of elements as input
# n = int(input("Enter number of elements : "))

# # iterating till the range
# for i in range(0, n):
# 	ele = int(input())

# 	lst.append(ele) # adding the element
	
# print(lst)

	n = len(a)+1
	miss = getMissingNo(a, n)
	print(miss)
