def plant_carrots():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest() == True:
				harvest()
				if get_ground_type() != Grounds.Soil:
					till()
					check_inv_and_plant_carrots()
				else:
					check_inv_and_plant_carrots()
			elif get_entity_type() == None:
				check_inv_and_plant_carrots()
			elif can_harvest() == False:
				water_plants()
			move(North)
		move(East)
while True:
	plant_carrots()
