my_list=["10", "20", "30", "40", ]
my_list.insert( 1, "15")  # Insert "15" at the second position
my_list.extend( ["50", "60", "70"] )  # Add "50", "60", "70" to the end of the list
my_list.remove("70")  # Remove the last element of the list
my_list = list(map(int, my_list))  # Convert all elements to integers
my_list.sort()  # Arrange the list in ascending numerical order

print(my_list [3])  # Print the fourth element of the list
