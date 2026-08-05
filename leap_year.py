from ast import Or
year=2020
if(year%100!=0 and  year%400==0)or(year%4==0):
  print("leap year",year)
else:
  print("No leap year")
