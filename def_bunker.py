def is_even(n):
	return n % 2 == 0

def return_home():
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() > 0:
		move(South)
			
def check_inv_and_plant_carrots():
	if num_items(Items.Carrot_Seed) == 0:
		trade(Items.Carrot_Seed, 10)
		plant(Entities.Carrots)
		water_plants()
	else:
		plant(Entities.Carrots)
		water_plants()
		

def water_plants():
	if get_water() < 0.25:
		use_item(Items.Water_Tank)
