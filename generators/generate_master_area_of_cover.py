from faker import Factory
from helpers import decor

def gen_master_areas(rows):
    fake = Factory.create()

    file = open('csv/Master-area-of-cover.csv', 'w+')

    content = 'Worldwide,Worldwide excluding USA,South East Asia,Europe\r\n'

    print file.read()

    for _ in range(0,rows):
        next_row = decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + '\r\n'
        content = content + next_row

    file.write(content)