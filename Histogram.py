import numpy as np
import matplotlib.pyplot as plt

def plot_normal_distribution_samples(N, mean=0, std=1):
    """
    Generates N samples from a normal distribution and plots them on a histogram.
    
    Parameters:
    N (int): Number of samples to generate.
    mean (float): Mean of the normal distribution (default is 0).
    std (float): Standard deviation of the normal distribution (default is 1).
    """
    # Generate N samples from a normal distribution with given mean and standard deviation
    samples = np.random.normal(loc=mean, scale=std, size=N) # generate random samples from a normal (Gaussian) distribution.
    
    # Plot the histogram
    plt.hist(samples, bins=50, edgecolor='black', density=True)  # Set density=True to normalize the histogram
    plt.title(f'Histogram of {N} samples from N({mean}, {std}^2)')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

# Example usage:
plot_normal_distribution_samples(1000, mean=0, std=1)
