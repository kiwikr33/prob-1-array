n= int(input("Enter list size:"))

arr = list(range(1, n + 1))
reverse_arr = []

for i in range(n - 1, -1,-1):
    reverse_arr.append(arr[i])

print("Original list:", arr)
print("Reversed list:", reverse_arr)