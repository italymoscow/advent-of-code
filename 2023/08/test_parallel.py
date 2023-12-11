import multiprocessing

def my_function(x):
    # Perform some computation
    result = x ** 2
    return result

if __name__ == "__main__":
    # Create a Pool object with the desired number of processes
    with multiprocessing.Pool() as pool:
        # Use the map() method to apply the function to a sequence of inputs
        inputs = [1, 2, 3, 4, 5]
        results = pool.map(my_function, inputs)
    
    # Print the results
    print(results)