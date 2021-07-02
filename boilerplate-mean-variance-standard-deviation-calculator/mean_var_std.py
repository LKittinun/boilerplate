import numpy as np

def calculate(list):
    try:
        arrays = np.array(list).reshape(3,3)
    except: 
        raise ValueError("List must contain nine numbers.")
    
    ## mean
    mean1 = arrays.mean(axis = 0).tolist()
    mean2 = arrays.mean(axis = 1).tolist()
    meanall = arrays.mean()

    ## variance
    var1 = arrays.var(axis = 0).tolist()
    var2 = arrays.var(axis = 1).tolist()
    varall = arrays.var()

    ## standard deviation
    std1 = arrays.std(axis = 0).tolist()
    std2 = arrays.std(axis = 1).tolist()
    stdall = arrays.std()

    ## min
    min1 = arrays.min(axis = 0).tolist()
    min2 = arrays.min(axis = 1).tolist()
    minall = arrays.min()

    ## max
    max1 = arrays.max(axis = 0).tolist()
    max2 = arrays.max(axis = 1).tolist()
    maxall = arrays.max()

    ## sum
    sum1 = arrays.sum(axis = 0).tolist()
    sum2 = arrays.sum(axis = 1).tolist()
    sumall = arrays.sum()

    calculations =  {"mean": [mean1, mean2, meanall], "variance": [var1, var2, varall],
                    "standard deviation": [std1, std2, stdall], "max": [max1, max2, maxall],
                    "min": [min1, min2, minall], "sum": [sum1, sum2, sumall]}
    
    return calculations

print(calculate([9,1,5,3,3,3,2,9,0]))