

def return_Array(arr, p, d):
    i = arr.index(p)
    new_list = []
    if(d == 0):
        new_list = arr[i+2:] + arr[0:i+2]
    else:
        new_list = arr[-i+1:] + arr[0:i]

    return new_list


arr = [1, 3, 2, 7, 4, 6, 9]
p = 4
n = len(arr)
d = 0
r_ar = return_Array(arr, p, d)
print(r_ar)
