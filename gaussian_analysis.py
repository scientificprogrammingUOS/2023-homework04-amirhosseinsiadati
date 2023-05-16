import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):

    if not all(isinstance(x, (int, float)) for x in [loc, scale, lower_bound, upper_bound]):
        return "Error: All inputs must be integers or floats"
    
    if lower_bound >= upper_bound:
        return "Error: lower_bound must be smaller than upper_bound"
    
    arr = np.random.normal(loc=loc, scale=scale, size=100)
    
    arr = arr[(arr >= lower_bound) & (arr <= upper_bound)]
    
    mean = np.mean(arr)
    std = np.std(arr)
    
    return (mean, std)



if __name__ == "__main__":
    # use this for your own testing!

    pass
