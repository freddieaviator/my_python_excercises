values = [23,54,76,34,97,56,87,45,76,12,3,49,92]

def quantile(series,alpha = 0.05)->tuple:
    """ returns the numerical lower and upper confidence interval of the numbers in the series.
    
    args: Series of numbers and alpha(default 0.05)

    return: Tuple with numerical lower and upper confidence interval
   
    """
    series = sorted(series)
    lower_index = round(len(series)*alpha/2)
    upper_index = round(len(series)*(1-alpha/2)) -1
    return series[:lower_index],series[upper_index:]

print(quantile(values,0.5))