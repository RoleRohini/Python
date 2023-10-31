
arr = []
print("Enter 10 Elements: ")
for i in range(10):
  arr.append(int(input()))

for i in range(1, 10):
  elem = arr[i]
  if elem<arr[i-1]:
    for j in range(i+1):
      if elem<arr[j]:
        index = j
        for k in range(i, j, -1):
          arr[k] = arr[k-1]
        break
  else:
    continue
  arr[index] = elem

print(arr)