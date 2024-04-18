matrix = [
    [3, 8, 9, 10, 0], 
    [5, 7, 8, 9, 2],
    [1, 4, 13, 14, 15],
    [2, 13, 18, 6, 20],
    [11, 22, 15, 8, 9]
]

def process_matrix(matrix):
    rows = len(matrix) # we will know the amount of rows
    columns = len(matrix[0]) # we will get the amount of columns because we already know the rows
    result = [] # initialize the processed matrix with a neutral value

    for cajita in range(rows): 
        new_row = [] 
        for b in range(columns): # loop to iterate through each column of the row (this iterates over the elements) of the sublists
            sum_ = matrix[cajita][b] # sum the value of the element in position (cajita, b) for the average calculation
            elements = 1 # element counter started at 1 to include the current element in the average
            
            if b < columns - 1: # we check if there is a neighbor to the right.
                sum_ += matrix[cajita][b+1] # add to the initial value the value of its right.
                elements += 1 # add the current element plus its neighbor to the right.
            
            if b > 0: # we check if there is a neighbor to the left. (is the current position greater than 0?, yes)
                sum_ += matrix[cajita][b-1] # add to the initial value the value of its left.
                elements += 1 # add the current element plus its neighbor to the left.
            
            if cajita > 0: # we check if there is a neighbor above. (if it is greater than zero, it has a sublist above)
                sum_ += matrix[cajita-1][b] # sum the element of the upper sublist with the iterating element (j)
                elements += 1 # add the current element plus its neighbor above.
            
            if cajita < rows - 1: # we check if there is a neighbor below. (if i is less than the length of rows of matrix)
                sum_ += matrix[cajita+1][b] # sum the current element plus its neighbor below.
                elements += 1 # add the current element plus its neighbor below.

            average = sum_ / elements # the average is calculated by dividing the sums by the value of elements
            new_row.append(average) # add to new_row the new average values to the sublists
        result.append(new_row) # adds the sublists to the processed matrix
            
    return result # the processed matrix is returned

print(process_matrix(matrix))
