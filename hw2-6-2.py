# Author: CRS 9/26/21
text1 = input("Please enter a radius ")
text2 = input("Please enter a height ")
radius = int(text1)
height = int(text2)
surfaceArea = (2 * 3.14 * radius * height) + (2 * 3.14 * (radius ** 2))
volume = 3.14 * (radius ** 2) * height
print(surfaceArea)
print(volume)
