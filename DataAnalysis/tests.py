from django.test import TestCase

# Create your tests here.
sheetnames = ['合纵', '龙一', '蓉锦', '华鼎', '聚创', '粤通']
dataall = []
context = {"test1": 1}
for sheetname in sheetnames:
    dataall.append(sheetname)
print(dataall)