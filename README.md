#FAKE DATA GENERATOR

Simple scripts to generate fake CSV files using fake-factory. It can be modified to generate many kinds of fake data files. For more info, check:

https://pypi.python.org/pypi/fake-factory

##INSTALATION

Environment: 

- Ubuntu 14.04
- Python 2.7.3
- pip 8.1.2

Steps:

```
git clone git@github.com:rahife/fake-data-generator.git
cd fake-data-generator
pip install -r requirements.txt
python generate_fake_data.py #if you have problems try with sudo
```

##FILES GENERATED

These files will be generated in the csv folder:

- Master-area-of-cover.csv
- Sub-zones-of-cover.csv
- Country-of-residence-plan-availability.csv
- Company-premiums-and-benefits.csv

You can modify the number of rows you want in each file editing generate_fake_data.py

##CSV VALIDATION

http://csvlint.io
