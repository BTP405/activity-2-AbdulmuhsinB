def wordCount(t):
    word_dict = {}  # creates a dictionar for storing words
    line_num = 1  # Initialize line number to 1
    
    # Open the file
    with open(t, 'r') as file:
        # for loop to iterate through each line in file
        for line in file:
            # Split the line up into words
            wordsInline = line.strip().split()
            
            # Iterate through each word in the line
            for word in wordsInline:
                # If the word is already in the dictionary, append the line_num
                if word in word_dict:
                    word_dict[word].append(line_num)
                # it its not then create a new key-value in the word_dict
                else:
                    word_dict[word] = [line_num]
            
            # incremment up the line_num
            line_num += 1
    
    #print the values in the word_dict
    print(word_dict)

wordCount('snowfall.txt')
