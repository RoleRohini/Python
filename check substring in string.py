
print("Enter the String: ", end="")
MyStr = input()

print("\nEnter the Substring: ", end="")
MySubStr = input()

if MySubStr in MyStr:
    print("\nYes,\nThe substring is available in the string.")
else:
    print("\nNo,\nThe substring is not available in the string.")