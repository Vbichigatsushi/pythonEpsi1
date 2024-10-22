

def several_zeros():
	l_zeros = []
	for i in range(10):
		l_zeros.append(0)
	return l_zeros

def several_zeros_custom(nb_zeros=10):
	l_zeros = []
	for i in range(nb_zeros):
		l_zeros.append(0)
	return l_zeros

def matrix(rows, cols):
	l_row = []
	for j in range(cols):
		l_row.append(0)
	l_matrix = []
	for i in range(rows):
		l_matrix.append(l_row)
	return l_matrix

class Matrix():
	def __init__(self, rows, cols):
		l_row = []
		for j in range(cols):
			l_row.append(0)
		self.__matrix = []
		for i in range(rows):
			self.__matrix.append(l_row)

	def __repr__(self):
		return str(self.__matrix)

	def get_value(self, row, col):
		return int(self.__matrix[row][col])

	def __eq__(self, other):
		return self.__matrix == other.__matrix

def my_sort(my_list: [int]) -> [int]:
	sorted_arr = arr.copy()
	n = len(sorted_arr)
	for i in range(n):
		for j in range(0, n-i-1):
			if sorted_arr[j] > sorted_arr[j+1]:
				sorted_arr[j], sorted_arr[j+1] = sorted_arr[j+1], sorted_arr[j]
    
	return sorted_arr

if __name__ == '__main__':
	print(several_zeros())

	print(several_zeros_custom())

	print(matrix(2, 3))

	testMat = Matrix(2, 3)
	testMat2 = Matrix(2, 3)
	print(testMat)
	print(testMat.get_value(1, 2))
	print(testMat == testMat2)

	arr = [64, 34, 25, 12, 22, 11, 90]
	sorted_arr = my_sort(arr)
	print("Tableau original:", arr)
	print("Tableau trié:", sorted_arr)
