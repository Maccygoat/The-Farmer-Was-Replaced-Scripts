def buy_pumpkin():
	if num_items(Items.Pumpkin_Seed) == 0:
		worldsize = get_world_size() * get_world_size()
		trade(Items.Pumpkin_Seed, worldsize)
def plant_pumpkin():
	if can_harvest() == True:
		if get_ground_type() != Grounds.Soil and get_entity_type() != Entities.Pumpkin:
			harvest()
			till()
			buy_pumpkin()
			plant(Entities.Pumpkin)
			water_plants()
		elif get_ground_type() == Grounds.Soil and get_entity_type() != Entities.Pumpkin:
			harvest()
			buy_pumpkin()
			plant(Entities.Pumpkin)
			water_plants()
		else:
			water_plants()
	elif can_harvest() != True:
		if get_entity_type() == None:
			buy_pumpkin()
			plant(Entities.Pumpkin)
			water_plants()
		else:
			water_plants()


def get_pumpkin_size_and_harvest():
	grown_pumpkin_plots = 0
	total_plots = get_world_size() * get_world_size()
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_entity_type() == Entities.Pumpkin and can_harvest() == True:
				move(North)
				grown_pumpkin_plots = grown_pumpkin_plots + 1
			else:
				plant_pumpkin()
		move(East)
		if grown_pumpkin_plots == total_plots:
			return_home()
			harvest()
			
while True:
	get_pumpkin_size_and_harvest()
	
