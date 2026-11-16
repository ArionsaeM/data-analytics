#Arionsae McCutcheon

''''5. You are going to tile a room whose dimensions are length by width feet. There are 
twelve tiles per box, each 1 foot by 1 foot. How many boxes of tiles do you need? You 
can only buy full boxes, not a partial box. 
You also want to buy at least 10% more tiles than you need in order to handle chips, 
breakage, and mess-ups. How many total boxes will you buy? 
Code the script in a file named tiles.py '''

length = float(input('Enter the length of the room in feet:')) #ex: 10
width = float(input('Enter the width of the room in feet:')) #ex: 12
import math
dimension = length * width

dimension_10p = dimension * 1.10

boxes_needed = math.ceil(dimension_10p / 12) 

print (f'You will need {boxes_needed} boxes ')