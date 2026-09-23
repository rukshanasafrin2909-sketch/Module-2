string = input("Enter your string")
reversed_string = ''
for i in string:
  reversed_string = i + reversed_string
print("\nThe original string ", string)
print("\nThe reversed string ", reversed_string)