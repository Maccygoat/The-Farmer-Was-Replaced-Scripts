def reset_field_to_grass():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest() == True:
				if get_ground_type() == Grounds.Soil:
					harvest()
					till()
				if get_ground_type() != Grounds.Soil:
					harvest()
			elif can_harvest() == False and get_ground_type() == Grounds.Soil:
				till()
			else:
				harvest()
			move(North)
		move(East)
	return_home()
reset_field_to_grass()
