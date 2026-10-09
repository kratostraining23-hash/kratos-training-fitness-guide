def calories_burned(minutes, intensity):
	"""Calculate calories burned.

	>>> calories_burned(30, 5)
	150
	>>> calories_burned(10, 2)
	20
	"""
	return minutes * intensity

import doctest
doctest.testmod()
