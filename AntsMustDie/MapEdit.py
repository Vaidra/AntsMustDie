class MapEdit(object):
	"""description of class"""

	def __init__(self):
		self.case=[]

	def __init__(self, _width, _height):
		self.case	= []		# Tableau contenant les CASES
		self.width	= _width
		self.height = _height
		
		self.case = [[0] * self.height for _ in range(self.width)]
		for p in range(self.width):
			for q in range(self.height):
				self.case[p][q] = 0

	#def readMapFile():
	#   file=open("map.txt","r")


	def createMap(self,width,height):
		self.case = [[0] * colonnes for _ in range(lignes)]
		for p in range(width):
			for q in range(height):
				self.case[p][q] = 0

	def setCaseType(self, _width, _height, _case_type):
		print(_width)
		print(_height)
		self.case[_width][_height] = _case_type

	def getCaseType(self, _width, _height):
		return self.case[_width][_height]

	def save(self,_fileName):
		file = open(_fileName, "w")
		file.write(str(self.case))
		file.close()

	def load(self,_fileName):
		file = open(_fileName, "r")
		case=file.read().strip().split("], [")
		case.replace(" ","")
		file.close()
		self.width=20
		self.height=20
		print(case)

