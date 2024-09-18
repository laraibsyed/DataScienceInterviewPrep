# defining the method to find the longest 
# word and the shortest word
def minMaxLengthWords(inp):
    length = len(inp) # Stores the total length of the input string inp.
    si = ei = 0 # These track the start and end positions of the words while looping through the string.
    min_length = length # Initialized to the total length of the input string. This will hold the length of the shortest word.
    min_start_index = max_length = max_start_index = 0
    
    # loop to find the length and stating index
    # of both longest and shortest words
    while ei <= length:
        if (ei < length) and (inp[ei] != " "): # The code checks whether the current character at inp[ei] is a space. If not, it increments the ei (end index) to keep moving forward to find the end of a word.
            ei += 1
        else: # This indicates that a word has been found between the indices si (start index) and ei (end index).
            curr_length = ei - si # Calculates the length of this word.
            
            # If the current word's length is smaller than the previously found minimum length, update min_length to the current word's length and set min_start_index to the start of this word.
            if curr_length < min_length:
                min_length = curr_length
                min_start_index = si
                
            # If the current word's length is greater than the previously found maximum length, update max_length to the current word's length and set max_start_index to the start of this word.
            if curr_length > max_length:
                max_length = curr_length
                max_start_index = si
            ei += 1
            si = ei # After processing the current word, the ei and si indices are both moved to the next position (after the space) to start looking for the next word.
            
    # extracting the shortest word using 
    # it's starting index and length     
    minWord = inp[min_start_index : 
                  min_start_index + min_length]
    
    # extracting the longest word using 
    # it's starting index and length     
    maxWord = inp[max_start_index : max_length]
    
    # printing the final result
    print("Minimum length word: ", minWord)
    print ("Maximum length word: ", maxWord)
    
# Driver Code

# Using this string to test our code
a = "GeeksforGeeks A Computer Science portal for Geeks"
minMaxLengthWords(a)