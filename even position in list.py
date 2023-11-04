
nums = []
print("Enter 10 Numbers: ")
for i in range(10):
  nums.insert(i, int(input()))

print("\nElements at Even Positions: ")
for i in range(10):
  if i%2==0:
    print(nums[i])