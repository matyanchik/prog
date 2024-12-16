my_family = ['dad', 'mom', 'me']
my_family_height = [
    ['dad', 180],
    ['mom', 170],
    ['me', 190]
]
print('Рост отца -', my_family_height[0][1], 'см')
r = 0
for i in my_family_height:
    r += i[1]
print('Общий рост моей семьи -', r, 'см')