from faker import Factory
from helpers import decor

def gen_sub_zones(rows):
    fake = Factory.create()

    file = open('csv/Sub-zones-of-cover.csv', 'w+')

    content = "Worldwide,Worldwide excluding USA,\"Worldwide exluding USA, Canada\",\"Worldwide exluding USA, Canada, China, HK, Macau, Japan, Singapore, Taiwan\",South East Asia 1,South East Asia 2,South East Asia 3,Europe 1\r\n"

    print file.read()

    for _ in range(0, rows):
        next_row = decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(
            fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(
            fake.country()) + ',' + decor(fake.country()) + '\r\n'
        content = content + next_row

    file.write(content)
