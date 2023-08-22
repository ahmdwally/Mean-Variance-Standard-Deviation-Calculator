import numpy as np

def calculate(input_li):
    '''
    this function takes a list of 9 digits and converts it to a 3x3 array and return a dictionary of mean, variance, standard deviation, max, min and sum of both axes and the flattened array
    
    :param input_li : list of 9 digits
    :return: dict of mean, variance, standard deviation, max, min, sum of both axes and flattened array
    '''

    if len(input_li) < 9:
       raise ValueError("List must contain nine numbers.")
    
    li = np.reshape(input_li, (3,3))
    
    def slicer(li):
        rows = []
        cols = []
        flattened = input_li
        transposed = np.transpose(li)
        for i in range(3):
            rows.append(list(li[i]))
        for i in range(3):
            cols.append(list(transposed[i]))
        return [cols,rows,flattened] 

    def applier(li,func):
        output = []
        for child_li in li :
            if not any(isinstance(i,list) for i in child_li):
                output.append(func(child_li))
            else:
                child = []
                for sub_child_li in child_li:
                    child.append(func(sub_child_li))
                output.append(child)
        return output
    
    sliced_li = slicer(li)
    return {'mean':applier(sliced_li,np.mean),
            'variance':applier(sliced_li,np.var),
            'standard deviation':applier(sliced_li,np.std),
            'max':applier(sliced_li,np.max),
            'min':applier(sliced_li,np.min),
            'sum':applier(sliced_li,np.sum)
            }


