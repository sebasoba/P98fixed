def swapFileData();

swapFile=input("enter the swap file:-")
file1 = input("enter files name:- ") 
file2 = input("enter files name:- ")

file=open(fileName, 'r')



with open(file1, 'r') as a:
data_a = a.read

with open(file1, 'w') as a:
a.write(data_b)