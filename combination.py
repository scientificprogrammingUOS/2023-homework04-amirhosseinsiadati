import numpy as np 

# implement your function to combine two numpy arrays 


def combination(arr1, arr2, axis=0):
    arr1 = np.squeeze(arr1)
    arr2 = np.squeeze(arr2)
    arr1_sh=list(arr1.shape)
    arr2_sh=list(arr2.shape)
    arr1_sh[axis] = arr2_sh[axis]
    if arr1_sh != arr2_sh:
        raise ValueError("Error: Arrays cannot be combined along the given axis")
    
    combined_arr = np.concatenate((arr1, arr2), axis=axis)
    
    return combined_arr

if __name__ == "__main__":
    # use this for your own testing!

    pass
