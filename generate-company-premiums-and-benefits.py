from faker import Factory

fake = Factory.create()

file = open('csv/Company-premiums-and-benefits.csv', 'w+')

text = "Plan_title,Plan_Name,ID,Company,Area_of_cover,Age,Currency,Annual_premium,Excess,Maximum_cover ,Maximum_cover_periodicity,Excess_periodicity,Outpatient_Cover_Maximum,Outpatient_cover_periodicity,Outpatient_cover,Outpatient_cover_information,Dental_cover_Maximum,Dental_cover_periodicity,Dental_cover,Dental_cover_information,Maternity_cover_maximum,Maternity_cover_periodicity,Maternity_cover,Maternity_cover_information,Optical_cover_maximum,Optical_cover_periodicity,Optical_cover,Optical_cover_information,Country_of_residence_plan_availability,Other_highlights,Only_Expat_insurance,Logo,Benefits_schedule_pdf,General_conditions_pdf,Application_form_pdf,Co_branding,Co_branding_link\r\n"

print file.read()

# hay que poner esta funcion en helpers/ ################
def decor(field):
    return ('"' + field + '"') if "," in field else field
#########################################################

for _ in range(0,10):
    next_row = decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + \
               decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + \
               decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + \
               decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + \
               decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + \
               decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + \
               decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + \
               decor(fake.country()) + ',' + decor(fake.country()) + ',' + decor(fake.country()) + ',' + '\r\n'
    text = text + next_row

file.write(text)