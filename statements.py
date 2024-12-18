inevitabilities = ['cold', 'hunger', 'sickness', 'deprivation', 'death']
for thing in inevitabilities:
    print('You are doomed to experience %s.' % thing)

fates = {
    'health': 'disease',
    'satiety': 'famine',
    'comfort': 'cruelty'
}

for a, b in fates.items():
    print('You want %s, but you will know %s.' % (a, b))


