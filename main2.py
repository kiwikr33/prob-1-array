arr = [1,2,3,4,5]

print("Original list:", arr)

n = int(input("How many positions to rotate left?"))

n = n % len(arr)

new_arr = arr[n:] + arr[:n]

print("Rotated list:", new_arr)