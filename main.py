import numpy as np



def t1_file_stat(filename):
    
    
    data = np.loadtxt(filename, delimiter='\t', dtype=np.float)
    dic = {}
    dic["mean"] = data.mean()
    dic["max"] = data.max()
    dic["min"] = data.min()
    dic["std_dev"] = data.std()
    dic["5th_central_moment"] = 0
    return {
        "mean": dic.get("mean"),
        "max": dic.get("max"),
        "min": dic.get("min"),
        "std_dev": dic.get("std_dev"),
        "5th_central_moment": dic.get("5th_central_moment")
    }

def t2_sort_int(array):
    return  np.sort(array)

def t3_sort_complex(complex_array):
    tup=np.sort_complex(complex_array)
    tup.tolist()
    module_array = ([abs(i) for i in complex_array.tolist()])
    d=dict(zip(module_array,complex_array))
    sorted(d.keys())
    
    return (np.array(list(d.values())),np.array(tup))

def t4_sort_string_len(string_array):
     return sorted(string_array, key = len)


def t5_sort_string_tuple(string_tuple):
    d=np.array(string_tuple)
    return tuple(np.sort(d))

