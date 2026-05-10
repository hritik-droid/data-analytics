import math

length = 12
width = 10
tiles_per_box = 12

room_area = length * width
tiles_needed = room_area * 1.10
boxes_needed = math.ceil(tiles_needed / tiles_per_box)

print("Room area is " + str(room_area) + " square feet")
print("Tiles needed with 10% extra is " + format(tiles_needed, ".0f"))
print("You need to buy " + str(boxes_needed) + " boxes of tiles")