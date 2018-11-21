"""
Week2lab2
Asoo Azad
28/09/18
"""

length_Of_Yard = 30
width_Of_Yard = 20
length_Of_House = 15
width_Of_House = 10
cuttingrate = 2

yard_area = (length_Of_Yard*width_Of_Yard)
print("The yard area is")
print(yard_area)

house_area = (length_Of_House*width_Of_House)
print("The house area is")
print(house_area)

cuttingpoint = (yard_area - house_area)

timecuttingpoint = (cuttingpoint/cuttingrate)
print("Time to cut")
timecuttinginseconds = (timecuttingpoint/ 60)
print(timecuttinginseconds)
