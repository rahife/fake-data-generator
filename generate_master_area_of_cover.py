from faker import Factory

fake = Factory.create()

file = open('csv/Master-area-of-cover.csv', 'w+')

content = 'Worldwide,Worldwide excluding USA,South East Asia,Europe\r\n'

print file.read()

# hay que poner esta funcion en helpers/ ################
def decor(field):
    return ('"' + field + '"') if "," in field else field
#########################################################

for _ in range(0,10):
    next_row = decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + '\r\n'
    content = content + next_row

file.write(content)