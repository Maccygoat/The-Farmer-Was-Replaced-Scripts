def get_hay():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest() == True:
				if get_ground_type() != Grounds.Soil:
					harvest()
				elif get_ground_type() == Grounds.Soil:
					harvest()
					till()
			elif can_harvest() == False and get_ground_type() == Grounds.Soil:
				till()
			else:
				harvest()
			move(North)
		move(East)
while True:
	get_hay()
