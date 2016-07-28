from faker import Factory

fake = Factory.create()

file = open('csv/Country-of-residence-plan-availability.csv', 'w+')

text = "Available Worldwide ,Available Worldwide excluding USA,\"Available Worldwide exluding USA, Canada\",\"Available Worldwide exluding USA, Canada, China, Hong Kong, Macau, Japan, Singapore, Taiwan\",Available South East Asia 1,Available South East Asia 2,Available South East Asia 3,Available Europe 1\r\n"

print file.read()

# hay que poner esta funcion en helpers/ ################
def decor(field):
    return ('"' + field + '"') if "," in field else field
#########################################################

for _ in range(0,10):
    next_row = decor("picha, ole") + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + '\r\n'
    text = text + next_row

file.write(text)