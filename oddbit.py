def odd_number(arr):
    res = 0
    
    for element in arr:
        res = res ^ element 
    return res
    
arr = []

n = int(input("Enter a range from 0 to : "))

while(n):
    num = int(input("Enter the numbers."))
    arr.append(num)
    n = n - 1
    
print("The odd number is: ",odd_number(arr))
