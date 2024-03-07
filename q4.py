def stats_decorator(func):
    # Define a wrapper function that will be returned
    def wrapper(arggs):  # Takes a single argument
        # Call the original function with arggs
        result = func(arggs)
        
        # Retrieve statistics from the result
        # Split the result string into a list of numbers
        numbers = result.split()
        # Convert each number from string to integer
        numbers = [int(num) for num in numbers]
        # Calculate the count of numbers
        count = len(numbers)
        # Calculate the average of numbers
        average = sum(numbers) / count
        # Find the maximum number
        maximum = max(numbers)
        
        # Print out the statistics
        print("Numbers read:", numbers)
        print("Count of numbers read:", count)
        print("Average of numbers:", average)
        print("Maximum of numbers:", maximum)
        
        # Return the result
        return result
    
    # Return the wrapper
    return wrapper

# Decorate with stats_decorator
@stats_decorator
def printStats(t):
    # Open the file
    with open(t, 'r') as file:
        # Read the first line
        return file.readline().strip()

printStats("snowfall.txt")
