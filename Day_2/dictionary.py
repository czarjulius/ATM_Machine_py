content_ratings = {'4+':4433, '9+': 987, '12+': 1155, '17+': 622}
print(content_ratings)

over_9 = content_ratings['9+']
over_17 = content_ratings['17+']

print(over_9)
print(over_17)

empty = {}
empty_list = ['zero']
empty['a'] = 'python'
empty_list.append('one')
empty_list.insert(0, 3)

print(empty)
print(empty_list)

for key in content_ratings:
    print(key, content_ratings[key])