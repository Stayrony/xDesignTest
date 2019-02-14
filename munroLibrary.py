import csv
from itertools import islice

d = []
munros = {"Munro Top":"TOP", "Munro":"MUN"}
sortKeys = {"height": "Height (m)", "name" : "Name", "Running No": "Running No"}

def openCSV(file):
	with open(file) as f:
		reader = csv.DictReader(f, delimiter=',') 
		for row in reader:
			if row['Running No'] != '' and row['Post 1997'] != '':
				d.append(row)
			

def checkCategory(category):
	if category == "MUN":
		return "Munro"
	else:
		return "Munro Top"

def stringToFloat(number):
	try:
		return float(number)
	except ValueError:
		return 0

def printResult(munros):
	#name, height in meters, hill category and grid reference 
	for munro in munros:
		print "Name: "+munro['Name'] + " | Height(m): " + munro['Height (m)'] + "m | Category: " + checkCategory(munro['Post 1997']) + " | Grid Reference: " + munro['Grid Ref'] + "\n"

def munroById(id):
	printResult([filter(lambda munro: munro['Running No'] == str(id), d)[0]])
		
def munroByName(name):
	printResult([filter(lambda munro: munro['Name'] == name, d)[0]])

def getMunros(limit=0, sortBy = "ASC", sortColumn = "Running No"):
	if needsSorting(sortBy, sortColumn):
		resultList = sortListBy(d, sortBy, sortColumn)
	else:
		resultList = d

	if limit != 0:
		resultList = limitResults(resultList, limit)

	printResult(resultList)

def munrosByCategory(category, limit = 0):
	resultList = filter(lambda munro: munro['Post 1997'] == munros[category], d)

	if limit != 0:
		resultList = limitResults(resultList, limit)

	printResult(resultList)

def limitResults(completeList, limit):
	filteredList = list(islice(completeList, limit))

	return filteredList

def castVal(dictVal):
	try:
		return float(dictVal)
	except:
		return dictVal

def sortListBy(unsortedList,sortType, sortColumn):
	l = [d for d in unsortedList if d[sortKeys[sortColumn]]]
	if sortType != "ASC":
		return sorted(l, key=lambda k: castVal(k[sortKeys[sortColumn]]), reverse = True)

	return sorted([d for d in l if d[sortKeys[sortColumn]]])


def needsSorting(sortBy, sortColumn):
	return sortBy != "ASC" or sortColumn != "Running No"

def munrosByMaxHeight(maxHeight, limit=0, sortBy = "ASC", sortColumn = "Running No"):

	if needsSorting(sortBy, sortColumn):
		resultList = sortListBy(d, sortBy, sortColumn)
		resultList = filter(lambda munro: stringToFloat(munro['Height (m)']) <= maxHeight and munro['Post 1997'] in munros.values(), resultList)
	else:
		resultList = filter(lambda munro: stringToFloat(munro['Height (m)']) <= maxHeight and munro['Post 1997'] in munros.values(), d)

	if limit != 0:
		resultList = limitResults(resultList, limit)

	printResult(resultList)

def munrosByMinHeight(minHeight, limit=0, sortBy = "ASC", sortColumn = "Running No"):
	if needsSorting(sortBy, sortColumn):
		resultList = sortListBy(d, sortBy, sortColumn)
		resultList = filter(lambda munro: stringToFloat(munro['Height (m)']) <= maxHeight and munro['Post 1997'] in munros.values(), resultList)
	else:
		resultList = filter(lambda munro: stringToFloat(munro['Height (m)']) >= minHeight and munro['Post 1997'] in munros.values(), d)

	if limit != 0:
		resultList = limitResults(resultList, limit)

	printResult(resultList)

def munrosBetweenHeights(minHeight, maxHeight, limit=0, sortBy = "ASC", sortColumn = "Running No"):

	if minHeight > maxHeight :
		raise ValueError('min height must not be less than max height')

	if needsSorting(sortBy, sortColumn):
		resultList = sortListBy(d, sortBy, sortColumn)
		resultList = filter(lambda munro: stringToFloat(munro['Height (m)']) <= maxHeight and munro['Post 1997'] in munros.values(), resultList)
	else:
		resultList = filter(lambda munro: stringToFloat(munro['Height (m)']) >= minHeight and stringToFloat(munro['Height (m)']) <= maxHeight and munro['Post 1997'] in munros.values(), d)

	if limit != 0:
		resultList = limitResults(resultList, limit)

	printResult(resultList)

def main():
	file = 'munro.csv'
	
	openCSV(file)
	#munroById(1)
	#munroByName("A' Bhuidheanach Bheag")
	#getMunros(10, "ASC", "name")
	#munrosByCategory("Munro", 5)
	#munrosByMaxHeight(1200, 10, "ASC", "name")
	#munrosByMinHeight(1000)
	#munrosBetweenHeights(1000, 1005)
	#munrosBetweenHeights(1000, 1005, 10, "ASC", "name")
	#munrosBetweenHeights(1008, 1005)
 
 
if __name__ == '__main__':
	main()