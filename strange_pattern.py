import numpy as np

# implement the function strange pattern

def strange_pattern(shape):
    n, m = shape
    pattern=np.zeros(shape, dtype='bool')
    pattern[::3, ::3]=True
    pattern[1::3, 2::3]=True
    pattern[2::3, 1::3]=True

    return pattern


if __name__ == "__main__":
    # use this for your own testing!

    pass
