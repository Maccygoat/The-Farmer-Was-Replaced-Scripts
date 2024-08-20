# This is for a plot size of 4x4

def get_wood():	
	coordinates = []
	for a in range(get_world_size()):
		for b in range(get_world_size()):
			if (a + b) % 2 == 1:
				coordinates.append((a, b))
    quick_print(coordinates)
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest() == True:
				harvest()
				if (get_pos_x(), get_pos_y()) in coordinates: 
					plant(Entities.Tree)
					water_plants()
				else:
					plant(Entities.Bush)
					water_plants()
			elif can_harvest() == False:
				water_plants()
			move(North)
		move(East)

while True:
	get_wood()
