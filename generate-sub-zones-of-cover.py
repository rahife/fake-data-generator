from faker import Factory

fake = Factory.create()

file = open('csv/Sub-zones-of-cover.csv', 'w+')

content = "Worldwide,Worldwide excluding USA,\"Worldwide exluding USA, Canada\",\"Worldwide exluding USA, Canada, China, HK, Macau, Japan, Singapore, Taiwan\",South East Asia 1,South East Asia 2,South East Asia 3,Europe 1\r\n"

print file.read()

# hay que poner esta funcion en helpers/ ################
def decor(field):
    return ('"' + field + '"') if "," in field else field
#########################################################

for _ in range(0,10):
    next_row = decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + '\r\n'
    content = content + next_row

file.write(content)