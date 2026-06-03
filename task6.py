# Create empty lists for Matrix A and Matrix B
A = []
B = []

# Take input for Matrix A
print("Enter elements of Matrix A")

# Loop through rows
for i in range(2):
    
    # Create an empty row
    row = []
    
    # Loop through columns
    for j in range(2):
        
        # Take input from user
        num = int(input(f"Enter element [{i}][{j}]: "))
        
        # Add the number to the row
        row.append(num)
    
    # Add the completed row to Matrix A
    A.append(row)

# Take input for Matrix B
print("Enter elements of Matrix B")

# Loop through rows
for i in range(2):
    
    # Create an empty row
    row = []
    
    # Loop through columns
    for j in range(2):
        
        # Take input from user
        num = int(input(f"Enter element [{i}][{j}]: "))
        
        # Add the number to the row
        row.append(num)
    
    # Add the completed row to Matrix B
    B.append(row)

# Create a result matrix filled with zeros
result = [[0, 0],
          [0, 0]]

# Perform matrix addition
for i in range(2):
    for j in range(2):
        
        # Add corresponding elements
        result[i][j] = A[i][j] + B[i][j]

# Display the result matrix
print("Result Matrix:")

# Print each row separately
for row in result:
    print(row)