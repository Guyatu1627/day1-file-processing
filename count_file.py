# Define the file name
filename = 'sample.txt'


# Initialize counters
line_count = 0
word_count = 0
char_count = 0

# Read the file
with open(filename, 'r') as file:
    for line in file:
        line_count += 1 # Count lines
        words = line.split() # Split the line into words
        word_count += len(words) # Count words
        char_count += len(line) # Count characters including whitespace

# Print the results
print("Results:")
print(f"Number of lines: {line_count}")
print(f"Number of words: {word_count}")
print(f"Number of characters: {char_count}")