def getPrimeNumbers(n):
    # Initialize an empty list to store prime numbers
    prime_numbers = []
    
    # Iterate through numbers from 2 to n inclusivly
    for num in range(2, n + 1): 
        
        # Assume num is prime will check if its not below
        is_prime = True
        sqrt_num = int(num ** 0.5) + 1  # Calculate the square root of num
        # Check if num is divisible by any number from 2 to its square root inclusivly
        for i in range(2, sqrt_num):
            # If num is divisible by any number other than 1 and itself, it's not prime, so set is_prime to False and exit the loop
            if num % i == 0:
                is_prime = False
                break
        
        # If is_prime is still True after the inner loop num is a prime number, so append it to the prime_numbers list
        if is_prime:
            prime_numbers.append(num)
    
    # Print the prime numbers
    print("the prime numbers up to", n, "are", prime_numbers)

getPrimeNumbers(5)
