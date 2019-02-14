# Munro Library Challenge

### Python Library

Provides information about munros and munro tops within Scotland.

Functions include:

- Filtering of search by hill category (i.e. Munro, Munro Top or either). If this information is
not provided by the user it should default to either. This should use the “post 1997”
column and if it is blank the hill should be always excluded from results.
- The ability to sort the results by height in meters and alphabetically by name. For both
options it should be possibly to specify if this should be done in ascending or descending
order.
- The ability to limit the total number of results returned, e.g. only show the top 10
- The ability to specify a minimum height in meters
- The ability to specify a maximum height in meters
- Queries may include any combination of the above features and none are mandatory.
- Suitable error handling for invalid queries (e.g. when the max height is less than the
minimum height)

### Usage

```python

	#Open de CSV file
	openCSV(file)

	#Get munro by id
	munroById(1)

	#Get munro by name
	munroByName("Druim Shionnach West Top")

	#Get all munros
	getMunros()

	#Get all munros, you can specify how many results, order by name or height in ascending or descending order
	getMunros(10, "ASC", "name")

	#Munros by category (Munro or Munro Top)
	munrosByCategory("Munro", 5)

	#Munros by maximum height
	munrosByMaxHeight(1200, 10, "ASC", "name")

	#Munros by minimum height
	munrosByMinHeight(1000)

	#Munros between heights
	munrosBetweenHeights(1000, 1005)

	#You can also specify a limit, order column and ascending or descending
	munrosBetweenHeights(1000, 1005, 10, "ASC", "name")

	#This call will produce an error since the minimum height is smaller than the maximum height
	munrosBetweenHeights(1008, 1005)

	# If you want to specify the ordering by ascending or descending and sort column the limit must be set to zero
	munrosByMaxHeight(1200, 0, "ASC", "name")

	#Default sorting is set to ASC and default sorting column is set to the "Running No"

```


## Author

✨✨mzellhuber✨✨ [https://github.com/mzellhuber](https://github.com/mzellhuber)