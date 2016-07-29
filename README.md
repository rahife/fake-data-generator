#FAKE DATA GENERATOR

Simple scripts to generate fake CSV files. It can be modified to generate many kinds of fake data files. For more info, check fake-factory online help.

It's using: 

- Python 2.7.10
- pip 8.1.2
- fake-factory 0.5.9

##INSTALATION

```
git clone git@github.com:rahife/fake-data-generator.git
cd fake-data-generator
pip install -r requirements.txt
python generate_fake_data.py #if you have problems try with sudo
```

##FILES GENERATED

- Master-area-of-cover.csv
- Sub-zones-of-cover.csv
- Country-of-residence-plan-availability.csv
- Company-premiums-and-benefits.csv

They are generated in the csv folder.

You can modify the number of rows you want in each file. Just edit generate_fake_data.py

##CSV VALIDATION

http://csvlint.io
