import colorgram

extracted_colors = colorgram.extract('image.jpg',20)
#print(colors)
colors = []
for col in extracted_colors:
    print(col.rgb)
    colors.append((col.rgb.r,col.rgb.g,col.rgb.b))

print(colors)

# Output after dropping the first white color shades
# colors = [(197, 166, 114), (64, 102, 124), (147, 166, 182), (14, 41, 59), (223, 205, 125), (142, 85, 57), (130, 77, 93), (183, 152, 165), (147, 174, 156), (71, 108, 89), (174, 148, 57), (17, 47, 38), (177, 99, 116), (123, 39, 30), (25, 88, 66), (72, 37, 26)]
