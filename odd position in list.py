
arr = []
print("Enter 10 Numbers: ")
for i in range(10):
  arr.insert(i, int(input()))

print("\nNumbers at Odd Positions: ")
for i in range(10):
  if i%2!=0:
    print(arr[i])