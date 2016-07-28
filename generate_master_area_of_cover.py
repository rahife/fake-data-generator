from faker import Factory
fake = Factory.create()

file = open('Master-area-of-cover.csv', 'w+')

text = "Worldwide,Worldwide excluding USA,South East Asia,Europe"


print file.read()

for _ in range(0,10):
    print fake.country() + ',' + fake.country() + ',' + fake.country() + ',' + fake.country()