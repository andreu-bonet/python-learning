def longest_common_subsequence(string_1, string_2):
    # Step 1: Initialize the grid
    grid = [[0 for _ in range(len(string_1) + 1)] for _ in range(len(string_2) + 1)]

    # Step 2: Fill the grid based on LCS logic
    for row in range(1, len(string_2) + 1):
        for col in range(1, len(string_1) + 1):
            if string_1[col - 1] == string_2[row - 1]:
                grid[row][col] = grid[row - 1][col - 1] + 1
            else:
                grid[row][col] = max(grid[row - 1][col], grid[row][col - 1])

    # Step 3: Backtrack to find the LCS
    result = []
    row, col = len(string_2), len(string_1)
    while row > 0 and col > 0:
        if string_1[col - 1] == string_2[row - 1]:
            result.append(string_1[col - 1])
            row -= 1
            col -= 1
        elif grid[row - 1][col] > grid[row][col - 1]:
            row -= 1
        else:
            col -= 1
    
    # Step 4: Reverse the result list to get the correct LCS
    result.reverse()
    return "".join(result)

# Test the function
s1 = 'BABAAA'
s2 = 'AAAAAB'
print("Longest Common Subsequence: ", longest_common_subsequence(s1, s2))