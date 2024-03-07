import matplotlib.pyplot as plt

def graphSnowfall(t):
    # Initialize a list, i initialized it to 6 for this specfic file, this is a bad practice that I will come back and fix at a later date
    snowfall_ranges = [0] * 6

    # Open the file
    with open(t, 'r') as file:
        # for loop to iterate through each line in file
        for line in file:
            # Convert to an integer and remove whitespaces
            snowfall = int(line.strip())
            # Iterate through the snowfall_ranges list
            for i in range(len(snowfall_ranges)):
                # Check if they fall within a range
                if snowfall <= (i + 1) * 10:
                    # If it does increment the corresponding count
                    snowfall_ranges[i] += 1
                    # then break
                    break
            else:
                # If the value is big, then incrememnnt  the count for the last range
                snowfall_ranges[-1] += 1

    # creating snowfall ranges for the x acis
    ranges = ['0-10cm', '11-20cm', '21-30cm', '31-40cm', '41-50cm', '51cm+']

    # Create a bar chart using matplotlib
    plt.bar(ranges, snowfall_ranges, color='skyblue')
    plt.xlabel('Snowfall Range')
    plt.ylabel('Occurrences')
    plt.title('Snowfall Accumulation')
    plt.show()

graphSnowfall('snowfall.txt')
