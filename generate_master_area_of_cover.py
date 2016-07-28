from faker import Factory

fake = Factory.create()

file = open('Master-area-of-cover.csv', 'w+')

text = 'Worldwide,Worldwide excluding USA,South East Asia,Europe\r\n'

print file.read()

def decor(field):
    return ('"' + field + '"') if "," in field else field

for _ in range(0,10):
    next_row = decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + '\r\n'
    text = text + next_row

file.write(text)