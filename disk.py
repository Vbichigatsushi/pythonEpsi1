class Disk():
	def __init__(self, total, used):
		self.__total = total
		self.__used = used
	
	@property
	def free(self):
		return (self.__total - self.__used)

	def __repr__(self):
		return f'Disk[total: {self.__total} Gb, used: {self.__used} Gb]'

	def __lt__(self, other):
		if not isinstance(other, Disk):
			return NotImplemented
		return (self.__used / self.__total) < (other.__used / other.__total)

if __name__ == '__main__':
	disk = Disk(10, 2)
	print(disk) # Disk[total: 10 Gb, used: 2 Gb]
	print(disk.free)
	
	disks = [Disk(100, 40), Disk(200, 100), Disk(50, 25)]
	print(sorted(disks))