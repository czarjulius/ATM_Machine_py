ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']

freq_result = {}

for value in ratings:
    if value in freq_result:
        freq_result[value] += 1
    else:
        freq_result[value] = 1
print(freq_result)