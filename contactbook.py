import csv
import os

current_dir=os.path.dirname(__file__)
filename="aniket.csv"
fields=['Name','phone no','email','address']
info=[]

with open(os.path.join(current_dir,filename),'w')as csvfile:
    csvfile1=csv.writer(csvfile)
    csvfile1.writerow(fields)
    n=int(input("Enter the no of people required:"))
    for i in range(n):
        info.append([])
    for i in range(n):
        for j in range(0,4):
            info[i].append(j)
            info[i][j]=0
            print("Row",i+1,"col",j+1)
            info[i][j]=input("Enter the name,phone_no,email,address")
    csvfile1.writerows(info)
with open(os.path.join(current_dir,filename),'r')as csvfile2:
    csvfile3=csv.reader(csvfile2)
    search=input("Enter any person name,person phone_no,email id ,address you want to search")
    for a in csvfile3:
        for i in a:
            if i==search:
                print(a)
