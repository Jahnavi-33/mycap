# Python program to print positive Numbers in given range 
  
start = int(input("Enter the start of range: ")) 
end = int(input("Enter the end of range: ")) 
  
# iterating each number in list 
for num in range(start, end + 1): 
      
    # checking condition 
    if num >= 0: 
       print(num, end = " ")
      
      

 # Python program to print positive Numbers in a List 
  

numberList = []
n = int(input("Enter the list size : "))

print("\n")
for i in range(0, n):
    print("Enter number at range", i, ":")
    item = int(input())
    numberList.append(item)
print("User List is ", numberList)
for num in numberList:
    if num >=0:
        print(num, end= " ")




       
